
# DE Zoomcamp Module 2  - Homework 2

### Freanu Peria

The flow of the pipeline developed is already in the pipeline file in
`\pipelines\green_taxi_etl\metadata.yaml`


The flow of the pipeline is basically

1. `load_green_taxi_data`
2. `transform_green_taxi_data`
3. `export_bigquery_green_taxi_data` & `export_gcs_green_taxi_data`


Answers are shown in the Mage AI web interface. 


## Q1.

After appending the green taxi data in `load_green_taxi_data`, *we get 266855 rows x 20 columns*

## Q2.

doing the following transformation:
```
@transformer
def transform(data, *args, **kwargs):

    # filter data
    data = data[
        (data["passenger_count"] > 0) &
        (data["trip_distance"] > 0)
    ]

    # add new date column
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # remove space from columns 
    data.columns = (data.columns
        .str.replace(' ', '_')
        .str.lower()
    )

    # print(len(data['lpep_pickup_date'].unique().tolist()))
    # print(data.shape)
    print(data['vendorid'].unique().tolist())

    return data
```
*we get 139370 rows x 21 columns*

The transformation is also discussed in one of the lessons in the module

## Q3

As mentioned in the code in Q2 ^above, the answer is

the answer is then *data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date*

this is also discussed in one of the lessons in the module


## Q4
I was able to check this by running this in the transformation code:
```
data['vendorid'].unique().tolist()
```

and *the unique values are 1 and 2*.


## Q5
Counting the columns with upper case and spaces, the answer is *4*


## Q6
In GCS, I only saw 95 folders. I also saw in the slack community that there were also people who had 95 folders only. Somebody said to just pick the closest answer, therefore the answer is 96.

