import numpy as np


class Avg_filter():
    def __init__(self, arr=[], window_size=10) -> None:
        self.arr = list(arr)
        self.N = window_size
        self._x = 0
        self.filte()

    def check(self):
        while len(self.arr) > self.N:
            self.arr.pop(0)

    def append(self, x):
        self.arr.append(x)
        self.check()

    def filte(self, x=None):
        if x is not None:
            self.append(x)
        else:
            if len(self.arr) == 0:
                return
            self.check()
        self._x = np.mean(np.array(self.arr))
        return self._x

    @property
    def x(self):
        return self._x


def angle2rad(x):
    """
    角度转弧度
    """
    return x / 180 * np.pi


if __name__ == '__main__':
    aa = Avg_filter(np.arange(10))
    bb = Avg_filter()
    for i in range(10):
        print(bb.filte(i))
        print(bb.arr)
    print(aa.arr)
    print(aa.filte())
