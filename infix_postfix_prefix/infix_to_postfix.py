#!/usr/bin/env python



def infix_to_postfix(exp):
    exp = exp.replace(" ","")
    operations = []
    for char in exp:
        print(char)

if __name__ == "__main__":
    exp = input("Expression to Convert: ")
    infix_to_postfix(exp)
