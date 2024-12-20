def area(width, height):
    if not(isinstance(width, (int, float)) and
           isinstance(height, (int, float))):
        raise TypeError('The width and height must be of type int or float')

    if not(width > 0 and height > 0):
        raise ValueError('The width and height must be positive.')

    return width * height

def isPalindrom(word):
    if word == word[::-1]:
        print(word, word[::-1])
        return True

print(isPalindrom('komar'))