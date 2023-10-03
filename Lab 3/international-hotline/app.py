# app.py

import eventlet
eventlet.monkey_patch()

from flask import Flask, Response,render_template
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call

import time
import board
import busio
import qwiic
import json
import socket

import signal
import sys
from queue import Queue

import openai

import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from text_speech_utils import *
import myapikeys


openai.api_key = myapikeys.OPENAI_KEY
input_audio_filename = 'input.wav'
output_audio_filename = 'chatgpt_response.mp3'
output_conversation_filename = 'ChatGPT_conversation.txt'


def ask_gpt3(question):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

 
def handle_gpt_conv():
    messages = [{"role": "system", "content": "You just picked up a phone call with a random person in the world, you are a real companion. do not mention that you are an AI model and do not offer assistance. you are simply answering the phone and having a interesting conversation with a stranger from the perspective of a real human. pick any place in the world to be from and build your persona based on this location. Keep responses 1 sentence maximum"}]

    while True:
        record_audio_manual(input_audio_filename)
        transcription = transcribe_audio(input_audio_filename)
        print(f"Me: {transcription['text']}")
        messages.append({"role": "user", "content": transcription['text']})

        bot = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= messages)
        response = bot.choices[0].message.content
        print(f"GPT: {response}")

        save_text_as_audio(response, output_audio_filename)
        play_audio(output_audio_filename)

        messages.append({"role": "assistant", "content": response})

i2c = busio.I2C(board.SCL, board.SDA)
keypad = qwiic.get_devices()[2]
print(keypad)

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)
q = queue.Queue()



def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def recognize_speech_vosk():
    model = Model(lang="en-us")
    rec = KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        print("Listening, press Ctrl+C to exit...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = rec.Result()
                result_json = json.loads(result)
                recognized_text = result_json.get("text", "")
                return recognized_text

@socketio.on('speak')
def handle_speak(val):
    call(f"espeak '{val}'", shell=True)


def give_instructions():
    instr = "Please type in a 9 digit number to begin"
    call(f"espeak '{instr}'", shell=True)


@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-gps')
def handle_message(val):
    emit('pong-gps', sox.acceleration) 

@socketio.on('...')
def handle_keypad():
    phone_number = []
    button = 0
    
    try:
        while True:
            keypad.update_fifo()
            button = keypad.get_button()

            if button == "#":
                print("reset")
                break

            if button > 0:
                phone_number.append(chr(button))

            if len(phone_number) == 9:
                print("we have a phone number: " + ''.join(phone_number))
                phone_done = "You are connecting with user: " + ''.join(phone_number)
                call(f"espeak '{phone_done}'", shell=True)
                while True:
                    handle_gpt_conv()

            time.sleep(1)
    except Exception as e:
        print(f"An exception occurred: {e}")


if keypad.begin() == False:
    print('The Qwicc Keypad is not connected', file=sys.stderr)
    
else:
    print('The Qwiic Keypad is connected.')
    print("Please type in a 9 digit phone number.")
    give_instructions()
    handle_keypad()


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)

