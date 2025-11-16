# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: D:\Python Decompilation Tool\example.py
# Compiled at: 2025-11-11 03:19:56
# Size of source mod 2**32: 176 bytes


def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)
