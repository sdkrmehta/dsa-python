class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        if value == 1:
            return -1

        if index > 0:
            if value % 2 == 0:
                if value < 2 * (index + 1):
                    return -1

            else:
                p = self.get_small(value)

                if value - p < 2 * index:
                    return -1

        R = n - 1 - index
        if R == 0:
            return value

        if value % 2 == 0:
            return value + 2 * R
        else:
            p = self.get_small(value)
            return value + p + 2 * (R - 1)

    def get_small(self, x):
        if x % 2 == 0:
            return 2

        d = 3
        while d * d <= x:
            if x % d == 0:
                return d

            d += 2

        return x