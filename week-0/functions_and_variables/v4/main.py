#!/usr/bin/env python

def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    # takes to and say hello
    return f"hello, {to}"


main()
