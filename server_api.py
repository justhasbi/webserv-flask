from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/api/test', methods=['POST'])
def test():
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    cv2.imwrite('coba.png', img)
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")