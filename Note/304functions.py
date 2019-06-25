#-----------返回函數-----------
def cal_sum(*args):
    ttl = 0
    for i in args:
        ttl = ttl + i
    return ttl

#若不是要立即求和，而是返回求和的函數
def lazy_sum(*args):
    def sum():
        ttl = 0
        for i in args:
            ttl = ttl + i
        return ttl
    return sum()

f = lazy_sum(1, 3, 5)
#返回的是求和函數
f
#<function lazy_sum.<locals>.sum at 0x101c6ed90>

#調用函數才真正求和
f()
#9

#-----------匿名函數-----------
'''
匿名函數有個限制，就是只能一個表達式，不用寫return，用匿名的好處在於
匿名函數沒有名字，不必擔心函數名衝突。
'''
lambda x: x * x

#-----------偏函數-----------
在調用函數時，有些函數可以傳入額外的參數轉換為別的用途，範例如下
int('12345')
#12345
int('12345', base=8)
#5349

'''
int只要傳入base參數，即可以做N進位轉換，假設要大量轉換，可以建立一
個函數為int8()的函數
'''
def int8(x, base=8):
    return int(x, base)
    
#但functools.partial提供創建偏函數的功能，不需要自己創建函數
import functools
int8 = functools.partial(int, base=8)
int8('1000000')
