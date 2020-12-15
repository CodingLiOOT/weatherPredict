
#coding=utf-8
import json
from flask import Flask, jsonify, render_template, request

from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket


app = Flask(__name__)

@app.route("/socket")
def socket():
    user_socket = request.environ.get("wsgi.websocket")
    print(request)
    print(user_socket)

    while True:
        data = user_socket.receive()
        print(data)

        filename = data+'.json' #此处为文件名
        directory = 'data/' #此处为文件路径

        message = 'error' #该变量为最终发送信息

        try:
            with open(directory+filename) as f:
                message = json.load(f)
        except:
            message = 'NO_EXISTENCE'

        try:
            user_socket.send(message)
        except:
            continue



#def read_json():
#       json_name = 'data'
#       filename = json_name + '.json'
#       directory = "E://spark//bin"  # json文件所在的目录路径
#       try:
#           with open(directory + '/' + filename) as f:
#               jsonStr = json.load(f)
#               return json.dumps(jsonStr)
#
#       except Exception as e:
 #          return jsonify({"code": "异常", "message": "{}".format(e)})



if __name__ == '__main__':
    http_serv = WSGIServer(('127.0.0.1',8000), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()
