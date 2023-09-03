
def DivExp(a,b):
    try:
        assert a>0, "Number 'a' is Negative"
        if b==0:
            raise ZeroDivisionError("Zero Division Error")
        c = a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    except AssertionError as e:
        print("Assertion failure: " + str(e))