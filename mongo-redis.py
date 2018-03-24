import redis
import json
from bson.json_util import dumps
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
redisClient = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

database = client['DummyDb'] #database name in mongodb
userList = database['Users'].find() #collection name in 'DummyDb' database

serializedObj = dumps(userList) #serialize object for the set redis.
result = redisClient.set('users', serializedObj) #set serialized object to redis server.

#you can check the users in redis using redis gui or type 'get users' to redis client or just get it from the redis like below.
parsedUserList = json.loads(redisClient.get('users'))

for user in parsedUserList: #check the names
	print(user["username"]) #'username' one of the field of the 'Users' collection