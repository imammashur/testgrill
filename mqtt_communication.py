import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to server")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    msg = message.payload
    msg = msg.decode("utf-8")
    print("Package received: "  + msg)
 
Connected = False   #global variable for the state of the connection
 
broker_address= 'farmer.cloudmqtt.com'  #Broker address
port = 17014                         #Broker port
user = "mggxilrp"                    #Connection username
password = "5zBND5VHiieI"            #Connection password
 
client = mqttClient.Client("Receiver")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
 
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("testgrill")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
