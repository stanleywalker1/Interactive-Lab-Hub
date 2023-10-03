# International Hotline

## Hardware Set-Up

For this demo, you will need: 
* a Raspberry Pi, 
* a Qwiic/Stemma Cable, 
* the display (we are just using it for the Qwiic/StemmaQT port. Feel free to use the display in your projects), 
* a keypad
* a web camera


* Receives input audio through the microphone
* Transcribe (or translate if necessary) with Wishper API
* Send it to OPENAI ChatGPT API
* Use Google Text-to-Speech API to read ChatGPT response out loud

Plug the display in and connect the keypad to the port underneath with your Qwiic connector cable. Plug the web camera into the raspberry pi. 

## Software Setup

Ssh on to your Raspberry Pi

`ssh pi@yourHostname.local`

Ensure audio is playing through the aux connector by typing

`sudo raspi-config`

on `system options` hit enter. Go down to `s2 Audio` and hit enter. Select `1 USB Audio` and hit enter. Then navigate to `<Finish>` and exit the config menu.

We will need one additional piece of software called VLC Media player. To install it type `sudo apt-get install vlc` 


I would suggest making a new virtual environment for this demo then navigating to this folder and installing the requirements.

```
pi@yourHostname:~ $ virtualenv woz
pi@yourHostname:~ $ source woz/bin/activate
(woz) pi@yourHostname:~ $ cd Interactive-Lab-Hub/Lab\ 3/demo
(woz) pi@yourHostname:~/Interactive-Lab-Hub/Lab 3/demo $ 
(woz) pi@yourHostname:~/Interactive-Lab-Hub/Lab 3/demo $ pip install -r requirements.txt
```

You also need to create a new file called `myapikeys.py` with this line inside:
`OPENAI_KEY = "my-apikey-goes-here"`

## Running

To run the app

`(woz) pi@yourHostname:~/Interactive-Lab-Hub/Lab 3/international-hotline $ python app.py`

to respond to the "person" on the other end of the phone, hit enter once to start recording your message, and hit enter again to stop and send your message






