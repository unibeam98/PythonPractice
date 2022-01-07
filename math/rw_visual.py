import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == '__main__':
    while True:
        # 创建一个RandomWalk实例，并将其点绘制出来
        rw = RandomWalk(50000)
        rw.fill_walk()

        # 设置绘图窗口尺寸
        plt.figure(dpi=128, figsize=(10, 6))

        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_vlaues, c=point_numbers, cmap=plt.cm.Blues,
                    edgecolors='none', s=1)

        # 突出起点和终点
        plt.scatter(0, 0, c='green', edgecolors='none', s=100)
        plt.scatter(rw.x_values[-1], rw.y_vlaues[-1], c='red', edgecolors='none', s=100)

        # 隐藏坐标轴
        plt.axis('off')
        plt.show()

        keep_running = input("Make another walk?(y/n): ")
        if keep_running == 'n':
            break
