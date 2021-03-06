from keras.models import Sequential, model_from_json
from keras import optimizers
from sklearn.model_selection import train_test_split
import numpy as np

class Model:
    
    def __init__(self, weights = None):
        self.model = Sequential()
        self.fitness = 0
        self.create(weights)

    def create(self, weights=None):
        return NotImplementedError

    def train(self, values_X, values_Y):
        train_X, test_X, train_Y, test_Y = train_test_split(values_X, values_Y, test_size=0.33) 

        self.model.fit(
            np.array(train_X), np.array(train_Y),
            validation_data=(np.array(test_X), np.array(test_Y)), epochs=200, batch_size=5,
            callbacks=[])

    def evaluate(self, values_X, values_Y):
        self.fitness = self.model.evaluate(np.array(values_X), np.array(values_Y))
        
        return self.fitness

    def predict(self, values_X):
        return self.model.predict(np.array(values_X))