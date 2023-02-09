import socketio

sio = socketio.Client()


def emit_server(task, place, content):
    data = {
        "task": task,
        "place": place,
        "content": content
    }
    sio.emit("server_client_local", data)


@sio.event
def message_client_local(data):
    if (data["task"] == "TexttoController"):
        if (data["content"] != None):
            text = data["content"]
            print('message received with ', data, text)
            emit_server("TextoControllerWeb", "page_home", text)


@sio.event
def connect():
    print('connection')
    emit_server("Notification", "none", "connect to server")


@sio.event
def disconnect():
    print('disconnection')
    emit_server("Notification", "none", "disconnect to server")


sio.connect('http://192.168.1.63:6868/', wait_timeout=10)
sio.wait()
