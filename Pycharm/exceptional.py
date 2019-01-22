import sys
from math import log

def convert(s):
    try:
        x=int(s)
        print(x)
#     except ValueError:
    except (ValueError, TypeError):
        print("conversion error")
        x=-1
    return x

def convert1(s):
    x=-1
    try:
        x=float(s)
        return(x)

#    except (ValueError, TypeError):
    except (ValueError, TypeError) as e:
        print("Conversion Error {}".format(str(e)),file=sys.stderr)
#       return(-1)
        raise
    finally:
        print("This will execute anyways")

def string_log(s):
    v = convert1(s)
    print(log(v))
