def generate_code(i):
    prefix = "#include <stdio.h>\n" \
             "\nchar arr[100000 * 32 * 1024ULL];\n"\
             "int main() {\n" \
             "\tchar arr_elem = 0;\n"
    strs = []
    for j in range(2**11):
        strs.append(f"\tarr_elem += arr[{(j % (1 + 2*i)) * 32 * 1024}];\n")
    suffix = '\tprintf("%d\\n", arr_elem);\n'\
             '\treturn 0;\n'\
             '}'
    return prefix + "".join(strs) + suffix

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
        generated = generate_code(idx)
        if src_dir:
            with open(src_dir + os.sep + str(idx) + "_perm" + str(lim) +
                      ".c", "w+") as f:
                f.write(generated)
