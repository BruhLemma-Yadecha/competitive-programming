def swap_case(s):
    r = ""
    ascii_A = ord('A')
    ascii_a = ord('a')
    ascii_Z = ord('Z')
    ascii_z = ord('z')
    for c in s:
        ascii_ver = ord(c)
        if ascii_ver >= ascii_A and ascii_ver <= ascii_Z:
            r = r + chr(ascii_ver - ascii_A + ascii_a)
        elif ascii_ver >= ascii_a and ascii_ver <= ascii_z:
            r = r + chr(ascii_ver - ascii_a + ascii_A)
        else:
            r = r + c
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)