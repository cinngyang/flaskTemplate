#codeing=utf-8



import boto3

pool_id='ap-northeast-1_vaao326oJ'
client_id='3u8f2lqj0llpir7jnfndu96hjh'
client = boto3.client('cognito-idp', region_name='ap-northeast-1')
response = client.admin_get_user(UserPoolId=pool_id,Username='chin')


import boto3
from warrant import Cognito
from warrant.aws_srp import AWSSRP

from dotenv import load_dotenv
import os

print(f"boto3 version {boto3.__version__}")
print(f"boto3 get_available_services{boto3.Session().get_available_services()}")


#載入 應用程式端 poolid & clientid
load_dotenv()
poolid=os.getenv('user-pool-id')
clientid=os.getenv('client-id')
client_secret=os.getenv('client_secret')
print(f"pool id {poolid}")
print(f"client id {clientid}")

#新增使用者
#client = boto3.client('cognito-idp')
#u = Cognito(poolid,clientid)
#u.add_base_attributes(email='chinng.yang@gmail.com',name='chinng.yang@gmail.com')
# u.register('chinng.yang@gmail.com','Itaa0$@1847')


client = boto3.client('cognito-idp')
u = Cognito(user_pool_id=poolid,client_id=clientid,username='cinng.yang@gmail.com')
u.admin_authenticate(password='Itaa0@1847')


u.authenticate(password='bobs-password')
u.change_password('Itaa0@1847','Itaa0@1874')
u.authenticate(password='Itaa0@1847')
#u.confirm_sign_up('Itaa0$@1847',username='chinng.yang@gmail.com')






