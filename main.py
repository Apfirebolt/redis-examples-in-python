import redis
client = redis.Redis(host='localhost', port=6379, db=0)
client.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

client.lpush('LanguageList', "Kotlin")

client.lpush('LanguageList', "Python")
                               
# Add key value pairs to the Redis hash

client.hset("NumberVsString", "1", "One")

client.hset("NumberVsString", "2", "Two")

client.hset("NumberVsString", "3", "Three")

# Retrieve the value for a specific key

print("Value for the key 3 is")

print(client.hget("NumberVsString", "3"))

 

print("The keys present in the Redis hash:");

print(client.hkeys("NumberVsString"))

 

print("The values present in the Redis hash:");

print(client.hvals("NumberVsString"))

 

print("The keys and values present in the Redis hash are:")

print(client.hgetall("NumberVsString"))

 

# Push multiple values through the HEAD of the list

client.lpush('LanguageList', "Java", "C++")

 

# Print the contents of the Redis list

while(client.llen('LanguageList')!=0):

    print(client.lpop('LanguageList'))

dork = client.get("Amit")
print(dork)
