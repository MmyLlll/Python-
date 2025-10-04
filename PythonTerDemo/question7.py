# 编写一个程序，X,Y作为输入，生成一个二维数组，数组的第i行和第j列的元素值应该是ij。
# 注意:i= 0,1..X-1;j=0,1,Y-1。假设，程序输入3,5;则程序输出为:[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]];
def generete_2d_array(X,Y):
    array_2d = [[0 for _ in range(Y)] for _ in range(X)]
    for i in range(X):
        for j in range(Y):
            array_2d[i][j] = i*j
    return array_2d

x = 3
y = 5
generete_2d_array(x,y)
print(generete_2d_array(x,y))