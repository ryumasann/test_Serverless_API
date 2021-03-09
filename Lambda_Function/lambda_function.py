import boto3 #AWS SDK for Python

dynamodb = boto3.resource('dynamodb')
#boto3.resource('')にサービス名を入れて操作するサービスを指定
table = dynamodb.Table('MemberTable')

#def get_member(id):
#    response = table.get_item(#boto3の関数
#        Key={
#            'MemberId': id
#        }
#    )
#    return response['Item']#取得したItemは辞書型のためリストやタプルの表記

    #「Runtime settings」のlambda_function.lambda_handler
def lambda_handler(event, context):#ラムダ関数で呼び出される関数名と引数
    #eventはpathパラメタ、contextは
    if len(event) == 0:
    #GET処理(パラメーターを渡さない想定)
        tableData = table.scan(
            #ReturnConsumedCapacity='TOTAL'を入れないとテーブル名を取得できない
            ReturnConsumedCapacity='TOTAL'
            )
        try:
            #scanでデータを取得できない場合は変数がからのためNameError
            strTableName = tableData['ConsumedCapacity']['TableName']
            dicTableItems = tableData['Items']
            return strTableName, dicTableItems
        
        except NameError:
            noRet = {"message":"There is no corresponding record"}
            return noRet
        #member = get_member(event['MemberId'])#関数にid=001が入り呼び出される
        #return member
    else:
    #POST処理
        item = {
            "MemberId": str(event["MemberId"]),
            "Name": str(event["MemberName"])
        }
        
        table.put_item(Item=item)
        
        return event