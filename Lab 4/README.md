# Ph-UI!!!

**Thomas Wallace & Stanley Walker**


For lab this week, we focus both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:


**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.
```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

Option 3: (preferred) use the Github.com interface to update the changes.

### Start brainstorming ideas by reading: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

* New hardware for your kit will be handed out. Update your parts list. 


(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Camera Test](#part-f)

G) [Record the interaction](#part-g)


## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
 
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). Install the latest requirements from your working virtual environment:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip install -r requirements.txt

```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 
 
<img src="https://cdn-shop.adafruit.com/970x728/3595-06.jpg" width=200>
 

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder (optional)

> **_NOTE:_**  Not in the kit yet - skip this.

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separate breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">

   
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick (optional)


A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### Distance Sensor


Earlier we have asked you to play with the proximity sensor, which is able to sense objects within a short distance. Here, we offer [Sparkfun Proximity Sensor Breakout](https://www.sparkfun.com/products/15177), With the ability to detect objects up to 20cm away.

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/9/2/15177-SparkFun_Proximity_Sensor_Breakout_-_20cm__VCNL4040__Qwiic_-01.jpg" height="200" />

</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python qwiic_distance.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Proximity_Py) to learn more about the sensor and see other examples

### Part C
### Physical considerations for sensing


Usually, sensors need to be positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.


**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

For all of these ideas, I'm thinking of using the distance sensor:
1. Social Distance Monitor: A device that helps people maintain 6 feet of distance from you, which could be because of COVID or personal preference.
2. Automated Sanitizer Dispenser: As you reach out with your hand, hand sanitiser will automatically be 
3. Adaptive Car Parking Assistant: As you back into parking, this device will tell you how close or far you are from bumping into the wall
4. Touchless Elevator Control: Distance sensor that recognizes how far up or down the hand is, relating to the floor.
5. Interactive Museum Exhibit: As you approach the gallery, interactive parts of the exhibit become alive
6. Interactive Play Mat for Pets/Kids: A mat that detects the presence of a pet/kid and activates interactive elements (like lights or gentle movements) to entertain them.
7. Smart Retail Mannequins: Mannequins in retail stores that activate and display additional information about the clothing when a customer approaches.


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to answer those questions?\*\*\***

These are the questions that are raised for each:

1. Social Distance Monitor
* Questions:
    * How will the device notify the user and surrounding individuals about maintaining distance without causing alarm or discomfort?
    * How can it distinguish between people and other objects?
* Prototyping Needs:
    * Explore different alert mechanisms (vibration, light, sound).
    * Validate sensor accuracy in various environments.
2. Automated Sanitizer Dispenser
* Questions:
    * What is the optimal sensor range to trigger the dispenser without accidental activation?
    * How will it handle varying hand sizes and shapes?
* Prototyping Needs:
    * Determine a mechanism to dispense controlled sanitizer amounts.
    * Test sensor responsiveness with different hand positions and distances.
3. Adaptive Car Parking Assistant
* Questions:
    * How will the device communicate distance information effectively to the driver?
    * How will it deal with different car sizes and parking spaces?
* Prototyping Needs:
    * Develop a feedback system (visual/auditory) that provides clear, real-time distance information.
    * Evaluate functionality in different parking scenarios.
4. Touchless Elevator Control
* Questions:
    * How to ensure the system interprets gestures accurately and prevents misreads?
    * How will it assist individuals with disabilities or varying heights?
* Prototyping Needs:
    * Test gesture recognition for selecting different floors.
    * Ensure accessibility for diverse user demographics.
5. Interactive Museum Exhibit
* Questions:
    * How to balance engagement and prevent overwhelming or distracting the audience?
    * How can it adapt to groups versus individual visitors?
* Prototyping Needs:
    * Create interactive content that enhances the exhibit experience.
    * Observe user engagement and adapt interactivity accordingly.
6. Interactive Play Mat for Pets/Kids
* Questions:
    * How to ensure safety and durability of the mat given the varied activities of pets/kids?
    * How can it adapt to different play styles and preferences?
