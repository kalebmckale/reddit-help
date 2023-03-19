from datetime import datetime as dt

time_of_day = {
    range(1): "it’s midnight!",
    range(1, 5): "it’s nighttime!",
    range(6, 12): "it’s daytime!",
    range(12, 13): "it’s noon!",
    range(13, 18): 'good afternoon!',
    range(18, 21): 'good evening!',
    range(21, 24): "it’s nighttime!"
}
for hour, msg in time_of_day.items():
    if dt.now().hour in hour:
        print(msg)