try:
    str1 = "123"
    # TypeError
    str1 / 5
    # ZeroDivisionError
    10 / 0

except ValueError:
    print "ya"

except ZeroDivisionError:
    print "ZeroDivisionError"

except:
    print "got everythings!"
