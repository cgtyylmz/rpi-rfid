import RPi.GPIO as GPIO
import MFRC522
import signal
import csv
import json

continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

def check_uid(uid):

    with open('/home/pi/RFID/test.csv') as f:

        reader = csv.reader(f)
        
        avai = False
        for row in reader:
            if uid == row[0]:
                avai = True
                break
            else:
                avai = False
        if avai:
            print(json.dumps({"result":1}))
        else:
            print(json.dumps({"result":0}))

while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        uid.pop(4)
        uid = [str(i) for i in uid]
        uid = ''.join(uid)
        check_uid(uid)
