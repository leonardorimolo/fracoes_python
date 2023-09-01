class Fracao:


    def __init__(self,numerador:int,denominador:int):
        if denominador == 0:
            raise ValueError('Atenção! O denominador não pode ser igual a zero')
        else:
            mdc = Fracao.mdc(denominador, numerador)
            if denominador < 0:
                mdc = -mdc
            self._numerador = numerador // mdc
            self._denominador = denominador // mdc


    def mdc(a: int, b: int) -> int:
        " Calcular o maximo divisor comum de a,b."
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def __add__(self, other):
        n = self._numerador * other._denominador + self._denominador * other._numerador
        d = self._denominador * other._denominador
        return Fracao(n,d)

    def __sub__(self, other):
        n = self._numerador * other._denominador - self._denominador * other._numerador
        d = self._denominador * other._denominador
        return Fracao(n,d)

    #FALTA ADICIONAR A MULTIPLICACAO
    #FALTA ADICIONAR A DIVISAO

    def __lt__(self, other):
        return  self._numerador * other._numerador < self._denominador * other._numerador

    def __str__(self):
       return f"{self._numerador} / {self._denominador}"






fracao = Fracao(16,10)

print(fracao)

f1 = Fracao ( 16 , 9 )
f2 = Fracao (3 , 4 )

print ( f1 )
print ( f2 )
f3 = Fracao (5 , 25 )

print ("F1 + F2 =", f1 + f2 )
print ("F2 - F3 =", f2 - f3 )