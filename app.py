import math
from flask import Flask

app = Flask(__name__)

def BlackBoxFunction(x):
    return abs(math.sin(x))

def NumericalIntegration(lower, upper, N):
    integral = 0
    lower = float(lower)
    upper = float(upper)
    dx = (upper-lower)/N
    for i in range(N):
        xip12 = lower+(i+1/2)*dx
        dI = BlackBoxFunction(xip12)*dx
        integral += dI
    return integral


@app.route('/numericalintegralservice/<lower>/<upper>', methods=['GET'])
def get_numerical_integration(lower, upper):
    N = [10, 100, 1000, 10**4, 10**5, 10**6, 10**7]
    output = {'message':[]}
    for n in N:
        output["message"].append(NumericalIntegration(lower, upper, n))
    status_code = 200
    return output, status_code