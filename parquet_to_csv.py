import pyarrow.parquet as pq
trips = pq.read_table('green_tripdata_2019-01.parquet')
trips = trips.to_pandas()
print(trips)
trips.to_csv('greentrips_jan.csv')
