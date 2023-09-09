# from abc import ABC, abstractmethod

# class Test(ABC):
#     @abstractmethod
#     def func(self):
#         ...

# class Child(Test):
#     def func(self):
#         return 7
# c =Child()
# print(c.func())


#single level 
class C_language:
    def __init__(self) -> None:
        self.description = "C is a funtional language which does not support the oops concepts."
    
    def display(self):
        print(self.description)
 
class Python_cla(C_language):
    def __init__(self) -> None:
        super().__init__()
        self.py_description = "python is high level language which is built over various languages like c : uses cpython"
    
    def display(self):
        super().display()
        print(self.py_description)

# p = Python_cla()
# p.display()


#multilevel
# class C_language:
#     def __init__(self) -> None:
#         self.description = "C is a funtional language which does not support the oops concepts."
    
#     def display(self):
#         print(self.description)
 
# class C_plus_plus(C_language):
#     def __init__(self) -> None:
#         super().__init__()
#         self.c_plus_description = "C++ is a Object oriented programming language which support the oops concepts."
    
#     def display(self):
#         super().display()
#         print(self.c_plus_description)

# class Python_cla(C_plus_plus):
#     def __init__(self) -> None:
#         super().__init__()
#         self.py_description = "python is high level language which is built over various languages like c : uses cpython"
    
#     def display(self):
#         super().display()
#         print(self.py_description)

# p = Python_cla()
# p.display()

#multiple_inheritence

# class C_language:
#     def __init__(self) -> None:
#         self.description = "C is a funtional language which does not support the oops concepts."
    
#     def display(self):
#         print(self.description)
 
# class C_plus_plus:
#     def __init__(self) -> None:
#         self.c_plus_description = "C++ is a Object oriented programming language which support the oops concepts."
    
#     def display(self):
#         print(self.c_plus_description)

# class Python_cla(C_plus_plus,C_language):
#     def __init__(self) -> None:
#         super().__init__()
#         self.py_description = "python is high level language which is built over various languages like c : uses cpython"
    
#     def display(self):
#         super().display()
#         print(self.py_description)

# p = Python_cla()
# p.display()

#hirarchical inheritence

# class ObjectOriented:
#     def __init__(self) -> None:
#         self.description = "Object Oriented programming "
    
#     def display(self):
#         print(self.description)
 
# class Java_lan(ObjectOriented):
#     def __init__(self) -> None:
#         super().__init__()
#         self.c_plus_description = "java is an Object oriented programming language"
    
#     def display(self):
#         super().display()
#         print(self.c_plus_description)

# class Python_lan(ObjectOriented):
#     def __init__(self) -> None:
#         super().__init__()
#         self.py_description = "python is high level language which ia an Object oriented Programming"
    
#     def display(self):
#         super().display()
#         print(self.py_description)

# p = Python_lan()
# p.display()
# j = Java_lan().display()

#hybrid inheritance
# class A:
#     ...

# class B(A):
#     ...

# class C(A):
#     ...

# class D(B):
#     ...

# class E(B):
#     ...

# class F(B,C):
#     ...

# class G(D,E):
#     ...

# class H(E,C):
#     ...

# class I(G,H,F,C):
#     ...

# data = I.mro()
# for i in reversed(data):
#     print(i)


#encapsulation
#private member and protected members
# class Employee:
#     def __init__(self) -> None:
#         self._sal = 10000
#         self.name ="xyz"
    
#     def _display(self):
#         print(self._sal, self.name)
    
#     def __display(self):
#         print(self._sal, self.name)

# class Extended(Employee):
#     def __init__(self) -> None:
#         super().__init__()

#     def display_private(self):
#         super()._display()
#         print(self._sal)

#     def display_protected(self):
#         super().__display()
#         print(self._sal)

# Employee()._display()
# Extended().display_private()
# Extended().display_protected()
# Employee().__display()
