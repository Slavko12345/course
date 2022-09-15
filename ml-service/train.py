import numpy as np
from sklearn.linear_model import LinearRegression

if __name__=='__main__':
    X_train = np.random.rand(10, 3)
    y_train = np.random.rand(10, 1)

    model = LinearRegression()
    model.fit(X_train, y_train)
    r2 = model.score(X_train, y_train)

    print("r2 score: ", r2)

