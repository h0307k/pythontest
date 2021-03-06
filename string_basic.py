# -*- coding: utf-8 -*-

# 文字列の基礎
print('python-izm')
print("python-izm")

# 文字列の連結
test_str = 'python'
test_str = test_str + '-'
test_str = test_str + 'izm'
print(test_str)

# 文字列の追加
test_str = '012'
test_str += '345'
test_str += '678'
test_str += '9'
print(test_str)

# 指定回数分繰り返す
test_str = '012' * 3
print(test_str)

# 文字列の変換
test_integer = 100
print(str(test_integer) + '円')

# 文字列の置換
test_str = 'python-izm'
print(test_str.replace('izm','ism'))

# 文字列の分割
print(test_str.split('-'))

# 文字列の桁揃え
test_str = '1234'
print(test_str.rjust(10,'0'))
print(test_str.rjust(10,'!'))

# ゼロで桁埋め
test_str = '1234'

print(test_str.zfill(10))
print(test_str.zfill((3)))

# 文字列の検索
test_str = 'python-izm'
print(test_str.startswith('python'))
print(test_str.startswith('izm'))

# 文字列中に任意の文字が含まれているか
test_str = 'python-izm'
print('z' in test_str)
print('s' in test_str)

# 小文字・大文字変換
test_str = 'Python-Izm.com'
print(test_str.upper())
print(test_str.lower())

# 先頭・末尾の削除
print('----------------------------------')

test_str = '     python-izm.com'
print(test_str)

test_str = test_str.lstrip()
print(test_str)

test_str = 'python-izm.com     '
print(test_str + '/')

test_str = test_str.rstrip()
print(test_str + '/')

test_str = test_str.rstrip("com")
print(test_str)
