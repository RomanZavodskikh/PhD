# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import sys
import os
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def generate_code(i):
    prefix = "#include <stdio.h>\n" \
             "\nchar arr[100000 * 32 * 1024ULL];\n"\
             "int main() {\n" \
             "\tchar sum = arr[0];\n"
    strs = []
    for j in range(2**9):
        strs.append(f"\tarr[{j+i}] = arr[{j}] + arr[{j+random.randint(0, i//8)}] + arr[{j+random.randint(0, i//2)}] + arr[{j+random.randint(0, i)}];\n")
    suffix = '\tprintf("%d\\n", sum);\n'\
             '\treturn 0;\n'\
             '}'
    return prefix + "".join(strs) + suffix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lim = 256
    if len(sys.argv) > 1:
        lim = int(sys.argv[1])

    second_lim = 128
    if len(sys.argv) > 2:
        second_lim = int(sys.argv[2])

    iterations = 64
    if len(sys.argv) > 3:
        iterations = int(sys.argv[3])

    src_dir = None
    if len(sys.argv) > 4:
        src_dir = sys.argv[4]
     
    for idx in range(iterations):
        generated = generate_code(int(1.07**idx))
        print(generated)
        if src_dir:
            with open(src_dir + os.sep + str(idx) + "_perm" + str(lim) + ".c", "w+") as f:
                f.write(generated)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
