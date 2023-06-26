
hello_there = 'hi'

class HelloWorld:

    def __init__(self, greeting='hello world') -> None:
        self.greeting = greeting

    def say_hello(self, greeting:str="") -> None:
        if greeting == "":
            greeting = self.greeting
        print(greeting)