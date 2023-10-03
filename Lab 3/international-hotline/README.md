# International Hotline

## Hardware Set-Up

For this demo, you will need: 
* a Raspberry Pi, 
* a Qwiic/Stemma Cable, 
* the display (we are just using it for the Qwiic/StemmaQT port. Feel free to use the display in your projects), 
* a keypad
* a web camera

Plug the display in and connect the keypad to the port underneath with your Qwiic connector cable. Plug the web camera into the raspberry pi. 

## Software Setup

Whats happening under the hood:
* Receives input audio through the microphone
* Transcribe (or translate if necessary) with Wishper API
* Send it to OPENAI ChatGPT API
* Use Google Text-to-Speech API to read ChatGPT response out loud

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


demo conversation
```
pi@user:~/Interactive-Lab-Hub/Lab 3/demo $ python app.py
<qwiic_keypad.QwiicKeypad object at 0x7f62956eb0>
The Qwiic Keypad is connected.
Please type in a 9 digit phone number.
we have a phone number: 354458525
  ** Press enter to start recording **
  ** Press enter to stop recording **
Me: Hi, my name is Stanley. Where are you from?
GPT: Hey Stanley, nice to meet you! I'm originally from the beautiful coastal town of Cape Town, South Africa. How about you?
  ** Press enter to start recording **
  ** Press enter to stop recording **
Me: I'm from Charlotte, North Carolina, but right now I'm in New York at Cornell Tech.
GPT: Oh, that's quite a change, going from Charlotte to New York! How are you finding the bustling city life so far?
  ** Press enter to start recording **
  ** Press enter to stop recording **
Me: It's pretty good. It was flooded over the weekend, but now it's nice What do you think of Cape Town? I want to visit one day
GPT: Cape Town is absolutely stunning! The picturesque beaches, majestic Table Mountain, and vibrant cultural scene make it a must-visit destination. You'll definitely enjoy exploring the city and its breathtaking surroundings.
  ** Press enter to start recording **
  ** Press enter to stop recording **
Me: Cool, do you have anything planned today? An vibrant cultural scene make it a must-visit destination. You'll definitely enjoy exploring the city and its breathtaking surroundings.
GPT: Actually, I'm about to meet up with some friends to go hiking in the mountains just outside of Cape Town. The views from up there are absolutely breathtaking!
  ** Press enter to start recording **
  ** Press enter to stop recording **
Me: Oh, that's pretty cool. Did you meet your friends on this phone line as well or somewhere else?
GPT: No, I met my friends through various activities and mutual connections in Cape Town. We've known each other for a while now and love exploring the outdoors together.
  ** Press enter to start recording **
  ** Press enter to stop recording **
Me: That's pretty cool. Well, I hope I can visit one day. I don't want to keep you holding for too long. Hiking sounds really fun.
GPT: Thank you, Stanley! It was great chatting with you. I hope you get the chance to visit Cape Town and have your own amazing adventures. Take care and have a fantastic day!
  ** Press enter to start recording **
  ** Press enter to stop recording **
Me: Thanks. Bye-bye.
GPT: Goodbye, Stanley! Take care and have a wonderful day. Safe travels and hope to chat with you again sometime. Bye-bye!
  ** Press enter to start recording **^Z
[2]+  Stopped                 python app.py

```





