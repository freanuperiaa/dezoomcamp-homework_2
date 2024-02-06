import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/model-caldron-411807-a8db72184585.json"

bucket_name = 'mage-zoomcamp-coy-peria'
project_id = 'model-caldron-411807'
table_name = "green_taxi_data"

root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data(data, *args, **kwargs):
    # print(data['lpep_pickup_date'].unique().tolist())

    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )