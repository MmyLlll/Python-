#使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字
class DivisibleBySeven:
    def __init__(self,n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.current <= self.n:
            if self.current % 7  == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration
n = 100
for number in DivisibleBySeven(n):
    print(number)


