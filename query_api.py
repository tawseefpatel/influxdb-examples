from api_info import *


query_api = client_INFLUXDB.query_api()

flux_query = 'from(bucket:"Smartplug")' \
    ' |> range(start: -1m, stop: now())' \
    ' |> filter(fn: (r) => r._measurement == "5_day_test_SN239")'\
    ' |> filter(fn: (r) => r._field == "power")'

result_df = query_api.query_data_frame(query=flux_query, org=API_ORG_INFLUXDB)
result_df.to_csv('results.csv')
