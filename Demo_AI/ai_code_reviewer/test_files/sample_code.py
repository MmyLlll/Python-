def calculate_factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.results = []

    def analyze(self):
        if not self.data:
            return "无数据可分析"
        total = sum(self.data)
        average = total / len(self.data)
        return {
            "总和": total,
            "平均值": average,
            "最大值": max(self.data),
            "最小值": min(self.data)
        }