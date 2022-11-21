from api_info import *
from influxdb_client.client.write_api import SYNCHRONOUS

api_point = "Power Brick Measurements 2"


write_api = client_INFLUXDB.write_api(write_options=SYNCHRONOUS)


def write_voltage_to_api(voltage_value, api_tag_key, api_tag_value):
    voltage_api = influxdb_client.Point(api_point).tag(
        api_tag_key, api_tag_value).field("voltage", voltage_value)
    write_api.write(bucket=api_bucket, org=API_ORG_INFLUXDB,
                    record=voltage_api)


def write_current_to_api(current_value, api_tag_key):
    current = influxdb_client.Point(api_point).field(
        api_tag_key, current_value)  # does work without .tag()
    write_api.write(bucket=api_bucket, org=API_ORG_INFLUXDB, record=current)


write_current_to_api(0.461, "192.168.1.12")
write_voltage_to_api(117, "Powerbrick ID", "192.168.1.12")
