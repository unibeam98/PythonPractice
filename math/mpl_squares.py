import matplotlib.pyplot as plt

if __name__ == '__main__':
    input_values = [1, 2, 3, 4, 5, 6]
    squares = [1, 4, 9, 16, 25, 36]
    plt.plot(input_values, squares, linewidth=5)

    # 设置图标标题
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of value", fontsize=14)

    # 设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)
    plt.show()
