import glob
import os

def check_directory():
    cwd = os.getcwd()
    os.chdir(cwd)
    for file in glob.glob('defense-os-data' + '*.zip'):
        if file != "":
            print('it has a value')


def main():
    check_directory()

main()
