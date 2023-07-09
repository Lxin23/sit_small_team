# 非ros，运行此文件
from my_detect import my_detect
from my_deepsort import MyDeepSort


def printf(label):  # 非ros端，将检测结果输出到终端
    print(label)


if __name__ == '__main__':
    det = my_detect()
    deepsort = MyDeepSort()

    det.action(printf, deepsort.update)
