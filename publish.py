import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT



ENDPOINT = "akzky8hi6tf2a-ats.iot.ap-south-1.amazonaws.com"
CLIENT_ID = "testDevice"
PATH_TO_CERTIFICATE = "certificates/73d46fd77375d5531a0ac7139570e148feb9fc453d282e0a3c9f06461147930f-certificate.pem (1).crt"
PATH_TO_PRIVATE_KEY = "certificates/73d46fd77375d5531a0ac7139570e148feb9fc453d282e0a3c9f06461147930f-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "certificates/root.pem"
MESSAGE = "Hello World"
TOPIC = "test/testing"
RANGE = 8

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"message" : data}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)
print('Publish End')
myAWSIoTMQTTClient.disconnect()