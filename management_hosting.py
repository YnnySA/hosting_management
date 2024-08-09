# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:49:55 2024

@author: Yenny SA
"""

import pandas as pd
import numpy as np

df = pd.read_excel("Listado_de_Inventario.xlsx")

print(df.info())

print(df[["COD_LOTE","IMPORTE"]])

