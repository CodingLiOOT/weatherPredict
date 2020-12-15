import asyncio
import websockets
import os

resource_dir = os.path.dirname(os.path.abspath(__file__))

async def transport():
    async with websockets.connect('ws://localhost:8765') as websocket:
        str = 'null'
        while True:
            while True:
                #file = open('E:/PythonProject/web/resource/city.txt', mode='r')
                global resource_dir
                file = open(resource_dir+"/resource/city.CFG",mode='r')
                # file.seek(0)
                str1 = file.readline()
                file.close()
                if str1 == "":
                    continue
                #print(str + '     ' + str1)
                # print(str1)

                if str1 != str:
                    str = str1
                    print(str)
                    #break
                    await websocket.send(str)
                    break
                else:
                    await websocket.send('2')
                    break

            strss = ''
            greeting = await websocket.recv()
            if greeting=='2':
                continue
            while greeting != 'END\n':
                strss += greeting
                greeting = await websocket.recv()

            #file = open('E:/PythonProject/web/resource/data.txt', mode='w')

            file = open(resource_dir+'/resource/data.json',mode='w')
            print(strss)
            # file.seek(0)
            file.write(strss)
            file.close()


asyncio.get_event_loop().run_until_complete(transport())
