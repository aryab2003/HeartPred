# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model=pickle.load(open('C:/Users/HP/Downloads/trained_model.sav','rb'))

input_data = (57, 0, 0, 120, 354, 0, 1, 163, 1, 0.6, 2, 0, 2)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print('Person does not have heart disease')
else:
  print('Person has heart disease')