* Prototyping Needs:
    * Explore different interactive elements (light, movement) that are safe and enticing.
    * Test the mat's durability and safety with actual use scenarios.
7. Smart Retail Mannequins
* Questions:
    * How to deliver additional information in a way that’s engaging and not intrusive to the shopping experience?
    * How will it respond to different customer behaviors and interactions?
* Prototyping Needs:
    * Design an interface or medium to communicate the clothing information.
    * Analyze customer interaction and refine the information delivery mechanism. 

**\*\*\*Pick one of these designs to prototype.\*\*\***


### Part D
### Physical considerations for displaying information and housing parts



Here is a Pi with a paper faceplate on it to turn it into a display interface:


<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>


Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibly mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />

</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

Build a cardboard prototype of your design.


**\*\*\*Document your rough prototype.\*\*\***


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

> **_NOTE:_**  Not in the kit yet.

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which is included in your kit. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.


<img src="Servo_Setup.jpg" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.


Now that you have a basic idea of what a servo motor is, look into the script `servo_test.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degrees. Try running the servo example code now and see what happens:


```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!


### Part F (Optional)
### Camera
You can use the inputs and outputs from the video camera in the kit. 
We provide another script called camera_test.py to test the USB camera on raspberry pi. 
It uses qt to render a video to the screen, so it is necessary to connect a screen or to connect via VNC to run this script. 

First install some more dependencies into your virtual environment. OpenCV should already be installed on the Pi for the super user. 

```
sudo apt-get install portaudio19-dev python-all-dev
pip install opencv-python pyaudio pygame
```

Once executed the script will render the camera output, press 'q' to stop video and record a sound through the microphone which will be played back by specificing the audio output. 

---
The video is rendered locally on the pi. For wizarding interactions and prototyping it can be necessary to stream the video to another device such as your laptop. A wizard, observing the user and acting as a computer vision algorithm, can then trigger interactions remotley, such as we did in the tinkerbelle lab.

