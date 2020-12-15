# coding=utf-8
import json
import asyncio
import websockets
from flask import Flask, jsonify, render_template, request
from LSTM_New import predict_csv
from json2 import csv_to_json


async def recv_msg(websocket):
    while True:
        data = await websocket.recv()
        #print(data)
        #predict_csv(data, 7)
        #csv_to_json(data)
        if data=='2':
            await websocket.send('2')
            continue

        # filename = data + '.txt'  # 此处为文件名
        filename = data + '.json'
        directory = 'prediction/'  # 此处为文件路径

        message = 'error'  # 该变量为最终发送信息

        try:
                # f = open('shanghai.txt', mode='r')
                f = open(directory + filename, mode='r')
                strs = f.readlines()
                print(strs)
                f.close()
                for txt in strs:
                    print(txt)
                    await websocket.send(txt)

        except:
            message = 'NO_EXISTENCE'


# 服务器端主逻辑
async def main_logic(websocket, path):
    # await check_permit(websocket)

    await recv_msg(websocket)


if __name__ == '__main__':
    DATA = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
    for data in DATA:
        predict_csv(data, 7)
        csv_to_json(data)
    start_server = websockets.serve(main_logic, '127.0.0.1', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
