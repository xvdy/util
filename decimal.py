import sys
import os

def main():
    f_name = sys.argv[1]
    f_path = os.path.join(os.getcwd(), f_name)

    result = []
    with open(f_path, 'rb') as f:
        while True:
            c = f.read(1)
            if c:
                result.append(c)
            else:
                break

    decimal_list = []
    hex_list = []
    for c in result:
        decimal_list.append(ord(c))
        hex_list.append(hex(ord(c)))
    print decimal_list
    print hex_list

if __name__ == '__main__':
    main()
