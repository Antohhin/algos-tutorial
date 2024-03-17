"""

"""

class Solution:
    """
    Encodes a list of strings to a single string using padding as delimiters.
    
    Each string is prefixed with its length in a 4-character wide field, 
    allowing for easy extraction during decoding.
    """
    def encode(self, strs):
        res = ''
        for s in strs: 
            length = '{:4}'.format(len(s)) # фиксирование ширины строки до 4 символов 
            res += length + s

        return res # фиксированная длина позволяет точно определить где строка начинается и заканчивается

    """
    Decodes a single string to a list of strings.

    Each string was encoded with a 4-character length prefix, which we use to 
    determine where one string ends and the next begins.
    """
    def decode(self, str):
        decoded_string = []
        i = 0
        while i < len(str):
            size = int(str[i: i + 4])
            i += 4
            print(i, size)
            decoded_string.append(str[i: i + size])
            i += size
                
        return decoded_string
   
    """
    Encode using # delimiter
    concatenation size of string + delimiter + string self 
    """
    def encode_delimiter(self, strs):
        endoded_string = ''
        for s in strs:
            endoded_string += str(len(s)) + "#" + s
        
        return endoded_string
    
    """
    Напиши на русском, тк сложно суукка 
    - Две петли while loop одна для текущего указателя i
    - Вторая для поиска индекса разделителя (delimiter)
    - Передвигаются друг за другом
    - Когда встречаю # (delimiter) 
    1. всё что слева до текущего указателя будет длина строки size
    2. delimiter + 1 - начало строки и 
        до del + 1 + size - конец строки
    - обновляю текущий указатель на конец строки, для считывания следующего числа
    """
    def decode_delimiter(self, str):
        decoded_string = []
        i = 0
        while i < len(str):
            delimiter = i
            while str[delimiter] != "#":
                delimiter += 1
            size = int(str[i: delimiter])
            decoded_string.append(str[delimiter + 1 : delimiter + 1 + size])
            i = delimiter + 1 + size
            # i += size
                
        return decoded_string

s = Solution()
# encode_str = s.encode(['I', 'love', 'you'])
# decode_str = s.decode(encode_str)
encode_str = s.encode_delimiter(['I', 'love', 'you'])
decode_str = s.decode_delimiter(encode_str)

print(encode_str, decode_str)