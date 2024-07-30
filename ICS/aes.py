CONST1 = "10000000"
CONST2 = "00110000"
MIXCOLCONST = [[1, 4], [4, 1]]


def slice_half(pl: str):
    return pl[: len(pl) // 2], pl[len(pl) // 2 :]


def nibblize(work: str):
    return work[0:4], work[4:8], work[8:12], work[12:16]


def xor(str1: str, str2: str):
    xored = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            xored += "0"
        else:
            xored += "1"
    return xored


def s(n: str):
    i, j = slice_half(n)
    if i == "00":
        if j == "00":
            return "1000"
        elif j == "01":
            return "0100"
        elif j == "10":
            return "1010"
        elif j == "11":
            return "1011"

    elif i == "01":
        if j == "00":
            return "1101"
        elif j == "01":
            return "0001"
        elif j == "10":
            return "1000"
        elif j == "11":
            return "0101"

    elif i == "10":
        if j == "00":
            return "0110"
        elif j == "01":
            return "0010"
        elif j == "10":
            return "0000"
        elif j == "11":
            return "0011"

    elif i == "11":
        if j == "00":
            return "1100"
        elif j == "01":
            return "1110"
        elif j == "10":
            return "1111"
        elif j == "11":
            return "0111"


def key_gen(w):

    def g(w1, cnt):
        n0, n1 = slice_half(w1)
        n0_, n1_ = s(n1), s(n0)
        w1_ = xor(n0_ + n1_, cnt)
        return w1_

    w0, w1 = slice_half(w)
    w1_ = g(w1, CONST1)
    w2 = xor(w1_, w0)
    w3 = xor(w2, w1)

    w3_ = g(w3, CONST2)
    w4 = xor(w3_, w2)
    w5 = xor(w3, w4)
    return w0, w1, w2, w3, w4, w5


def add_round_key(pt: str, key: str):
    return xor(pt, key)


def shift_row(nsk: str):
    n0, n1, n2, n3 = nibblize(nsk)
    return n0 + n3 + n2 + n1


def nibble_substitution(ark: str):
    n0, n1, n2, n3 = nibblize(ark)
    return s(n0) + s(n1) + s(n2) + s(n3)


def star(nib1: str, nib2: str):
    num1, num2 = int(nib1, 2), nib2
    mul = (num1 * num2) % 16
    result_bin = format(mul, "04b")
    return result_bin


def mul_mat(srw: str):
    n0, n1, n2, n3 = nibblize(srw)
    ans_mat = [
        [xor(star(n0, 1), star(n1, 4)), xor(star(n2, 1), star(n3, 4))],
        [xor(star(n0, 4), star(n1, 1)), xor(star(n2, 4), star(n3, 1))],
    ]
    return ans_mat[0][0] + ans_mat[1][0] + ans_mat[0][1] + ans_mat[1][1]


def mix_column(srw: str):
    return mul_mat(srw)


def excription(pt: str, keys: list[str]):
    ark = add_round_key(pt, keys[0] + keys[1])
    nsk = nibble_substitution(ark)
    srw = shift_row(nsk)
    mcw = mix_column(srw)
    ark1 = add_round_key(mcw, keys[2] + keys[3])
    nsk1 = nibble_substitution(ark1)
    srw1 = shift_row(nsk1)
    cypher = add_round_key(srw1, keys[4] + keys[5])
    return cypher


plain_text = "1101011100101000"
key = "0100101011110101"
keys = key_gen(key)

print(excription(plain_text, keys))
