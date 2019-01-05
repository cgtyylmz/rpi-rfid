# rpi-rfid
RFID access control using Raspberry Pi Zero W.

## Requirements
* SPI-Py
	* Clone git repository
		`git clone https://github.com/lthiery/SPI-Py.git`
	* Change directory
		`cd SPI-Py`
	* And install
		`sudo python setup.py install`
* MFRC522-Python


## Node-Red Folow

`[{"id":"8cec8011.f34d","type":"tab","label":"Flow 1","disabled":false,"info":""},{"id":"6ddcfc2e.0ba384","type":"rpi-gpio out","z":"8cec8011.f34d","name":"","pin":"7","set":true,"level":"0","freq":"","out":"out","x":680,"y":360,"wires":[]},{"id":"ac9e10bb.08f968","type":"trigger","z":"8cec8011.f34d","op1":"1","op2":"0","op1type":"str","op2type":"str","duration":"1000","extend":false,"units":"ms","reset":"","bytopic":"all","name":"","x":360,"y":360,"wires":[["6ddcfc2e.0ba384"]]},{"id":"ca4aa92f.eddfe8","type":"exec","z":"8cec8011.f34d","command":"python /home/pi/RFID/Read.py","addpay":true,"append":"","useSpawn":"true","timer":"","oldrc":false,"name":"","x":370,"y":100,"wires":[["f3c4fe23.453148"],[],[]]},{"id":"22e572bf.efab96","type":"debug","z":"8cec8011.f34d","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":870,"y":40,"wires":[]},{"id":"f3c4fe23.453148","type":"json","z":"8cec8011.f34d","name":"","property":"payload","action":"","pretty":false,"x":680,"y":60,"wires":[["22e572bf.efab96","90a7e63a.355b98"]]},{"id":"3c1356db.296772","type":"switch","z":"8cec8011.f34d","name":"","property":"payload","propertyType":"msg","rules":[{"t":"eq","v":"1","vt":"num"},{"t":"eq","v":"0","vt":"num"}],"checkall":"true","repair":false,"outputs":2,"x":150,"y":400,"wires":[["ac9e10bb.08f968"],["cc7f73f1.750178"]]},{"id":"cc7f73f1.750178","type":"trigger","z":"8cec8011.f34d","op1":"1","op2":"0","op1type":"str","op2type":"str","duration":"1000","extend":false,"units":"ms","reset":"","bytopic":"all","name":"","x":360,"y":440,"wires":[["ce5e018a.01aa2"]]},{"id":"90a7e63a.355b98","type":"function","z":"8cec8011.f34d","name":"Identify Car","func":"if(msg.payload.result==1) {\n    msg.payload=1;\n}\n//If car plate and car model don't match\nelse {\n    msg.payload=0;   \n}\n\nreturn msg;\n\n","outputs":1,"noerr":0,"x":610,"y":200,"wires":[["3c1356db.296772"]]},{"id":"ce5e018a.01aa2","type":"rpi-gpio out","z":"8cec8011.f34d","name":"","pin":"11","set":true,"level":"0","freq":"","out":"out","x":680,"y":440,"wires":[]},{"id":"3081e240.837e06","type":"inject","z":"8cec8011.f34d","name":"","topic":"","payload":"Started!","payloadType":"str","repeat":"","crontab":"","once":true,"x":100,"y":100,"wires":[["ca4aa92f.eddfe8"]]}]`
