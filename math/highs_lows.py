import csv
from matplotlib import pyplot as plt
from datetime import datetime

if __name__ == '__main__':
    # 从文件获取日期和最高气温
    filename = 'data/death_valley_2018_full.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[6].strip())
                low = int(row[7])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        # 根据数据绘制图形
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(dates, highs, c='red', alpha=0.5)
        plt.plot(dates, lows, c='blue', alpha=0.5)
        plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

        # 设置图形格式
        plt.title("Daily high temperatures, 07-2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature(F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
