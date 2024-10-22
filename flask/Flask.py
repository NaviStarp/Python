#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:16:12 2024

@author: ivan
"""

from flask import Flask,jsonify

app = Flask(__name__)

#Lista 1
@app.route('/api/lista1',methods=['GET'] )
def obtenerLista1():
    datos={
        "nombre":"Sebastian",
        "Edad":19,
        "Residencia": "Seseña"
           
           
           }
    return jsonify(datos)
#Lista 2
@app.route('/api/lista2', methods = ['GET'])
def obtenerLista2():
    datos=[{"nombre":"Sebastian","Edad":19, "Residencia": "Seseña" }
    ,{"nombre":"Sebastian","Edad":19, "Residencia": "Seseña" }
    ,{"nombre":"Sebastian","Edad":19, "Residencia": "Seseña" }
    ,{"nombre":"Sebastian","Edad":19, "Residencia": "Seseña" }]
    return jsonify(datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
