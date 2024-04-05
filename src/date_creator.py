import pandas as pd
import random
from datetime import datetime
from bank_holidays import Holidays
from date_helper import extract_year


class NotHoliday():
    def __init__(self, known_holidays: Holidays):
        self.holidays = known_holidays.holidays
        self.min_year = self.determine_bounds(0)
        self.max_year = self.determine_bounds(-1)
        self.all_possible_dates = self.get_all_possible_dates()
        self.not_holidays = self.remove_matches()
        self.random_day = self.get_random_date()
        self.today = datetime.today()
        self.inform_user()
    
    def determine_bounds(self, index: int) -> str:
        entry = self.holidays[index]
        return extract_year(entry)

    def get_all_possible_dates(self) -> list[str]:
        lower = f"{self.min_year}-01-01"
        upper = f"{self.max_year}-12-31"
        x = pd.date_range(lower, upper, freq='d')
        x = x.strftime('%Y-%m-%d')
        return x

    def remove_matches(self) -> list[str]:
        not_holidays = []
        for day in self.all_possible_dates:
            if day not in self.holidays:
                not_holidays.append(day)
        return not_holidays

    def get_random_date(self) -> str:
        upper = len(self.not_holidays)
        random_index = random.randint(0, upper)
        return self.not_holidays[random_index]

    def inform_user(self):
        if self.today > datetime.strptime(self.random_day, '%Y-%m-%d'):
            tense = "was not a"
        else:
            tense = "will not be a"
        
        print(f"{self.random_day} {tense} banking holiday in the United Kingdom.")

h = Holidays()
new = NotHoliday(h)