'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''
# addition = 0
# division = 1
# def calculate(message = 'The result is', **kwargs):
#     if (("operation" in kwargs == 'add') and ("make_float" in kwargs == False)):
#         global addition 
#         addition = kwargs['first'] + kwargs['second']
#         return "f{kwargs['message']} + {addition}"
#     elif(("operation" in kwargs == 'divide') and ("make_float" in kwargs == True)):
#         global division
#         division = kwargs['first'] / kwargs['second']
#         return "f{message} + {division}"

# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))

def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message','The result is')} {int(operation_value)}"
    return final