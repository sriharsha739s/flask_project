import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

#train test splitting

def data_split(data, ratio):
    np.random.seed(0)
    shuffled = np.random.permutation(len(data))
    test_set = int(len(data) * ratio)
    test_indices = shuffled[:test_set]
    train_indices = shuffled[test_set:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__ == "__main__":
    #Reading the data
    df = pd.read_csv('data.csv')
    train, test = data_split(df, 0.2)
    X_train = train[['Fever', 'Bodypain', 'Age', 'runnyNose', 'diffBreathing', 'Tiredness']].to_numpy()
    X_test = test[['Fever', 'Bodypain', 'Age', 'runnyNose', 'diffBreathing', 'Tiredness']].to_numpy()

    Y_train = train[['Covid_prob']].to_numpy().reshape(800 , )
    Y_test = test[['Covid_prob']].to_numpy().reshape(199 , )

    lr = LogisticRegression().fit(X_train, Y_train)
    #openning a file to store data
    file = open('model.pkl', 'wb')
    #dump information to that file
    pickle.dump(lr, file)