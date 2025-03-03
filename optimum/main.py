"""typing modülü tipleri belirtmek için"""
from typing import Callable, Union

Num = Union[int, float]


def d(f: Callable[[Num], Num], h: Num = 0.001) -> Callable[[Num], Num]:
    """nümerik türev alma"""
    def fark(x: Num) -> Num:
        return (f(x + h) - f(x)) / h
    return fark


def root(f: Callable[[Num], Num], a: Num, k: int = 10) -> Num:
    """kök almak için newton-raphson metodu kullanılıyor"""
    for _ in range(k):
        a = a - (f(a) / d(f)(a))
    return a


def area_filt(f: Callable[[Num], Num], a: list,h: Num) -> list:
    """verilen alandaki kökleri bulur"""
    def fitrele(x: tuple[Num, Num]) -> bool:
        return f(x[0])*f(x[1])<0
    l=[]
    for i in a:
        l.append((i-h,i+h))
    return list(filter(fitrele,l))


#def area(a: Num, b: Num, h: Num) -> list:
#    """alan döndürür"""




def main() -> None:
    """ana fonksiyon"""
    # f = lambda x : x**2 - 4
    def f(x: Num) -> Num:
        """basit bir fonksiyon"""
        return x**2 - 4
    k=area_filt(f,list(range(-4,4)),1)
    for i in k:
        print(root(f,i[0]+1))


if __name__ == '__main__':
    main()
