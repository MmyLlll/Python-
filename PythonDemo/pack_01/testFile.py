def func(kwarges):
    print(kwarges)
    print(type(kwarges))
dict = {'name':'小米呦'}
func(dict)

def func1(**kwarges):
    print(kwarges)
    print(type(kwarges))
dict = {'name1':'小米呦','name2':'月月鸟'}
func1(name1 = '小米呦',name2 = '月月鸟')