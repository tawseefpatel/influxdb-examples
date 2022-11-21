import influxdb_client

# InfluxDB API setup
API_TOKEN_INFLUXDB = "API TOKEN"
API_ORG_INFLUXDB = "INFLUX DB ORG"
api_bucket = "BUCKET NAME"
api_url = "LOCAL ADDRESS"

client_INFLUXDB = influxdb_client.InfluxDBClient(
    url=api_url,
    token=API_TOKEN_INFLUXDB,
    org=API_ORG_INFLUXDB
)
