def AddAndReset(min, max, first, second): # if a+b > max -> min + ( b - (max - a))

    if second > max or first > max or second < min or first < min:
        raise Exception("Maximum " + str(max) + "\nMinimum " + str(min) + "\nFrist" + str(first) + "\nSecond " + str(second))

    if second <0: raise Exception("AddAndReset: Subtraction is not allowed")

    result = None

    if first + second > max:
        result = min + (second - (max - first))
    else:
        result = first + second

    return result

def SubAndReset(min, max, first, second): # if a-b < min -> max - ( b - a )

    if second > max or first > max or second < min or first < min:
        raise Exception("Maximum " + str(max) + "\nMinimum " + str(min) + "\nFrist" + str(first) + "\nSecond " + str(second))

    if second <0: raise Exception("SubAndReset: Addition is not allowed")

    result = None

    if first - second < min:
        result = max - (second - first)
    else:
        result = first - second

    return result
