# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# https://ru.wikipedia.org/wiki/Кодирование_длин_серий



"""Run-length encoding and decoding functions."""


def main():
    """Demo usage of functions."""
    rle = "rrrrrrrrrlllllllleeeeeeeeeeeee"
    encoded = encode(rle)
    decoded = decode(encoded)

    print("Test Vector: " + rle)

    # Expected output: 9r8l13eJ
    print("Encoded Result: " + formatOutput(encoded))

    # Expected output: rrrrrrrrrlllllllleeeeeeeeeeeee
    print("Decoded Result: " + decoded)


def encode(sequence):
    """Encode a sequence of characters and return the result as a list of tuples (data value and number of observed instances of value).
    Keyword arguments:
    sequence -- a sequence of characters to encode represented as a string.
    """
    count = 1
    result = []

    for x, item in enumerate(sequence): 
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:        
            result.append((sequence[x - 1], count))
            count = 1            
    
    result.append((sequence[len(sequence) - 1], count))

    return result


def decode(sequence):
    """Decodes the sequence and returns the result as a string.
    Keyword arguments:
    sequence -- a list of tuples (data value and number of observed instances of value).
    """
    result = []

    for item in sequence:
        result.append(item[0] * item[1])

    return "".join(result)


def formatOutput(sequence):
    """Returns a print friendly version of the encoded data. 
    Keyword arguments:
    sequence -- list of tuples (data value and number of observed instances of value).
    """
    result = []

    for item in sequence:
        if item[1] == 1:
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])

    return "".join(result)
    

if __name__ == "__main__":
    main()


