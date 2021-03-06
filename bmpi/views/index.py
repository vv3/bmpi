from flask import Blueprint, render_template, request
from flask import current_app as app
#from flask import g


index_bp = Blueprint('index', __name__)

def sendCommand(data_stream):

    if data_stream == "ui.txt":
        app.wifi_srv.sendToSerial(b'AT+RSI_READ\x01\x27\x00GET /ui.txt HTTP/1.1 Host: 172.16.20.48\r\n')
    if data_stream == "recipe":
        app.wifi_srv.sendToSerial(b'AT+RSI_READ\x01\x27\x00GET /rz.txt HTTP/1.1 Host: 172.16.20.48\r\n')
    if data_stream == "bm.txt":
        app.wifi_srv.sendToSerial(b'AT+RSI_READ\x01\x27\x00GET /bm.txt HTTP/1.1 Host: 172.16.20.48\r\n')
    if data_stream == "key1":
        app.wifi_srv.sendToSerial(b'AT+RSI_READ\x01\x27\x00GET /bm.txt?k=1 HTTP/1.1 Host: 172.16.20.48\r\n')
    if data_stream == "key2":
        app.wifi_srv.sendToSerial(b'AT+RSI_READ\x01\x27\x00GET /bm.txt?k=2 HTTP/1.1 Host: 172.16.20.48\r\n')
    if data_stream == "key3":
        app.wifi_srv.sendToSerial(b'AT+RSI_READ\x01\x27\x00GET /bm.txt?k=3 HTTP/1.1 Host: 172.16.20.48\r\n')
    if data_stream == "key4":
        app.wifi_srv.sendToSerial(b'AT+RSI_READ\x01\x27\x00GET /bm.txt?k=4 HTTP/1.1 Host: 172.16.20.48\r\n')


def remove_null_bytes(b_data):
    return b_data.decode().replace('\x00', '')

@index_bp.route('/', methods=['GET', 'POST'])
@index_bp.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'David'}
    #if form.validate_on_submit():
    if request.method == 'POST':
        if 'recipe' in request.form:
            sendCommand("recipe")
            return render_template('index.html', title='Home', user=user)
        if 'bm.txt' in request.form:
            sendCommand("bm.txt")
            return render_template('index.html', title='Home', user=user)
        if 'ui.txt' in request.form:
            sendCommand("ui.txt")
            return render_template('index.html', title='Home', user=user)
        if 'key1' in request.form:
            sendCommand("key1")
            return render_template('index.html', title='Home', user=user)
        if 'key2' in request.form:
            sendCommand("key2")
            return render_template('index.html', title='Home', user=user)
        if 'key3' in request.form:
            sendCommand("key3")
            return render_template('index.html', title='Home', user=user)
        if 'key4' in request.form:
            sendCommand("key4")
            return render_template('index.html', title='Home', user=user)
        else:
            return render_template('index.html', title='Home', user=user)
    elif request.method == 'GET':
            return render_template('index.html', title='Home', user=user)