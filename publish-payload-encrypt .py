import time
import paho.mqtt.client as paho
from cryptography.fernet import Fernet
broker="broker.hivemq.com"
#broker="192.168.1.3"
#define callback
def on_log(client, userdata):
    
def on_message(client, userdata, message):
   #time.sleep(1)
   print("receive payload ",message.payload)
   decrypted_message = cipher.decrypt(message.payload)   #decrypted_message = cipher.decrypt(encrypted_message)
   print("\nreceived message =",str(decrypted_message.decode("utf-8")))


client= paho.Client("client-pub")
client.on_log=on_log
######
client.on_message=on_message
#####encryption
#cipher_key = Fernet.generate_key()
cipher_key=b'WDrevvK8ZrPn8gmiNFjcOp2xovBr40TCwJlZOyI94IY='
cipher = Fernet(cipher_key)
message = b'on33'
#message = b'the quick brown fox jumps over the lazy dog'
encrypted_message = cipher.encrypt(message)
out_message=encrypted_message.decode()# turn it into a string to send
##
print("connecting to broker ",broker)
client.connect(broker)#connect
print("publishing encrypted message ",encrypted_message)
out_message="25 C"
client.publish("home/temp",out_message)#publish
time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop
