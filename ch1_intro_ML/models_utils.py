from keras.models import Sequential
from keras.layers import SimpleRNN, LSTM, Dense, GRU
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from models_utils import *
from keras.utils.layer_utils import count_params
import time


def create_RNN(shape):
    model = Sequential()
    model.add(SimpleRNN(64, input_shape=shape))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="Adam", metrics=["accuracy"])
    return model

def create_LSTM(shape):
    model = Sequential()
    model.add(LSTM(64, input_shape=shape))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="Adam", metrics=["accuracy"])
    return model

def create_GRU(shape):
    model = Sequential()
    model.add(GRU(64, input_shape=shape))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="Adam", metrics=["accuracy"])
    return model

def separate_data(data, fraction):
    train_size = int(len(data) * fraction)
    data_fraction = data[:train_size]
    data_remaining = data[train_size:]
    return data_fraction, data_remaining


def train_model_rnn(model_type, X, Y, shape, batch_size, epochs):
    if model_type == "simple":
        model = create_RNN(shape)
    elif model_type == "lstm":
        model = create_LSTM(shape)
    elif model_type == "gru":
        model = create_GRU(shape)
    else:
        print("invalid model type")
        return None
    
    tik = time.time()
    hist = model.fit(X, Y, batch_size=batch_size, epochs=epochs)
    return model, hist, time.time()-tik

def get_num_params(model):
    weights = 0
    for i in range(len(model.trainable_weights)-1):
        weights += model.trainable_weights[i].numpy().size
    return weights


def parse_and_separate_input_output(file, output_list):
    df = pd.read_csv('eeg/EEG_data.csv')
    df_input_data = df.drop(output_list, axis=1)
    df_output_data = df[output_list]
    return df_input_data, df_output_data

def remove_cols(data, col_list):
    df = data.copy()
    df = df.drop(col_list, axis=1)
    return df

def separate_data(data, fraction):
    train_size = int(len(data) * fraction)
    data_fraction = data[:train_size]
    data_remaining = data[train_size:]
    return data_fraction, data_remaining
