#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:34:30 2024

@author: ivan
"""

import requests
url = 'https://pokeapi.co/api/v2/pokemon?limit=150'
request = requests.get(url)
listaPokemon = request.json()["results"]
for pokemon in listaPokemon:
    print(pokemon["name"])