from storage import TemperatureStorage
import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as etree


def fetch_data(starttime, endtime, stationstring='LKTB'):
    url = "https://aviationweather.gov/adds/dataserver_current/httpparam"
    params = {'dataSource':'metars', 'requestType': 'retrieve', 'format':
              'xml', 'stationString': stationstring,
              'startTime': int(starttime), 'endTime': int(endtime)}
    r = requests.get(url, params)
    tree = etree.fromstring(r.text)
    data = {}
    for element in tree.findall('.//data/METAR'):
        timestamp = element.find('./observation_time').text
        temperature = element.find('./temp_c').text
        data[timestamp] = temperature

    return data


if __name__ == '__main__':
    storage = TemperatureStorage()
    starttime = datetime.timestamp(datetime.utcnow() - timedelta(hours=2))
    endtime = datetime.timestamp(datetime.utcnow())
    data = fetch_data(starttime, endtime, 'LKTB')
    for key, value in data.items():
        storage.put_value(key, value)
    print(storage.get_all_values())