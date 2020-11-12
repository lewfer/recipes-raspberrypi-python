import time
from subprocess import call

call(["fswebcam", "-d", "/dev/video0", "-r", "1280x720", "--no-banner", "./image.jpg"])

