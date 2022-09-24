import pandas as pd
import numpy as np
from random import choice
from time import time, sleep
from multiprocessing import Pool
import itertools

def get_random_dataset(n_rows):
    random_string_list = [choice(['acdwe', 'dwedwe']) for _ in range(n_rows)]
    return pd.DataFrame({'column_1': np.random.choice(range(0,100), size=n_rows),
                         'column_2': random_string_list,
                         'column_3': np.random.rand(n_rows)})

def predict(row):
    sleep(0.01)
    return (row['column_3']>0.5) & (row['column_2'][0]=='a')

def process_single_core(dataset):
    result = []
    for index, row in dataset.iterrows():
        res = predict(row)
        result.append(res)
    return result

def process_multiple_cores(dataset, n_cores):
    df_split = np.array_split(dataset, n_cores)
    pool = Pool(n_cores)
    res = itertools.chain.from_iterable(pool.map(process_single_core, df_split))
    pool.close()
    pool.join()
    return list(res) 

if __name__=='__main__':
    dataset = get_random_dataset(100)
    
    time_0 = time()
    result_single = process_single_core(dataset)
    time_1 = time()
    result_multiple = process_multiple_cores(dataset, n_cores=4)
    time_2 = time()
    
    assert result_single==result_multiple
    
    print("single processing time: ", time_1 - time_0)
    print("4 processes processing time: ", time_2 - time_1)
