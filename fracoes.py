class Fracao:


    def __init__(self,numerador:int,denominador:int):
        if denominador == 0:
            raise ValueError('Atenção! O denominador não pode ser igual a zero')
        else:
            mdc = Fracao.mdc(denominador, numerador)
            if denominador < 0:
                mdc = -mdc
            self._numerador = numerador // mdc #simplificando a fracao dividindo pelo seu mdc
            self._denominador = denominador // mdc #simplificando a fracao dividindo pelo seu mdc

    #CALCULO MDC
    def mdc(a: int, b: int) -> int:
        " Calcular o maximo divisor comum de a,b."
        while b != 0:
            r = a % b
            a = b
            b = r
        return a


    #----OPERAÇÕES MATEMÁTICAS----

    #ADIÇÃO
    def __add__(self, other):
        n = self._numerador * other._denominador + self._denominador * other._numerador
        d = self._denominador * other._denominador
        return Fracao(n,d)

    #SUBTRAÇÃO
    def __sub__(self, other):
        n = self._numerador * other._denominador - self._denominador * other._numerador
        d = self._denominador * other._denominador
        return Fracao(n,d)
    
    #MULTIPLICAÇÃO
    def __mul__(self,other):
        n = self._numerador * other._numerador
        d = self._denominador * other._denominador
        return Fracao(n,d)

    #DIVISÃO
    def __truediv__(self,other):
        n = self._numerador * other._denominador
        d = self._denominador * other._numerador
        return Fracao(n,d)
    




    #----OPERADORES RELACIONAIS-----

    #MENOR
    def __lt__(self, other):
        return self._numerador * other._denominador < self._denominador * other._numerador
         
    #IGUAL
    def __eq__(self,other):
        if self._numerador == other._numerador and self._denominador == other._denominador:
            return True
        return False
    
    #MENOR IGUAL
    def __le__(self):
        return Fracao.__lt__ or Fracao.__eq__







    #----CONVERSÕES DE TIPO----

    #STRING
    def __str__(self):
       return f"{self._numerador} / {self._denominador}"
    
    #FLOAT
    def __float__(self):
        return float(self._numerador / self._denominador)
    
    #INT
    def __int__(self):
        return int(self._numerador / self._denominador)








#-----TESTES------

f1 = Fracao ( 16 , 9 )
f2 = Fracao (3 , 4 )
f3 = Fracao (5 , 25 )
f4 = Fracao ( 16 , 4 )
f5 = Fracao (5 , 4 )
print ( f1 )
print ( f2 )
print ( f3 )
print ( f4 )
print ( f5 )
print ("F1 + F2 =", f1 + f2 )
print ("F2 - F3 =", f2 - f3 )
print ("F3 * F4 =", f3 * f4 )
print ("F4 / F5 =", f4 / f5 )
print ("16/2 + 16/2 =", Fracao ( 16 , 2 ) + Fracao ( 16 , 2 ) )
print ("F2 == F3 =", f2 == f3 )
print ("F3 > F3 =", f3 > f3 )
print ("F4 == 4/1 =", f4 == Fracao (4 , 1 ) )
print ( f1 , float ( f1 ) , int( f1 ) )
print ( f2 , float ( f2 ) , int( f2 ) )
print ( f3 , float ( f3 ) , int( f3 ) )
print ( f4 , float ( f4 ) , int( f4 ) )
print ( f5 , float ( f5 ) , int( f5 ) )