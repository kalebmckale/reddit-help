import abc
from collections import namedtuple
from calendar import monthrange

import datetime as dt

DEFAULT_HOROSCOPE_TEXT = "something here"

astrology_sign = {
    'Capricorn': ('December 22nd', 'January 19th'),
    'Aquarius': ('January 20th', 'February 18th'),
}

Date = namedtuple("Date", ["year", "month", "day"])

def all_dates_in_year(year=2021):
    for month in range(1, 13): # Month is always 1..12
        for day in range(1, monthrange(year, month)[1] + 1):
            yield Date(year, month, day)


class Horoscope(abc.ABC):
    def __init__(self):
        self._daily = DEFAULT_HOROSCOPE_TEXT
        self._weekly = DEFAULT_HOROSCOPE_TEXT
        self._monthly = DEFAULT_HOROSCOPE_TEXT

    @abc.abstractmethod
    def to_dict(self):
        return {
            'Daily': self._daily,
            'Weekly': self._weekly,
            'Monthly': self._monthly,
        }


class CareerHoroscope(Horoscope):
    def __init__(self):
        super().__init__()
        self._annual = DEFAULT_HOROSCOPE_TEXT

    def to_dict(self):
        return dict(
            **super().to_dict(),
            Annual=self._annual
        )


class HealthHoroscope(Horoscope):
    pass        


class GeneralHoroscope(Horoscope):
    def __init__(self):
        super().__init__()
        self._annual = DEFAULT_HOROSCOPE_TEXT

    def to_dict(self):
        return dict(
            **super().to_dict(),
            Annual=self._annual
        )


#def astrology_date(year=dt.):
    
class AstrologyDate:
    def __init__(self):
        pass

table=tbl_date
columns=(date_id, date_str, week_id, month_id)
entries=[
    (0, 'January 1st', 0, 0),
    (1, 'January 2nd', 0, 0),
    ...,
    (364, 'December 30th', 52, 11),
    (365, 'December 31st', 52, 11)
]

table=tbl_astrology_sign
columns=(sign_id, name, start$date_id, end$date_id)
entries=[
    (0, 'Capricorn', 356, 18),   # 18 is January 19th
    (1, 'Aquarius', 19, 48),     # 48 is February 18th
    (2, 'Pisces', , ),
    (3, 'Aries', , ),
    (4, 'Taurus', , ),
    (5, 'Gemini', , ),
    (6, 'Cancer', , ),
    (7, 'Leo', , ),
    (8, 'Virgo', , ),
    (9, 'Libra', , ),
    (10, 'Scorpio', , ),
    (11, 'Sagittarius', , )
]

table=tbl_horoscope_type
columns=(horo_type_id, horo_type_name)
entries=[
    (0, 'Career Horoscope'),
    (1, 'Health Horoscope'),
    (2, 'General Horoscope')
]

table=tbl_horoscope_date_type
columns=(horo_date_type_id, horo_date_type_name, horo_date_type_table)
entries=[
    (0, 'Daily', tbl_horoscope_daily),
    (1, 'Weekly', tbl_horoscope_weekly),
    (2, 'Monthly', tbl_horoscope_monthly),
    (3, 'Annual', tbl_horoscope_annual)
]


table=tbl_horoscope_daily
columns=(daily_horo_id, daily_horo_type_id, daily_horo_str)
entries=[
    (0, 0, 'something here'),
    (1, 1, 'something here'),
    (2, 2, 'something here'),
    (3, 0, 'something here'),
    (4, 1, 'something here'),
]

table=tbl_horoscope
columns=(horo_id, horo_date_type_id, horo_date_type_table_id


"""
a = {
    date_txt: [
        {
            'id': generate_id(id),
            'Sign': sign.name,
            'Sign Starts': sign.start,
            'Sign Ends': sign.end,
            'Career Horoscope': career[id].to_dict(),
            'Health Horoscope': health[id].to_dict(),
            'General Horoscope': general[id].to_dict()
        } for id in list_id
    ] for date_txt in year
}
"""

"""
"January 1": \[

{ 

id: 0,  
Sign: Capricorn,  
Sign Starts: December 22nd,  
Sign Ends: January 19th,  
Career Horoscope: {  
Daily: "something here",  
Weekly: "something here",  
Monthly: "something here",  
Annual: "something here",  
},  
Health Horoscope: {  
Daily: "something else here",  
Weekly: "something else here",  
Monthly: "something else here",  
},  
General Horoscope: {  
Daily: "something else else here",  
Weekly: "something else else here",  
Monthly: "something else else here",  
Annual: "something else else here",  
}

},

{ 

id: 1,  
Sign: Aquarius,  
Sign Starts: January 20th,  
Sign Ends: February 18th,  
Career Horoscope: {  
Daily: "something here",  
Weekly: "something here",  
Monthly: "something here",  
Annual: "something here",  
},  
Health Horoscope: {  
Daily: "something else here",  
Weekly: "something else here",  
Monthly: "something else here",  
},  
General Horoscope: {  
Daily: "something else else here",  
Weekly: "something else else here",  
Monthly: "something else else here",  
Annual: "something else else here",  
},  


},

etc....

\],

"January 2": \[

\],  


"January 3": \[

\],

&#x200B;

and so on . . . .

I realize the above is an imperfect skeleton with syntax errors, and so I was hoping one of the many much smarter people than I on here could help me put together something solid to get me going.
"""