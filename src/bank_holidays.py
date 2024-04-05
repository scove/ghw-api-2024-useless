import requests

API_URL = "https://www.gov.uk/bank-holidays.json"

class Holidays():
    def __init__(self):
        self.holidays = self.get_holidays()
    
    def pull_from_api(self) -> dict:
        r = requests.get(API_URL)
        return r.json()

    def get_holidays(self) -> list:
        response_data = self.pull_from_api()
        holidays = []
        for area in response_data:
            for holiday_data in response_data[area]['events']:
                holidays.append(holiday_data['date'])
        return holidays
