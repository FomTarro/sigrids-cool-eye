import os
import json
import configparser

import asyncio
import websockets

import func
from func import *

import pytchat
from pytchat import *
import webbrowser
async def setup(websocket):
    if os.path.exists('token.json'):
        print('Loading authtoken From File...')
        with open('token.json', "r") as json_file:
            data = json.load(json_file)
            authtoken = (data['authenticationkey'])
            confirm = await authen(websocket,authtoken)
            if authtoken == "" or confirm["data"]["authenticated"] == False:
                print('Error Token Invalid')
                print('Fetching New Tokens...')
                authtoken = await token(websocket)
                print(authtoken)
                print('Saving authtoken for Future Use...')
                data["authenticationkey"] = authtoken
                json_file.close()
                json_file = open('token.json', "w")
                json_file.write(json.dumps(data))
                json_file.close()
                print("Saving finished")
            else:
                json_file.close()
    else:
            print('Fetching New Tokens...')
            authtoken = await token(websocket)
            print(authtoken)
            print('Saving authtoken for Future Use...')
            with open('token.json', "w") as json_file:
                jsonfilecon = {
                            "chatspeed": 0.1,
                            "authenticationkey": authtoken,
                            "authenticationkeytwitch": ""
                        }
                json_file.write(json.dumps(jsonfilecon))
                json_file.close()
            await authen(websocket,authtoken)
    if os.path.exists('commands.ini'):
        config = configparser.ConfigParser()
        commandlist = config.read('commands.ini')
    else:
        config = configparser.ConfigParser()
        with open('commands.ini', "w") as configfile:
            config['COMMANDS'] = {
                    "!spin": "spin(websocket,x,y,s)",
                    "!reset": "mdmv(websocket,0.2,False,0,0,0,-76)",
                    "!rainbow": "rainbow(websocket)"
                }
            config.write(configfile)
    with open('token.json') as json_file:
        data = json.load(json_file)
        json_file.close()
        
    print("Successfully Loaded")
    # print("Detected Commands")
    # for key in config['COMMANDS']:
    #     print(key)
    return config