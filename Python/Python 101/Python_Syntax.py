#Python Syntax & Output

#if condition
if 10 > 9:
    print("10 is greater than 9")

#variable
x = 5
y = "Hello world"

"""
Ini kalau teks nya lumayan panjang
jadi gini mas
anone
"""

# ingin assign banyak variable ke banyak nilai
x, y,z = "Banana", "Berkas", "Bomb"
print(x)
print(y)
print(z)

# kalau ingin assign banyak variable ke satu nilai bisa
x = y = z = "Ketoprak"
print(x)
print(y)
print(z)

things = "Banana", "Berkas", "Bomb"
x, y, z = things
print(x)
print(y)
print(z)

"""
di case ini, things called list, kalau kita unpacking ini dia punya list
masing-masing jadi punya nilai nya sendiri, x banana, y berkas, z bomb
"""

#output variable

x = "golden ketoprak"
print(x)

#ini kalau nilainya berupa string, bisa aja di print
x = "golden ketoprak"
y = "is"
z = "the"
v = "best"

print(x, y, z, v)
# bisa juga di print kalau banyak

print(x)
print("\n")
print(y)
print("\n")
print(z)
print("\n")
print(v)

#ini kalau mau pake \n

#mathematical operation
x = 10
y = 20
print(x + y)


x = "jon"
y = 20
print(x, y)

x = "GOLDEN KETOPRAK"
def myfunc():
    x = "biji"
    print("My favorite food is", x)

myfunc()

print(x)
"""
case 1 : 
ketika 2 variable saling menimpah, maka nilai yang ada di dalam function
yang akan menggantikan isi nilai, hanya saja nilai yang ada di dalam 
function, hanya berlaku di function itu saja
"""

x = "GOLDEN KETOPRAK"
def myfunc():
    global x
    x = "biji"
    print("My favorite food is", x)

myfunc()

print(x)

"""
case 2 : 
Ketika 2 nilai x memiliki status yang sama yaitu global, 
maka akan sama sama berantem dan nilai yang akan di pilih adalah yang di dalam
function
"""

def myfunc():
    global x
    x = "biji"
    print("My favorite food is", x)

myfunc()

print(x)

"""
Ketika di coba, maka ia akan menjadikan biji sebagai nilai global
"""


#Variable type
x = 5
y = "Kale"
z = 1 + 2j
t = ("apple", "banana", "cherry")
l = ["apple", "banana", "cherry"]
print(type(x))
print(type(y))
print(type(z))
print(type(t))
print(type(l))

port = "8080"
port_int = int(port)

if port_int == 8080:
    print("Ya ini udah int")
else:
    print("Bukan int wok")


