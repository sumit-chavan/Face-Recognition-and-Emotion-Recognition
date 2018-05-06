# Rahul Barhate - 2/3/2018

import keras
import numpy as np
import sys
import subprocess

##guif_values = subprocess.check_output([sys.executable, "guif.py"])
##print(guif_values)


data_in = np.array([[0,0], [0,1], [1,0], [1,1]])
#print(data_in)

logic_and = np.array([[0], [0], [0], [1]])
#print(logic_and)

#Available options - Dense, Deconv2D, Deconvolution2D
model = keras.models.Sequential(layers=[ keras.layers.Dense(input_dim=2, units=1), keras.layers.Activation(keras.activations.sigmoid)])

# SGD - Stocastic Gradient Descent
# mse - Mean Squared Error
model.compile(optimizer=keras.optimizers.SGD(lr=.5), loss='mse')
#model.weights # Gets random untrained wieghts in tf format

#keras.backend.eval(model.weights[0]) # gets weights in keras format. Permitted indices - 0,1
#0 - weights
#1 - biases

#model.fit(data_in, logic_and)

model.fit(data_in, logic_and, epochs = 2000, verbose=False)

# Epoch - It means that the model has seen the entire dataset.


#use this to get the predictions. #change the input to get the output accordingly.
print(model.predict(np.array([[1,0]])))


