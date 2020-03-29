##Error
#1 compile time        --> error done by programmer
#2 logical
#3 run time error      --> error done by user

# aim: even if you get exception/error your execution should not stop

a = 10
b = 0

try:
    print(a/b)
except Exception:
    print("Hey you cannot divide any value by 0")
print("Bye")

print("==========# or=========================")

a = 10
b = 4
try:
    print("resource open")
    print(a/b)
    print("resource close")
except Exception as e:
    print("Hey you cannot divide any value by 0",e)
print("Bye")


print("==========# or=========================")

a = 10
b = 0
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("Hey you cannot divide any value by 0",e)
finally:
    print("resource close")


print("==========# or=========================")

a = 10
b = 5
try:
    print("resource open")
    print(a/b)
    k =int (input("Enter a number"))            # if we enter string thrn exception handle that error also like a/0
    print(k)

except Exception as e:
    print("Hey you cannot divide any value by 0",e)

finally:
    print("resource close")



print("==========# or=========================")
# diff type error handle by diff state

a = 10
b = 0                              #get  ZeroDivisionError
try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number"))      # if we enter string then get value error.
    print(k)
except ZeroDivisionError as z:
    print("Hey you cannot divide any value by 0",z)

except ValueError as v:
    print("invalid input")

except Exception as e:
    print("something wents wrong", e)

finally:
    print("resource close")
