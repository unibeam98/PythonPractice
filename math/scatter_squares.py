import matplotlib.pyplot as plt

if __name__ == '__main__':
    x_value = list(range(1, 501))
    y_value = [x ** 2 for x in x_value]
    plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

    # 设置图标标题并给坐标加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of value", fontsize=14)

    # 设置每个坐标轴的取值范围
    plt.axis([0, 500, 0, 500000])

    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.savefig('squares_plot.png', bbox_inches='tight')
    plt.show()
