import pandas as pd 
import pymysql 
import pymssql 
#import cx_Oracle
import pandas as pd
import os
from sqlalchemy import create_engine
from datetime import datetime

class dbConnect():
    
    dtConf=pd.DataFrame()
    FilePath=os.path.dirname(__file__)
        
    def __init__(self):
        print (self.FilePath)
        confFile="{0}\dbconf.conf".format(self.FilePath)
        self.dtConf=pd.read_csv(confFile)
        
        #mySql
        self.pi='pi'  

    def WiteLog(self,Msg):
        """Write Log""" 
        fileName="dbConn_"+datetime.now().strftime('%Y%m%d')+".log"
        with open(fileName,'a',encoding='utf-8') as fi:
            Msg=datetime.now().strftime('%Y%m%d %H:%M:%S')+","+Msg+"\n"
            fi.write(Msg)  
            fi.close()    
    
    def mySqlCon(self,ServerName,dbName):
        
        #取得 mySql 連線
        usr=self.dtConf.loc[self.dtConf['ServerName']==ServerName,'user'].tolist()[0]
        pwd=self.dtConf.loc[self.dtConf['ServerName']==ServerName,'pwd'].tolist()[0]    
        host=self.dtConf.loc[self.dtConf['ServerName']==ServerName,'host'].tolist()[0]  

        conn = pymysql.connect(host=host, port=3306, user=usr, passwd=pwd,
                db=dbName, charset='utf8')
        
        return conn
        
    def mySqlQuer(self,ServerName,dbName,sqlstr):
        
        cn=self.mySqlCon(ServerName,dbName)
        df=pd.read_sql(sqlstr,cn)
        
        return df
    
    def mySqlExCmd(self,ServerName,dbName,sqlstr):
        strsql=""
        
        try :

            cn=self.mySqlCon(ServerName,dbName)      
            cur = cn.cursor()     
            cur.execute(strsql)
            
            cn.commit()
            cur.close()
            cn.close()

        except  Exception as err:
            
            msg="mySqlInsDataFrame"+err+"\r\n"
            msg+=strsql+"\r\n"
            self.WiteLog(msg)
            return  0     
                
        return True
            
    def mySqlInsDataFrame(self,ServerName,dbName,tableName,df):
        strsql=""
        
        try :

            cn=self.mySqlCon(ServerName,dbName)       
            
            cur = cn.cursor()     
            cols=df.columns.tolist()
            
            for ix in df.index:
                data=df.iloc[ix,:].tolist()        
                strsql="INSERT INTO "+tableName+"("+','.join(cols)+") VALUES ("        
        
                for i in data:
                    strsql+="'"+str(i)+"',"         
                
                strsql=strsql[:len(strsql)-1]
                strsql+=")"  

                cur.execute(strsql)
                cn.commit()

            cur.close()
            cn.close()

        except  Exception as err:
            
            msg="mySqlInsDataFrame"+err+"\r\n"
            msg+=strsql+"\r\n"
            self.WiteLog(msg)
            return  0     
                
        return df.shape[0]

