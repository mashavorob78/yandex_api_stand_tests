import configuration
import requests

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                            params={"count": 20})

traf=get_logs()


#print(response.status_code)
#print(response.headers)
#print(response.text)
