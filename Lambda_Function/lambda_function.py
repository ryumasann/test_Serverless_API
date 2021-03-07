import boto3 #AWS SDK for Python

dynamodb = boto3.resource('dynamodb')
#boto3.resource('')にサービス名を入れて操作するサービスを指定
table = dynamodb.Table('MemberTable')

def get_member(id):
    response = table.get_item(#boto3の関数
        Key={
            'MemberId': id
        }
    )
    return response['Item']#リストやタプルの表記

def lambda_handler(event, context):#ラムダ関数で呼び出される関数名と引数
    #「Runtime settings」のlambda_function.lambda_handler
    member = get_member('001')#関数にid=001が入り呼び出される
    return member