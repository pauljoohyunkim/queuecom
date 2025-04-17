#!/bin/python

import subprocess
import sys

def file_to_line(filename : str):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]

        # Get rid of empty lines
        return [line for line in lines if line != ""]

def run_command(line : str):
    return subprocess.call(line, shell=True)

def main():
    argc = len(sys.argv)

    if argc != 2:
        print("Usage: queuecom.py file.txt")
        exit(1)

    filename = sys.argv[1]

    while True:
        lines = file_to_line(filename)
        if len(lines) == 0:
            break
        command = lines[0]

        lines.pop(0)

        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
                file.write("\n")

        run_command(command)
        

if __name__ == "__main__":
    main()
