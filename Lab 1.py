import math

def hypotenuse(a,b):
    return math.sqrt(a ** 2 + b ** 2)


def num_digits(n):
    return len(str(abs(n)))



def tip_amount(total, percent):
    one_percent = float(total) / 100
    tip = one_percent * float(percent)
    tip_rounded = round(tip, 2)
    return tip_rounded
    
#End the code here.
