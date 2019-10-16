"""
分析csv文件头
"""
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = r'pydata/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
    # print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜的日期标签，避免重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
