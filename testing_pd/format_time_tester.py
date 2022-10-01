import pandas as pd
import numpy as np
from random import choice
from time import time
import dataframe_image as dfi


def get_random_dataset(n_rows):
    random_string_list = [choice(['acdwe', 'dwedwe']) for _ in range(n_rows)]
    return pd.DataFrame({'column_1': np.random.choice(range(0,100), size=n_rows),
                         'column_2': random_string_list,
                         'column_3': np.random.rand(n_rows)})

def measure_time(func):
    time_start = time()
    func()
    return time() - time_start

def measure_processing_times(dataset):
    times = {'read': {},'write': {}}

    times['write']['csv'] = measure_time(lambda: dataset.to_csv('dataset.csv'))
    times['read']['csv'] = measure_time(lambda: pd.read_csv('dataset.csv'))

    times['write']['hdf'] = measure_time(lambda: dataset.to_hdf('dataset.h5', key='dataset'))
    times['read']['hdf'] = measure_time(lambda: pd.read_hdf('dataset.h5'))

    times['write']['json'] = measure_time(lambda: dataset.to_json('dataset.json'))
    times['read']['json'] = measure_time(lambda: pd.read_json('dataset.json'))

    times['write']['parquet'] = measure_time(lambda: dataset.to_parquet('dataset.parquet'))
    times['read']['parquet'] = measure_time(lambda: pd.read_parquet('dataset.parquet'))

    times['write']['pickle'] = measure_time(lambda: dataset.to_pickle('dataset.pickle'))
    times['read']['pickle'] = measure_time(lambda: pd.read_pickle('dataset.pickle'))

    times['write']['feather'] = measure_time(lambda: dataset.to_feather('dataset.feather'))
    times['read']['feather'] = measure_time(lambda: pd.read_feather('dataset.feather'))
    
    return pd.DataFrame(times)

if __name__=='__main__':
    n_rows = 100000
    dataset = get_random_dataset(n_rows)
    times = measure_processing_times(dataset)
    dfi.export(times, 'performance_table.png')

