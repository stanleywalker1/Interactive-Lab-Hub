import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime
from render_image import create_display_image

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

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)

# Define fonts and colors
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 23)
text_color = (255, 255, 255)
shadow_color = (192, 192, 192)

# Define the positions and dimensions of the progress bars.
minute_bar_x = 50
minute_bar_y = 20
minute_bar_width = 100
minute_bar_height = 10

hour_bar_x = 50
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
seconds_to_minutes_bar_x = 50
seconds_to_minutes_bar_y = 80
seconds_to_minutes_bar_width = 100
seconds_to_minutes_bar_height = 10

# Define colors for the progress bars and shadows (in RGB format).
minute_bar_color = (253, 201, 33)  # Light green
seconds_to_minutes_bar_color = (0, 165, 207)  # Light green
hour_bar_color = (153, 226, 180)    # Light blue
shadow_color = (226, 253, 255, 1)      # Light gray


# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Get the current time in hours, minutes, and seconds.
    current_time = strftime("%H:%M:%S")
    current_hour, current_minute, current_second = map(int, current_time.split(":"))

    # Calculate the progress for the minute and hour bars.
    minute_progress = current_minute / 60.0
    hour_progress = (current_hour % 24) / 24.0
    seconds_to_minutes_progress = current_second / 60.0

    # Calculate the width of the bars based on progress.
    minute_bar_width = int((width - minute_bar_x - 20) * minute_progress)
    hour_bar_width = int((width - hour_bar_x - 20) * hour_progress)
    seconds_to_minutes_bar_width = int((width - seconds_to_minutes_bar_x - 20) * seconds_to_minutes_progress)

     # Draw labels for the progress bars.
    draw.text((minute_bar_x - 43, minute_bar_y - 13), "m", fill=(255, 255, 255), font=font, rotate=270)
    draw.text((hour_bar_x - 43, hour_bar_y - 13), "hr", fill=(255, 255, 255), font=font, rotate=90)
    draw.text((seconds_to_minutes_bar_x - 43, seconds_to_minutes_bar_y - 13), "sec", fill=(255, 255, 255), font=font)
    
    # Draw the shadow container for the minute progress bar.
    draw.rectangle(
        (minute_shadow_x, minute_shadow_y, minute_shadow_x + minute_shadow_width, minute_shadow_y + minute_shadow_height),
        outline=0,
        fill=shadow_color,
    )

    # Draw the shadow container for the hour progress bar.
    draw.rectangle(
        (hour_shadow_x, hour_shadow_y, hour_shadow_x + hour_shadow_width, hour_shadow_y + hour_shadow_height),
        outline=0,
        fill=shadow_color,
    )

    # Draw the rectangles for the progress bars.
    draw.rectangle(
        (minute_bar_x, minute_bar_y, minute_bar_x + minute_bar_width, minute_bar_y + minute_bar_height),
        outline=0,
        fill=minute_bar_color,
    )

    draw.rectangle(
        (hour_bar_x, hour_bar_y, hour_bar_x + hour_bar_width, hour_bar_y + hour_bar_height),
        outline=0,
        fill=hour_bar_color,
    )

    draw.rectangle(
        (seconds_to_minutes_bar_x, seconds_to_minutes_bar_y, seconds_to_minutes_bar_x + seconds_to_minutes_bar_width,
         seconds_to_minutes_bar_y + seconds_to_minutes_bar_height),
        outline=0,
        fill=seconds_to_minutes_bar_color,  # Define this color as you like
    )

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
