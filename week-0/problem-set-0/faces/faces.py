#!/usr/bin/env python

def convert(string):
    string = string.replace(":)", "😀")
    string = string.replace(":(", "🥲")
    return string

def main():
    word = input()
    print(convert(word))

main()
