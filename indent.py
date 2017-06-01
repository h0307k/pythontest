"""
概要
Python ではインデント(行頭の空白文字の数)が重要な意味を持ち、
同じ数の空白でインデントされた文がブロックとみなされます。
"""

a = 3
if a == 5:
    print("AAA")    # if文の対象
    print("BBB")    # if文の対象
print("CCC")        # if文の対象ではない

print("AAA")    # 8文字の空白とみなされる