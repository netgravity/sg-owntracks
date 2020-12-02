import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
    print ("inside on_connect function")
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print ("Message received: "  + message.payload)
 
Connected = False   #global variable for the state of the connection
 
broker_address= "enigma.netgravity.org"
port = 1234
user = "xxxx"
password = "xxxxx"

print ("starting")
client = mqttClient.Client("python1")               #create new instance
print ("Created class")
client.username_pw_set(user, password=password)    #set username and password
print ("credentials entered")
client.on_connect=on_connect                      #attach function to callback
print ("on_connect function defined")
client.on_message=on_message                      #attach function to callback
print ("on_message function defined")
client.connect(broker_address, port=port)          #connect to broker
print ("connect function")
client.loop_start()        #start the loop
print ("Entering loop")
print Connected
#while Connected != True:    #Wait for connection
#    time.sleep(0.1)
 
client.subscribe("/owntracks/SunnyG-owntracks/SG")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()
