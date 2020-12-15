import asyncio
import websockets


async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        str = 'null'
        while True:
            while True:
                file = open('E:/PythonProject/web/resource/city.txt', mode='r')
                # file.seek(0)
                str1 = file.readline()
                if str1 == "":
                    continue
                print(str + '     ' + str1)
                # print(str1)
                file.close()
                if str1 != str:
                    str = str1
                    print(str)
                    break
            await websocket.send(str)

            strss = ''
            greeting = await websocket.recv()

            while greeting != 'END\n':
                strss += greeting
                greeting = await websocket.recv()

            file = open('E:/PythonProject/web/resource/data.txt', mode='w')
            print(strss)
            # file.seek(0)
            file.write(strss)
            file.close()


asyncio.get_event_loop().run_until_complete(hello())
