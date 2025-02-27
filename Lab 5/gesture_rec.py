# Copyright 2023 The MediaPipe Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# """Main scripts to run gesture recognition."""
import argparse
import sys
import os
import time
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
# Global variables to calculate FPS
COUNTER, FPS = 0, 0
START_TIME = time.time()
image_file_name = "frame.jpg"
import replicate
import myapikeys_lab5


os.environ["REPLICATE_API_TOKEN"] = myapikeys_lab5.REPLICATE_API_TOKEN

def run(model: str, num_hands: int,
        min_hand_detection_confidence: float,
        min_hand_presence_confidence: float, min_tracking_confidence: float,
        camera_id: int, width: int, height: int) -> None:
#  """Continuously run inference on images acquired from the camera.
#   Args:
#       model: Name of the gesture recognition model bundle.
#       num_hands: Max number of hands can be detected by the recognizer.
#       min_hand_detection_confidence: The minimum confidence score for hand
#         detection to be considered successful.
#       min_hand_presence_confidence: The minimum confidence score of hand
#         presence score in the hand landmark detection.
#       min_tracking_confidence: The minimum confidence score for the hand
#         tracking to be considered successful.
#       camera_id: The camera id to be passed to OpenCV.
#       width: The width of the frame captured from the camera.
#       height: The height of the frame captured from the camera.
#   """

  # Start capturing video input from the camera
  cap = cv2.VideoCapture(camera_id)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

  # Visualization parameters
  row_size = 50  # pixels
  left_margin = 24  # pixels
  text_color = (0, 0, 0)  # black
  font_size = 1
  font_thickness = 1
  fps_avg_frame_count = 10

  # Label box parameters
  label_text_color = (0, 0, 0)  # red
  label_background_color = (255, 255, 255)  # white
  label_font_size = 1
  label_thickness = 2
  label_padding_width = 100  # pixels

  recognition_frame = None
  recognition_result_list = []

  def save_result(result: vision.GestureRecognizerResult,
                  unused_output_image: mp.Image, timestamp_ms: int):
      global FPS, COUNTER, START_TIME

      # Calculate the FPS
      if COUNTER % fps_avg_frame_count == 0:
          FPS = fps_avg_frame_count / (time.time() - START_TIME)
          START_TIME = time.time()

      recognition_result_list.append(result)
      COUNTER += 1

  # Initialize the gesture recognizer model
  base_options = python.BaseOptions(model_asset_path=model)
  options = vision.GestureRecognizerOptions(base_options=base_options,
                                          running_mode=vision.RunningMode.LIVE_STREAM,
                                          num_hands=num_hands,
                                          min_hand_detection_confidence=min_hand_detection_confidence,
                                          min_hand_presence_confidence=min_hand_presence_confidence,
                                          min_tracking_confidence=min_tracking_confidence,
                                          result_callback=save_result)
  recognizer = vision.GestureRecognizer.create_from_options(options)
  counter = 0
  # Continuously capture images from the camera and run inference
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      sys.exit(
          'ERROR: Unable to read from webcam. Please verify your webcam settings.'
      )

    image = cv2.flip(image, 1)

    # Convert the image from BGR to RGB as required by the TFLite model.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

    # Run gesture recognizer using the model.
    recognizer.recognize_async(mp_image, time.time_ns() // 1_000_000)

    # Show the FPS
    fps_text = 'FPS = {:.1f}'.format(FPS)
    text_location = (left_margin, row_size)
    current_frame = image

    # Expand the frame to show the labels.
    current_frame = cv2.copyMakeBorder(current_frame, 0, label_padding_width,
                                       0, 0,
                                       cv2.BORDER_CONSTANT, None,
                                       label_background_color)

    if recognition_result_list:
      # Show top gesture classification.
      gestures = recognition_result_list[0].gestures

      if gestures:
        print(gestures)
        category_name = gestures[0][0].category_name
        score = round(gestures[0][0].score, 2)
        result_text = category_name + ' (' + str(score) + ')'
        if category_name == "Thumb_Up" and score >= 0.6:
          if counter > 5:
            cv2.imwrite(image_file_name, image)
            with open(image_file_name, "rb") as imager:
                output = replicate.run( 
                    "daanelson/plug_and_play_image_translation:ae10351e6de912fa681854e472bb7aff011411f2c3802b2ccd836a2a22408069",
                    input={
                        "input_image": imager,
                        "translation_prompts": "a photo of a spooky haloween face"
                        }
                    )
                print(output)
                break
          print("THUMBS UP DETECTED")
          counter += 1
          print("Counter: ", counter)
        
        else:
          counter = 0
        # Compute text size
        text_size = \
        cv2.getTextSize(result_text, cv2.FONT_HERSHEY_DUPLEX, label_font_size,
                        label_thickness)[0]
        text_width, text_height = text_size

        # Compute centered x, y coordinates
        legend_x = (current_frame.shape[1] - text_width) // 2
        legend_y = current_frame.shape[0] - (
                    label_padding_width - text_height) // 2

        # Draw the text
        cv2.putText(current_frame, result_text, (legend_x, legend_y),
                    cv2.FONT_HERSHEY_DUPLEX, label_font_size,
                    label_text_color, label_thickness, cv2.LINE_AA)

      recognition_frame = current_frame
      recognition_result_list.clear()

    if recognition_frame is not None:
        cv2.imshow('gesture_recognition', recognition_frame)

    # Stop the program if the ESC key is pressed.
    if cv2.waitKey(1) == 27:
        break

  recognizer.close()
  cap.release()
  cv2.destroyAllWindows()


def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Name of gesture recognition model.',
      required=False,
      default='gesture_recognizer.task')
  parser.add_argument(
      '--numHands',
      help='Max number of hands that can be detected by the recognizer.',
      required=False,
      default=1)
  parser.add_argument(
      '--minHandDetectionConfidence',
      help='The minimum confidence score for hand detection to be considered '
           'successful.',
      required=False,
      default=0.5)
  parser.add_argument(
      '--minHandPresenceConfidence',
      help='The minimum confidence score of hand presence score in the hand '
           'landmark detection.',
      required=False,
      default=0.5)
  parser.add_argument(
      '--minTrackingConfidence',
      help='The minimum confidence score for the hand tracking to be '
           'considered successful.',
      required=False,
      default=0.5)
  # Finding the camera ID can be very reliant on platform-dependent methods. 
  # One common approach is to use the fact that camera IDs are usually indexed sequentially by the OS, starting from 0. 
  # Here, we use OpenCV and create a VideoCapture object for each potential ID with 'cap = cv2.VideoCapture(i)'.
  # If 'cap' is None or not 'cap.isOpened()', it indicates the camera ID is not available.
  parser.add_argument(
      '--cameraId', help='Id of camera.', required=False, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      default=640)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      default=480)
  args = parser.parse_args()

  run(args.model, int(args.numHands), args.minHandDetectionConfidence,
      args.minHandPresenceConfidence, args.minTrackingConfidence,
      int(args.cameraId), args.frameWidth, args.frameHeight)


if __name__ == '__main__':
  main()