from boto3 import resource
from boto3.dynamodb.conditions import Key

# THIS ACTUALLY WORKS!!! Stolen from https://stackoverflow.com/questions/53935211/query-all-items-by-partition-key-in-dynamo-using-boto3
dynamodb_resource = resource('dynamodb')

def query_table(table_name, key=None, value=None):
    table = dynamodb_resource.Table(table_name)

    if key is not None and value is not None:
        filtering_exp = Key(key).eq(value)
        return table.query(KeyConditionExpression=filtering_exp)

    raise ValueError('Parameters missing or invalid')

if __name__ == '__main__':
    resp = query_table(
        table_name='searchItems', 
        key='email', 
        value='222222'
    )
    items = resp.get('Items')
    print(len(items))
    print(items)