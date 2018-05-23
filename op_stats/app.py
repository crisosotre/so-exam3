from flask import Flask
import json
import sys
sys.path.append('/home/operativos/so-exam3')
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/CPU')
def informacion_cpu():
    return json.dumps({'Porcentaje CPU': Stats.porcentaje_cpu()})

@app.route('/RAM')
def informacion_memoria():
    return json.dumps({'Memoria Disponible': Stats.ram_disponible()})

@app.route('/DISCO')
def informacion_disco():
    return json.dumps({'Espacio Libre Disco': Stats.espacio_disco_disponible()})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

