# classes

class employee: 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



      
emp_1 = employee('Ferran','Font', 80000)
emp_2 = employee('Marta','Aspiroz', 60000)

print(emp_1.email)

#emp_1.fullname()
print(emp_1.fullname())
print(emp_2.fullname())

# Podemos usar el método llamando a la clase, lo cual es más lógico
print('Llamada a la clase:')
print(employee.fullname(emp_2) )