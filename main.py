import glob
import os
import requests
import sys


def main():
    # print_hello_world()
    # print_hi('Simon')
    # read('C:\\WINDOWS\\DirectX.log')
    # get('https://www.google.ca/')
    dir('C:\\WINDOWS\\*.log')
    

def get(url):
    response = requests.get(url)
    print(response.status_code)
    print(response.content)
    print(type(response))


def read(file):
    stream = open(file)
    string = stream.read()
    stream.close()

    print(string)
    

def dir(pathname):
    paths = glob(pathname)

    for path in paths:
        print(path)


def print_hello_world():
    for i in range(1, 6):
        print(f'Hello World {i}!')


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
