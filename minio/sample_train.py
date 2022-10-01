import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
from minio_client import MinioClientNative
from pathlib import Path

if __name__=='__main__':
    X_train = np.random.rand(10, 3)
    y_train = np.random.rand(10, 1)

    model = LinearRegression()
    model.fit(X_train, y_train)

    model_path = Path('dummy_model')
    pickle.dump(model, open(model_path, 'wb'))

    minio_client = MinioClientNative('models')
    minio_client.upload_file(model_path)
