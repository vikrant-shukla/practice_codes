class TooYoungAgeException(Exception):
    def __init__(self, args):
        self.msg = args

class TooOldAgeException(Exception):
    def __init__(self, args):
        self.msg = args

age =  int(input("enter your age:"))
if age < 18:
    raise TooOldAgeException("you are about to die in few years")
if age > 60:
    raise TooYoungAgeException("you have enough life to spend, chill!!!!")
else:
    print("ypu will Find some one ")