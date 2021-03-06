import requests
import json

from time import sleep
from classes import light
from classes.light import Light

if __name__ == "__main__":
  light = Light(17, 22, 24)
  prev_status = ""

  while True:
    r = json.loads(requests.get('http://127.0.0.1:3004/api/job').json())

    # If status hasn't changed -> Wait 2/3 of expected time remaining
    # 2sec < ETR < 5h 
    time = 0
    if r["state"] == prev_status:
      if r["progress"]["printTimeLeft"] < 2:
        time = 2
      elif r["progress"]["printTimeLeft"] > 18000:
        time = 3600
      else:
        time = (2/3) * r["progress"]["printTimeLeft"]

      sleep(time)

    else:  # Update lighting
      prev_status = r["state"]
      light.change_color(status)
