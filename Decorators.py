# A Decorator is a function that takes another function as an argument,adds some functionality 
# and then returns a function, All of this without modifying the original function that was passed in.
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function # Same as display = decorator_function(display)
def display():
    print('display function ran')


@decorator_function 
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info('John',25)
display()