# python
**Python** ile oluşturduğum basit projeler için bir repository.


## matris_carp projesi:
matriscarp(x,y) fonksiyonunun açıklaması.
``` python
def matriscarp(x,y):
    z=list()
    if(matrisgenislik(x)==matrisyukseklik(y)):
        z=matrisol(matrisyukseklik(x),matrisgenislik(y))
        for j in range(matrisyukseklik(x)):
            for i in range(matrisgenislik(y)):
                for k in range(matrisyukseklik(y)):
                    z[j][i]+=x[j][k]*y[k][i]
        return z
    else:
        return False

```
Bu fonksiyonun asıl amacı 2 tane 2 boyutlu diziyi matris çarpımı kuralına uygun bir şekilde çarpıp  bu çarpımı döndürmektir.
Eğer bu matrisler çarpılamaz ise False değerini döndürür.

İlk olarak z adında boş bir dizi oluşturuyoruz.
Bu boş diziyi oluşturma sebebim çarpımın sonucunu bu diziye atarak return edebilmektir:

``` python
if(matrisgenislik(x)==matrisyukseklik(y)):
```
Bu koşulun amacı ise matrislerin çarpılıp çarpılamamasını kontrol etmektir.
Matrislerin çarpılabilmesi için çarpılacak matrislerden ilkinin genişliği ile ikincisinin yüksekliği aynı olmalıdır.(not:Matris çarpımında değişme özelliği yoktur.)

``` python
z=matrisol(matrisyukseklik(x),matrisgenislik(y))
```
