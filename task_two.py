import argparse

parser = argparse.ArgumentParser()

# creating two variables using the add_argument method
parser.add_argument("num1", help="first number")
parser.add_argument("num2", help="second number")
parser.add_argument("operation", help="operation")