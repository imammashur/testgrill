import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
app = Flask(__name__)

mqttc=mqtt.Client()
mqttc.connect("localhost",1883,60)
mqttc.loop_start()

pins = {
   4 : {'name' : 'GPIO 4', 'board' : 'esp8266', 'topic' : 'esp8266/4', 'state' : 'False'},
   5 : {'name' : 'GPIO 5', 'board' : 'esp8266', 'topic' : 'esp8266/5', 'state' : 'False'}
   }

# Put the pin dictionary into the template data dictionary:
templateData = {
   'pins' : pins
   }

@app.route("/")
def main():
   return render_template('main.html', **templateData)

@app.route("/<board>/<changePin>/<action>")

def action(board, changePin, action):
   changePin = int(changePin)
   devicePin = pins[changePin]['name']
   if action == "1" and board == 'esp8266':
      mqttc.publish(pins[changePin]['topic'],"1")
      pins[changePin]['state'] = 'True'

   if action == "0" and board == 'esp8266':
      mqttc.publish(pins[changePin]['topic'],"0")
      pins[changePin]['state'] = 'False'

   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8181, debug=True) 
