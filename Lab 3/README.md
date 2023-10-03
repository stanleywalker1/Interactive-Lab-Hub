# Chatterboxes
**NAMES OF COLLABORATORS HERE**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

**Please note:** connect the webcam/speaker/microphone while the pi is *off*. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Setup 

*DO NOT* forget to work on your virtual environment! 

Run the setup script
```chmod u+x setup.sh && sudo ./setup.sh  ```

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the directory is a folder called `speech-scripts` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/speech-scripts $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files `.sh` by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/speech-scripts $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech
```
You can test the commands by running
```
echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? 
Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

The file name for this is: thomas_and_stanley_greeting_pi.sh

---
Bonus:
[Piper](https://github.com/rhasspy/piper) is another fast neural based text to speech package for raspberry pi which can be installed easily through python with:
```
pip install piper-tts
```
and used from the command line. Running the command below the first time will download the model, concurrent runs will be faster. 
```
echo 'Welcome to the world of speech synthesis!' | piper \
  --model en_US-lessac-medium \
  --output_file welcome.wav
```
Check the file that was created by running `aplay welcome.wav`. Many more languages are supported and audio can be streamed dirctly to an audio output, rather than into an file by:

```
echo 'This sentence is spoken first. This sentence is synthesized while the first sentence is spoken.' | \
  piper --model en_US-lessac-medium --output-raw | \
  aplay -r 22050 -f S16_LE -t raw -
```
  
### Speech to Text

Next setup speech to text. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 
```
pip install vosk
pip install sounddevice
```

Test if vosk works by transcribing text:

```
vosk-transcriber -i recorded_mono.wav -o test.txt
```

You can use vosk with the microphone by running 
```
python test_microphone.py -m en
```

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

The file name for this is: phone_number_ask.sh
### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

We began thinking about text-to-speech and then speech-to-text. In the speech-to-text we thought of a smart assistant that looks at how you are speaking and gives you feedback/cues on where you are putting emphasis, for example, if you talked loudly it could bold the letters, or change the font size or put in a word cloud where the loudest or highest pitch is the biggest. Another example we thought of was a strange talking animal, where it could act like a kids toy and offer funness to kids! Finally we thought about a scream-o-meter, which could be used in sports games, depending on how loud the crowd goes, how high the meter goes, another idea could be like one of those festival games called high striker (you hit and it rings a bell). For text-to-speech we thought about a Human-GPT, where you could ask it something and a human responds, maybe something completely irrelevant, or funny. Another idea we had here was to it be able to read a book or a script and it read you, maybe a bed time story. Finally we thought of a Target "That-was-easy button" here the idea would be that you would press it and it would say something fun!
<img width="1395" alt="270742773-238505cf-ab95-4443-a785-7829c086023e" src="https://github.com/stanleywalker1/Interactive-Lab-Hub/assets/24898801/600cd410-67bf-4dde-b55f-274b1e87d772">

We decided on the Target "That-was-easy button", here is our storyboard: 
<img width="1052" alt="270754592-07bddade-572e-4dee-8253-127217300e02" src="https://github.com/stanleywalker1/Interactive-Lab-Hub/assets/24898801/745c2548-d028-486a-af1f-6b81ebcaff8f">

but after class we realized it was too boring, so we pivoted to a world that you move/shake & speak to, while moving it will change how it speaks back to you, in the specific language of the country that is at its center at that time: 


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses.

\*\***Please describe and document your process.**\*\*

We imagine the world asking you if you speak the language of that specific country that is at its center. Once you move it will reask the question in that specific language. Once you respond yes, the world will begin to talk to you and asks you questions, or wait for you to converse.

<img width="850" alt="Screen Shot 2023-10-02 at 11 11 54 PM" src="https://github.com/stanleywalker1/Interactive-Lab-Hub/assets/24898801/6d300018-3f4e-4ecf-9571-22172e8d153c">

### Acting out the dialogue


https://github.com/stanleywalker1/Interactive-Lab-Hub/assets/24898801/168ed3a6-10dc-4859-86f1-9e21a965d703


Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).


https://github.com/stanleywalker1/Interactive-Lab-Hub/assets/24898801/e9243eec-6f34-4741-b601-26fc27f91396


\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

# International Hotline

## Hardware Set-Up

What we used: 
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
* Send it to OpenAI ChatGPT API
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

## Videos & Pictures


![WhatsApp Image 2023-10-02 at 10 50 58 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/5e9f5e5f-3336-41a0-a4b2-a1373a1c5cc2)
![WhatsApp Image 2023-10-02 at 10 51 10 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/94cc1ee4-92d8-4d40-9cb1-82d274568af4)
![WhatsApp Image 2023-10-02 at 10 51 20 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/8d6f0401-bcbe-49e1-be07-8fa3648ded73)
![WhatsApp Image 2023-10-02 at 7 32 48 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/98fdcd73-c23b-40f6-91a3-c8c23f115d87)
![WhatsApp Image 2023-10-02 at 10 50 50 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/2e481b09-3f5c-4b86-a453-f5300e199eaa)

https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/06b3d909-4275-45b8-b58f-5278777ddbbf



## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)


Answer the following:

### What worked well about the system and what didn't?

#### What Worked:

- Using OpenAI API: Adding the OpenAI API really helped make user conversations more natural and smooth.
- Simple Design: Keeping the interface simple with just a keypad naturally encouraged users to start typing and interacting, which was a big win in terms of user engagement.

#### What Didn't Work:

- Instruction Clarity: Initially, the instructions were too vague, so for example we had changed "enter a phone number" to "enter a 9-digit phone number" to make things clearer for users.
- Technical Issues: We ran into a bunch of I/O errors during testing, thinking that perhaps the sleep interval was too short, causing the while loop to run too quickly and overload the system and keypad, by increasing the sleep time, it stopped causing so many I/O errors.
- Library and Version Problems: Dealing with library and version issues, although common in coding, was a bit of a headache.

### What worked well about the controller and what didn't?

#### What Worked:

- The controller was simple and intuitive, naturally prompting users to engage and interact with the system.

#### What Didn't Work:

- We found issues related to the timing and frequency of hardware calls, showing us that we need to refine the control logic and manage I/O processes to avoid errors and keep it stable.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

- Clear Communication: One key lesson was the absolute need for clear and direct user instructions to enhance the user experience and avoid confusion.
- Technical Stability: We learned how important it is to manage potential technical issues, like those related to I/O processing and looping, to keep the system running smoothly.
- Keep It Simple: Maintaining intuitive user interaction is crucial, suggesting that future designs should keep things simple while also looking for ways to improve user interactions.
- Managing Dependencies: We saw firsthand how crucial it is to manage dependencies effectively to prevent library and version issues from affecting the user experience.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

#### Creating a Dataset:
- Recording Interactions: We could log all user inputs and system outputs.
- Collecting User Feedback: Getting feedback from users after they interact with the system will give us insights into their experience and any issues or unexpected system responses they encountered.

#### Additional Sensing Modalities:
- Facial Expression or Gesture Recognition: Using a camera to analyze facial expressions or recognize gestures might give us more insight into user engagement and emotional responses. Just like companies like Humane or Rewing are exploring as of October 2023.


