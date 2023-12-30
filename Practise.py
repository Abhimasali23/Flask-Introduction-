#
# ##  Advanced Python Decorator Functions
#
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authentication_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
# @is_authentication_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
# new_user = User("Abhishek")
# new_user.is_logged_in = True
# create_blog_post(new_user)



# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         print(f"You call {function.__name__} {args}")
#         result = function(args[0], args[1], args[2])
#         print(f"It returned: {result}")
#     return wrapper
#
#
# @logging_decorator
# def Multiplication_function(a, b, c):
#     return a * b * c
#
# Multiplication_function(1, 2, 3)



def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__} {args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def Multiplication_function(a, b, c):
    return a * b * c

Multiplication_function(2, 5, 6)






























