#map
#map(function, *iterable)
def double(x):
    return x*x

m = map(double, [1, 2, 3])
#結果為迭代器，需透過list來將整個序列計算出來
list(m)
#[1, 4, 9]

#reduce
#reduce(function, [x1, x2, x3]) = f(f(x1, x2), x3)
from functools import reduce
def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3])
print(r)
#6
