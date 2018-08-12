import pandas as pd
from random import random
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import LSTM

flow = (list(range(1, 10, 1)) + list(range(10, 1, -1))) * 100
pdata = pd.DataFrame({"a": flow, "b": flow})
pdata.b = pdata.b.shift(9)
data = pdata.iloc[10:] * random()


def _load_data(data, n_prev=100):
    """
    data should be pd.DataFrame()
    """
    docX, docY = [], []
    for i in range(len(data) - n_prev):
        docX.append(data.iloc[i:i + n_prev].as_matrix())
        docY.append(data.iloc[i + n_prev].as_matrix())
    alsX = np.array(docX)
    alsY = np.array(docY)
    return alsX, alsY


def train_test_split(df, test_size=0.1):
    ntrn = round(len(df) * (1 - test_size))

    X_train, y_train = _load_data(df.iloc[0:ntrn])
    X_test, y_test = _load_data(df.iloc[ntrn:])
    return (X_train, y_train), (X_test, y_test)


(X_train, y_train), (X_test, y_test) = train_test_split(data)
in_out_neurons = 2
hidden_neurons = 50

model = Sequential()

model.add(LSTM(11, input_shape=(100, 2)))
model.add(Dense(2))
model.add(Activation("linear"))
model.compile(loss="mean_squared_error", optimizer="rmsprop")
model.fit(X_train, y_train, batch_size=700, nb_epoch=100, validation_split=0.05)
predicted = model.predict(X_test)
