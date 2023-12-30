from flask import Flask

app = Flask(__name__)

def makebold(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper

def makeitalic(function):
    def wrapper():
        return"<em>"+function()+"</em>"
    return  wrapper




@app.route('/')
@makeitalic
@makebold
def hello_world():
    return '<h1 style="text-align : center" >Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="<div style="width:100%;height:0;padding-bottom:80%;position:relative;"><iframe src="https://giphy.com/embed/K1wjOn6HImv7y" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/kitten-cat-K1wjOn6HImv7y">via GIPHY</a></p> width=200px'
@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<path:name>/<int:number>")
def name(name, number):
    return f"Hello there a {name }, you are {number} years old "


if __name__ == "__main__":
    app.run(debug=True)


















































# def outer_function():
#     print("\n I'm outer")
#
#     def inner_function():
#         print("\n I'm inner")
#
#     return inner_function
#
# innegr_function = outer_function()
# innegr_function()



## Python Decorator Function
#
# import time
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do Something
#         function()
#         function()
#         # Do Something
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# @delay_decorator
# def say_bye():
#     print("Bye")
#
#
# def say_greetings():
#     print("How are you?")
#
#
# decorated_function = delay_decorator(say_greetings)
#
# decorated_function()




#
# def decorater(function):
#
#     def wrapper():
#
#         function()
#         function()
#         function()
#
#     return wrapper
# @decorater
# def A():
#     print("Abhishek")
# @decorater
# def S():
#     print("Samarth")
# @decorater
# def Aj():
#     print("Ajay")
#
#
#
# A()
# S()
# Aj()
#
#
# d = decorater(A)
# d()


# # Challenge
#
# import time
# current = time.time()
# print(current)
#
# def decorator(function):
#
#     def wrapper():
#         start = time.time()
#         function()
#         end = time.time();
#
#         print(f"{function.__name__} speed: {end - start} s")
#     return wrapper
# @decorator
# def fast():
#     for i in range(1000000):
#         i*i
#
# @decorator
# def slow():
#     for i in range(100000000):
#         i*i
#
#
#
# fast()
# slow()






