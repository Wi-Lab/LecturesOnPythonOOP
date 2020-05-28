'''
Error Handling
'''

'''
lots of code before this
'''

d = f

# b = 0

# a = b

# c = 234/a

'''
lots of code after this
'''

'''How to handle this errors in our project?'''

# try:
#     var1 = var2
# except Exception:
#     print("we have error")


'''Exception is for handling general error(we do not know exact error Type)'''

# try:
#     var1 = var2
# except NameError:
#     print("we have name error")


'''We may have multiple except blocks in try statement'''
# d = 11
# try:
#     a = 23/d
#     var1 = var2
# except NameError:
#     print("we have name error")
# except ZeroDivisionError:
#     print("we have zero division error")
# except Exception:
#     print("we have error")

'''we can print error message'''

# d = 11
# try:
#     a = 23/d
#     var1 = var2
# except NameError as ne:
#     print(ne)
# except ZeroDivisionError as zde:
#     print(f"{zde} , line 58, file main.py")
# except Exception as e:
#     print(e)


''' try except else '''

# d = 11
# try:
#     a = 23/d
# except NameError as ne:
#     print(ne)
# except ZeroDivisionError as zde:
#     print(f"{zde} , line 58, file main.py")
# else:  # if we have no errors then execute else block
#     f = a**2
#     print(f"f is {f}")

'''we may have other codes after this try block'''


''' try except else finally'''

# d = 0
# try:
#     a = 23/d
# except NameError as ne:
#     print(ne)
# except ZeroDivisionError as zde:
#     print(f"{zde} , line 58, file main.py")
# else:  # if we have no errors then execute else block
#     f = a**2
#     print(f"f is {f}")
# finally:  # this block will be executed whether we have error or not
#     d = 12
#     print(f"d is {d}")
