import json
import random
import time
import os
import func
from func import *

import setup
from setup import *

def pickRandomExpressionFile():
    # Your numeric eyeball expressions go here!
    list = [
        "blush_flowers.exp3.json",
        "sadtears.exp3.json",
    ]
    return random.choice(list)

async def main():
    # Connect to VTube Studio
    try:
        websocket = await websockets.connect('ws://127.0.0.1:8001')
    except:
        print("Couldn't connect to vtube studio")
        input("press enter to quit program")
        quit()
    await setup(websocket)

    # In your voice detection code, set this to False to interrupt the random cycling
    cycleRandomly = True

    # Main Program Loop
    while True:
        if cycleRandomly:
            chosenExpression = pickRandomExpressionFile()
            await func.setexstate(websocket, chosenExpression, True)
            time.sleep(1)
            await func.setexstate(websocket, chosenExpression, False)
            time.sleep(1)

# Run the loop with awaits
asyncio.run(main())