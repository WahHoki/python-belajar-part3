# teknik menduplikasi list

a = ["ucup","otong","dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a

# ini akanmerubah list
a[1] = "michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list a dan b
print(f"adress a = {hex(id(a))}")
print(f"adress b = {hex(id(b))}")

# menduplikat lsit dengan copy

print("membuat list c dengan a.copy()")
c = a.copy() #full duplicate / data baru

print(f"adress a = {hex(id(a))}")
print(f"adress b = {hex(id(b))}")
print(f"adress c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
