import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime
from render_image import create_display_image
import math

import p5
from p5 import *

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Make sure to create an image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

tree_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
progress_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))


# Get drawing object to draw on image.
# draw = ImageDraw.Draw(image)


# Get drawing objects for each layer
tree_draw = ImageDraw.Draw(tree_layer)
progress_draw = ImageDraw.Draw(progress_layer)

# Define fonts and colors
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 23)
text_color = (255, 255, 255)
shadow_color = (192, 192, 192)

# Define the positions and dimensions of the progress bars.
# position with labels
# minute_bar_x = 50
# position without labels
minute_bar_x = 30
minute_bar_y = 20
minute_bar_width = 100
minute_bar_height = 10

# position with labels
#hour_bar_x = 50
# position without labels
hour_bar_x = 30
hour_bar_y = 50
hour_bar_width = 100
hour_bar_height = 10

# Define the shadow container for minute progress bar.
minute_shadow_x = minute_bar_x - 3
minute_shadow_y = minute_bar_y - 3
minute_shadow_width = 178
minute_shadow_height = 17

# Define the shadow container for hour progress bar.
hour_shadow_x = hour_bar_x - 3
hour_shadow_y = hour_bar_y - 3
hour_shadow_width = 178
hour_shadow_height = 17

# Define the positions and dimensions for the new progress bar (Seconds to Minutes).
seconds_to_minutes_bar_x = 30
seconds_to_minutes_bar_y = 80
seconds_to_minutes_bar_width = 100
seconds_to_minutes_bar_height = 10

# Define colors for the progress bars and shadows (in RGB format).
minute_bar_color = (253, 201, 33)  # Light green
seconds_to_minutes_bar_color = (0, 165, 207)  # Light green
hour_bar_color = (153, 226, 180)    # Light blue
shadow_color = (226, 253, 255, 1)      # Light gray

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


# Get drawing objects for each layer
tree_draw = ImageDraw.Draw(tree_layer)
progress_draw = ImageDraw.Draw(progress_layer)

def draw_tree(x1, y1, angle, length, width, draw):
    if length < 10:
        return
    # Calculate the end point for the line segment to be drawn
    x2 = x1 + length * math.cos(math.radians(angle))
    y2 = y1 - length * math.sin(math.radians(angle))
    
    draw.line(xy=(x1, y1, x2, y2), fill=(255, 255, 255, 128), width=width)
    
    # Calculate new width, angle and length
    new_width = max(1, width - 1)
    new_angle = 20  # The angle between branches
    new_length = length * 0.85  # Reduce the length for the next branches
    
    # Draw the two new branches
    draw_tree(x2, y2, angle - new_angle, new_length, new_width, draw)
    draw_tree(x2, y2, angle + new_angle, new_length, new_width, draw)

# Start drawing from the bottom center
x, y = 0, 67.5
angle = 0  # Pointing upwards
length = 45  # Length of the initial line
treeWidth = 7  # Width of the line

draw_tree(x, y, angle, length, treeWidth, tree_draw)
tree_draw.ellipse((-10, 32, 10, 100), fill=(150, 75, 0), outline=0)


while True:
    # Clear the screen
    progress_draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Get the current time
    current_time = strftime("%H:%M:%S")
    current_hour, current_minute, current_second = map(int, current_time.split(":"))

    # Calculate the progress for each time unit
    minute_progress = current_minute / 60.0
    hour_progress = (current_hour % 24) / 24.0
    seconds_to_minutes_progress = current_second / 60.0

    progress_draw.ellipse(
        (0, 0, width * hour_progress, height),
        outline=0,
        fill=(0, 255, 0)  # hours
    )
    progress_draw.ellipse(
        (0, 0, width * minute_progress, height),
        outline=0,
        fill=(200, 40, 0)  # minutes
    )
    progress_draw.rectangle(
        (width * seconds_to_minutes_progress - 14, 0, width * seconds_to_minutes_progress+4, height),
        outline=0,
        fill=(255, 255, 255)  # seconds
    )
    progress_draw.rectangle(
        (width * seconds_to_minutes_progress - 10, 0, width * seconds_to_minutes_progress, height),
        outline=0,
        fill=(0, 0, 255)  # seconds
    )
   
    # Mask progress bars using the tree alpha channel and paste onto the main image
    image.paste(progress_layer, (0, 0), mask=tree_layer.split()[3])

    # Paste the tree layer onto the main image
    image.paste(tree_layer, (0, 0), tree_layer)
    
     # Display image.
    disp.image(image, rotation)
    time.sleep(1)






## progress bar functions 

 # Calculate the width of the bars based on progress.
    # minute_bar_width = int((width - minute_bar_x - 20) * minute_progress)
    # hour_bar_width = int((width - hour_bar_x - 20) * hour_progress)
    # seconds_to_minutes_bar_width = int((width - seconds_to_minutes_bar_x - 20) * seconds_to_minutes_progress)


  # Draw labels for the progress bars.
    # draw.text((minute_bar_x - 43, minute_bar_y - 13), "m", fill=(255, 255, 255), font=font, rotate=270)
    # draw.text((hour_bar_x - 43, hour_bar_y - 13), "hr", fill=(255, 255, 255), font=font, rotate=90)
    # draw.text((seconds_to_minutes_bar_x - 43, seconds_to_minutes_bar_y - 13), "sec", fill=(255, 255, 255), font=font)
    
    # Draw the shadow container for the minute progress bar.

#  draw.rectangle(
#         (minute_shadow_x, minute_shadow_y, minute_shadow_x + minute_shadow_width, minute_shadow_y + minute_shadow_height),
#         outline=0,
#         fill=shadow_color,
#     )

#     # Draw the shadow container for the hour progress bar.
#     draw.rectangle(
#         (hour_shadow_x, hour_shadow_y, hour_shadow_x + hour_shadow_width, hour_shadow_y + hour_shadow_height),
#         outline=0,
#         fill=shadow_color,
#     )

#     # Draw the rectangles for the progress bars.
#     draw.rectangle(
#         (minute_bar_x, minute_bar_y, minute_bar_x + minute_bar_width, minute_bar_y + minute_bar_height),
#         outline=0,
#         fill=minute_bar_color,
#     )

#     draw.rectangle(
#         (hour_bar_x, hour_bar_y, hour_bar_x + hour_bar_width, hour_bar_y + hour_bar_height),
#         outline=0,
#         fill=hour_bar_color,
#     )

#     draw.rectangle(
#         (seconds_to_minutes_bar_x, seconds_to_minutes_bar_y, seconds_to_minutes_bar_x + seconds_to_minutes_bar_width,
#          seconds_to_minutes_bar_y + seconds_to_minutes_bar_height),
#         outline=0,
#         fill=seconds_to_minutes_bar_color,  # Define this color as you like
#     )