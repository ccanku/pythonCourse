
x = 7
y = 6
z = 5

enBuyukMesaji = "En buyuk sayi: "
enKucukMesaji = "En kucuk sayi: "
if x > y:
    if x > z:
        print(enBuyukMesaji + "x")
        print(x)
    elif z > x:
        print(enBuyukMesaji + "z")
        print(z)
    elif z == x:
        print(enBuyukMesaji + "x ve z")
        print(x)
elif y > x:
    if y > z:
        print(enBuyukMesaji + "y")
        print(y)
    elif z > y:
        print(enBuyukMesaji + "z")
        print(z)
    elif z == y:
        print(enBuyukMesaji + "y ve z")
        print(z)
elif y == x:
    if x > z:
        print(enBuyukMesaji + "x ve y")
        print(x)
    elif z > x:
        print(enBuyukMesaji + "z= ")
        print(z)
    elif z == x:
        print(enBuyukMesaji + "x, y ve z")
        print(z)