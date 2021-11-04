import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

num1 = 10
num2 = 5

add_result = add(num1, num2)
logging.info('Add: {} + {} = {}'.format(num1, num2, add_result))
sub_result = sub(num1, num2)
logging.info('Sub: {} - {} = {}'.format(num1, num2, sub_result))
mul_result = mul(num1, num2)
logging.info('Mul: {} * {} = {}'.format(num1, num2, mul_result))
div_result = div(num1, num2)
logging.info('Div: {} / {} = {}'.format(num1, num2, div_result))
