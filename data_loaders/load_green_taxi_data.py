import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    months = [10, 11, 12]

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'RatecodeID': pd.Int64Dtype(),
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'ehail_fee': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'payment_type': pd.Int64Dtype(),
        'trip_type': float,
        'congestion_surcharge': float 
    }

    # store data of separate months
    green_taxi_data = []

    # use for loop
    for month in months:
        print(month)
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz'
        print(url)
        df = pd.read_csv(
            url, 
            compression="gzip", 
            dtype=taxi_dtypes, 
            parse_dates=parse_dates,
        )        
        # for checking 
        print(df.shape)

        green_taxi_data.append(df)

    green_taxi_q4_df = pd.concat(green_taxi_data, ignore_index=True)
    
    # for checking
    print('total')
    print(green_taxi_q4_df.shape)

    return green_taxi_q4_df
    
