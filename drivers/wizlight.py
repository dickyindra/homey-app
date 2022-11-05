import sys, getopt
import asyncio

from pywizlight import wizlight, PilotBuilder
from PIL import ImageColor

ip = "192.168.18.16"

async def turn_on():
    light = wizlight(ip)
    await light.turn_on()

async def turn_off():
    light = wizlight(ip)
    await light.turn_off()

async def set_color(color: str):
    light = wizlight(ip)
    await light.turn_on(PilotBuilder(rgb = ImageColor.getrgb(color)))

async def set_brightness(brightness: int):
    light = wizlight(ip)
    await light.turn_on(PilotBuilder(brightness = brightness))

def main():
    opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "ip=", "on", "off", "white", "color=", "brightness=", "temperature="])

    for opt, arg in opts:
        if (opt in ("-h", "--help")):
            print("Usage: wizlight.py --ip <ip> --on | --off | --white | --color <color> | --brightness <brightness> | --temperature <temperature>")
            sys.exit(0)
        elif (opt == "--ip"):
            ip = arg
        elif (opt == "--on"):
            asyncio.run(turn_on())
        elif (opt == "--off"):
            asyncio.run(turn_off())
        elif (opt == "--color"):
            asyncio.run(set_color(arg))
        elif (opt == "--brightness"):
            brightness = int(arg)
            asyncio.run(set_brightness(brightness))

main()
