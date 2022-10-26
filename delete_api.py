from api_info import *

api_point = 'new_point'

delete_api = client_INFLUXDB.delete_api()

delete_api.delete('1970-01-01T00:00:00Z', '2022-07-20T00:00:00Z',
                  '_measurement=' + api_point, bucket=api_bucket, org=API_ORG_INFLUXDB)
