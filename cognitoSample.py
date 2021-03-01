import boto3
from warrant.aws_srp import AWSSRP
from warrant import Cognito
from dotenv import load_dotenv
import os


print(boto3.__version__)
print(boto3.Session().get_available_services())

load_dotenv()
poolid=os.getenv('user-pool-id')
clientid=os.getenv('client-id')
pwd=os.getenv('password')


#init

#u = Cognito(poolid,poolid)
#Add User
#u.add_base_attributes(email='chin.yang@lextar.com')
#u.register('chin.yang@lextar.com', 'p4319p4319')


#Admin Authenticate
u = Cognito(poolid,clientid,username='cinng.yang@gmail.com')
u.admin_authenticate(password=pwd)
print(u.access_token)
print(u.get_key)
print('done')



# client = boto3.client('cognito-idp')
# aws = AWSSRP(username='chin.yang@lextar.com', password=pwd, pool_id=poolid,
#              client_id=clientid, client=client)
# tokens = aws.authenticate_user()

# print(tokens['AccessToken'])
# print(tokens['RefreshToken'])
# print(tokens['TokenType'])
# print(tokens['IdToken'])