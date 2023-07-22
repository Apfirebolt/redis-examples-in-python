# import pandas and read csv file
import redis
import pandas as pd

df = pd.read_csv('myntra.csv')
client = redis.Redis(host='localhost', port=6379, db=0)

# get first 20 rows of df with columns

header_data = df.head(20)

# Push data in a list in redis

for data in header_data['Description']:
    client.lpush('ProductList', data)

# Get ProductList data from redis

print('Redis data ..')
while(client.llen('ProductList')!=0):
    print(client.lpop('ProductList'))