The following resources are good starts on how to stream video: 
* [OpenCV – Stream video to web browser/HTML page](https://pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/)
* [Live video streaming over network with OpenCV and ImageZMQ](https://pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/)
### Part G

### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device



### PROJECT SUMMARY

In this project, our aim was to enhance the AI phone prototype we introduced in Lab 3, transforming it into a more functional version suitable for real-world interactions, such as in a Museum or Maker Lab. Despite having integrated features like speech-to-text, text-to-speech, and speech-to-speech in the previous iteration, the user experience was hindered by the AI voice's sluggish and awkward responses. To address this, we sought out superior APIs and voice assistants, ultimately selecting the [ElevenLabs API](https://elevenlabs.io/speech-synthesis) for its significant impact on the phone's responsiveness.

The final code is in the file lab4_main.py

Understanding this was merely the beginning, we recognized the necessity to clarify user interaction with the prototype. Our enhancements focused on several key areas:

1. Proximity Sensing: We incorporated a proximity sensor to gauge the user's distance from the phone, enabling tailored responses from the Raspberry Pi. For instance, it could alter LED light colors or emit particular sounds, prompting the user to engage with the prototype.
2. Visual Alerts: We installed LED lights on the phone's rear. In conjunction with the proximity sensor, the lights emit a pulsating red signal when the user is distant, creating a sense of urgency and encouraging closer investigation. As the user approaches, the color shifts to a welcoming green, enticing the user to interact further.
3. Aesthetic Design: The phone was outfitted with a 3D-printed case, enhancing its authenticity. This realistic design appeals to users, inviting them to interact as they would with a conventional phone.
4. Audio Guidance: We enriched the audio feedback to provide lucid instructions, ensuring users near the phone understand their subsequent interaction steps.

Through these advancements, we significantly improved its intuitiveness and user-friendliness (our personal main objective for this lab).


## Photos and Videos

Here are a few videos and pictures of our process:

Some initial sketches of how the phone should look, we were thinking that it should stand, so that it would be easier for the user to see:
![WhatsApp Image 2023-10-23 at 6 01 54 PM (1)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/566eebbf-48e7-4259-ade6-1adbc3900396)

Our first basic, cardboard prototype:
![WhatsApp Image 2023-10-23 at 6 01 55 PM (6)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/2dabe6c1-a088-4615-b5ca-65d5508c678d)
![WhatsApp Image 2023-10-23 at 6 01 55 PM (7)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/690e8039-6086-4835-889a-b6288a765da1)

And how it looked with all the parts inside of it (keypad, proximity sensor, LED lights, camera/speaker):
![WhatsApp Image 2023-10-23 at 6 01 54 PM (2)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/48802024-a852-4ed9-87c1-ffd52455206d)
![WhatsApp Image 2023-10-23 at 6 01 54 PM (3)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/617d0851-fe45-4bd9-869a-ebcdb7fb90e8)
![WhatsApp Image 2023-10-23 at 6 01 54 PM (4)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/49e8dc13-84a5-4a39-a7b6-33da8bc5f35a)
![WhatsApp Image 2023-10-23 at 6 01 55 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/fb2db1e7-20d6-4b39-8328-15259076528f)
![WhatsApp Image 2023-10-23 at 6 01 55 PM (1)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/0ded1259-1225-474e-a431-ae8545634612)

The 3D Print Model:
<img width="1149" alt="Screenshot 2023-10-23 at 18 02 39@2x" src="https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/44265fc1-f78a-439a-9c74-6da96cfa9e19">

Starting to print it!
![WhatsApp Image 2023-10-23 at 6 01 55 PM (2)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/b7e51036-d8c3-4366-a089-3371331517d5)

Printed:
![WhatsApp Image 2023-10-23 at 6 01 55 PM (3)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/c77603ef-f58a-42bc-aad5-6a87a0fa8e40)


Connecting everything:
![WhatsApp Image 2023-10-23 at 6 01 55 PM (4)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/c330ae93-be47-40f7-aa72-ef990c59b6d9)

How it looks!
![WhatsApp Image 2023-10-23 at 6 01 55 PM (5)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/256102b7-1b6d-47ce-aef7-f9486998404b)

![WhatsApp Image 2023-10-23 at 7 51 46 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/4e69c47c-0168-4f7f-b6b0-1fc02e5b455d)

![WhatsApp Image 2023-10-23 at 7 51 49 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/cac8eaba-3db8-475c-8c1c-4f32b2a6e5f9)
![WhatsApp Image 2023-10-23 at 8 06 49 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/28adfefb-bdd6-46bc-b032-3d997e38e0a6)
![WhatsApp Image 2023-10-23 at 8 06 51 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/c7f19ff9-b960-430a-bb31-4af9b7a9b01d)
![WhatsApp Image 2023-10-23 at 8 06 51 PM (1)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/7c817fbc-485a-4e74-9cfb-190f5583a61c)
![WhatsApp Image 2023-10-23 at 8 06 53 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/64124fca-c637-49f6-80b2-d9d3ac840932)
![WhatsApp Image 2023-10-23 at 8 06 53 PM (1)](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/dc7e7e2a-3198-4892-b329-063ae0ef287e)
![WhatsApp Image 2023-10-23 at 8 06 54 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/e42199cb-1da2-4937-8f02-53832917ae7e)
![WhatsApp Image 2023-10-23 at 8 06 50 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/cd088538-e65c-4b54-9dab-5fd8d3dc1f66)


We included a space for the cables to go out and have some space so that they wouldn't tip the whole phone over:
![WhatsApp Image 2023-10-23 at 7 59 18 PM](https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/0195e515-3ede-4dbe-8cef-eedb1d081d73)

Here are some videos of it working:


https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/c08520e2-799b-4e41-9e99-b69404dd9903


https://github.com/twallacech95/Interactive-Lab-Hub/assets/11597920/1c3b75a3-2b00-43b4-9092-3966ee3dc1c7


## Looks Like / Works Like / Acts Like

"Looks like":
1. Physical Dimensions: The device likely retains the dimensions of a standard phone, making it familiar and approachable. However, specific details about its size, weight, and balance would depend on the components housed within, especially with the inclusion of new sensors and LEDs.
2. Aesthetic Appeal: With a 3D-printed case, the device not only gains a protective layer but also a customizable aspect. The case can be designed to mimic the appearance of current smartphones or have a unique design, setting it apart as a specialized device.
3. Visual Indicators: The rear of the phone is equipped with LED lights. These aren't just functional but part of the device's aesthetic, providing visual feedback that is integral to the interaction. The lights change colors based on user proximity, acting as a non-verbal form of communication.
4. Overall Feel: The device should feel robust yet inviting, considering its use in public spaces like museums or labs. The weight should be substantial enough to prevent easy theft, but not so heavy that it discourages interaction.

"Works like":
1. Responsive AI: Utilizing the ElevenLabs API, the phone's AI capabilities are more responsive, providing quicker and more natural conversational interactions. This elevates the user's experience from what was previously sluggish and awkward.
2. Proximity Sensing: The phone can now sense how near a user is, thanks to the integrated proximity sensor. This allows for tailored responses, potentially altering its behavior in terms of lighting, sounds, or interaction modes.
3. Visual and Auditory Interactions: The device uses its LED system to attract and guide users, changing colors based on their distance. Furthermore, improved audio feedback provides clear, accessible instructions for users.

"Acts like":
1. Inviting Interaction: The phone actively invites passersby to engage, using visual signals like the pulsating red LED light. It creates a sense of urgency or curiosity, encouraging people to approach.
2. Dynamic Engagement: As a user gets closer, the device's feedback changes in real-time. The visual cues become more welcoming, and the audio guidance clarifies, helping users understand what to do next without confusion.
3. Intuitive Communication: The phone aims to mimic human-like interaction. It doesn't just passively wait for input; it reacts to human presence, potentially initiating the conversation or guiding the interaction flow. This makes it feel less like a tool and more like an interactive guide or assistant.
4. Adaptive Responses: Depending on how users interact or how close they are, the device might offer different prompts or information, providing a personalized experience rather than a one-size-fits-all solution.



## Our errors

Since @Hauke asked for our documentation to help others in the future (and maybe get some extra points hehehe, we spent most of the time in this whole project just doing this) here it goes, a rundown of our problems:

During our development, a key important thing to address was our beloved Qwicc Keypad, with which we had countless connection issues. The issues were mainly categorized into either of these two:
1. Connection IO Error: This was mainly fixed by giving either a bigger timer for sleep between functions/calls or for us, using instead eventlet. Eventlet is a concurrent networking library for Python, which in simple terms allows you to run multiple functions without I/O errors.
2. Keypad just not connecting:
The main problem here was that the KeyPad's IC2 address was being re-written (we weren't able to find the source of why this was happening, I hypothesise that it might be because of a library or the eventlet library and calls that are being done, it is coming however from the .update_fifo function, more importantly however is that we did find the solution).

To Fix n2:
1. In your terminal, run <sudo i2cdetect -y 1>. This will give you a matrix where you will be able to find the new address that your Raspberry Pi gave to your Qwicc Keypad. e.g. 10 or 52
2. Change <myKeypad = qwiic_keypad.QwiicKeypad()> in your python script to <myKeypad = qwiic_keypad.QwiicKeypad(address=0x{your address})> e.g. <myKeypad = qwiic_keypad.QwiicKeypad(address=0x10)>
3. Run your script once. This could change the address back to the original one "4b"
4. If 3 happens, then change back <myKeypad = qwiic_keypad.QwiicKeypad(address=0x{your address})> to <myKeypad = qwiic_keypad.QwiicKeypad()>

Source of information on how Qwicc Keypad works [here](https://github.com/sparkfun/Qwiic_Keypad_Py/blob/main/qwiic_keypad.py#L94) 