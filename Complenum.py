import math
class Comple:
    def __init__(self, real:float, unreal: float):
        self.real = real
        self.unreal = unreal
    #Печать числа в виде а+b*i
    def print(self):
        if self.unreal != 0:
            if self.unreal > 0:
                if self.unreal == 1:
                    print(f"{self.real}+i")
                else:
                   print(f"{self.real}+{self.unreal}i")
            else:
                if self.unreal != -1:
                    print(f"{self.real}{self.unreal}i")
                else:
                    print(f"{self.real}-i")

        else:
            print(self.real)
    #Сумма двух комплексных чисел
    def sum_comple(self, a:"Comple"):
        return Comple(real = self.real+ a.real, unreal = self.unreal + a.unreal)
    #Произведение двух комплексных чисел
    def multi_comple(self, a:"Comple"):
        return Comple(real = a.real*self.real-a.unreal*self.unreal, unreal = self.real*a.unreal+self.unreal*a.real)
    #Обратное к комплексному числу
    def invert_comple(self):
        return Comple(real = self.real/(self.real**2+self.unreal**2), unreal = -(self.unreal)/(self.real**2+self.unreal**2))
    #деление двух комплексных чисел
    def division_comple(self, a:"Comple"):
        return self.multi_comple(a.invert_comple())
    #Возведение комплексного числа в натуральную степень
    def pow_comple(self, a:int):
        if a == 0:
            return Comple(real = 1, unreal = 0)
        if a > 0:
         b = self
         for i in range(a-1):
            self = self.multi_comple(b)
         return self
        else:
            return self.pow_comple(-a).invert_comple()
    #Возвести действительное число в комплексную степень
    def pow_in_comple(self, a:float):
        return(Comple(real = a**self.real*math.cos(self.unreal*math.log(a)), unreal = a**self.real*math.sin(self.unreal*math.log(a))))
    #Проверяет равны ли комплексные числа
    def comprasion(self, a:"Comple"):
        return(self.real == a.real and self.unreal == a.unreal)
    def trig_comple(self):
        x = math.atan(self.unreal/self.real)
        return [self.real*(x**2+1), x]
    #Переделывает float или int в Comple
    def float_to_comple(self, a):
        return Comple(real = a, unreal = 0)
    

a = Comple(real = 3, unreal = 1)
a.print()
b = Comple(real = 3, unreal = 91)
c = a.float_to_comple(2)
c.print()
s = a.sum_comple(c)
s.print()
