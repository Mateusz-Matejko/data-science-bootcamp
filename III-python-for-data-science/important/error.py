x = 10
try:
    print( x / 0 )
except (ZeroDivisionError, TypeError):
    print("You have tried division by 0")
finally:
    print("Wykonałem się!")

print("I am here.")

