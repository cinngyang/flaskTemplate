# coding=utf-8
import numpy as np
import pandas as pd



class ChartData():


    def HtmlItem(self):

        elements = ['First','Second', 'Third','Fourth','Fifth','Sixth','Seventh',
        'Eighth','Ninth','Tenth','Eleventh','Twelfth']

        return elements

    def LinChat(self):
        #產生 12 個亂數
        np.random.seed(12)
        Qty=list()
        Ratio=list()
        num = 0
        while(num < 12):
            Qty.append(np.random.random_integers(50000,100000))
            Ratio.append(np.random.random_integers(30,100))
            num +=1
        month=[1,2,3,4,5,6,7,8,9,10,11,12]

        dfData=pd.DataFrame({'Month':month,'Qty':Qty,'Ratio':Ratio})
    
        return dfData

    def pichart(self):
        pie = {
        'values': [100, 50, 30, 20],
        'labels': ['香蕉', '蘋果', '水梨', '草莓'],
        'type': 'pie'
    }

    # 將相關圖表物件以list方式寫入
    

    



