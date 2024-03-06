def encode_answers(answers):
    multipleChoice = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}
    bit_string = ''.join([multipleChoice[answer] for answer in answers])
    encoded = ''
    for i in range(0, len(bit_string), 8):
        encoded_char = chr(int(bit_string[i:i+8], 2))
        encoded += encoded_char
    return encoded

def decode_answers(encoded):
    reverse_multipleChoice = {'00': 'A', '01': 'B', '10': 'C', '11': 'D'}
    bit_string = ''.join([format(ord(char), '08b') for char in encoded])
    answers = ''
    for i in range(0, len(bit_string), 2):
        answers += reverse_multipleChoice[bit_string[i:i+2]]
    return answers


original_answers = 'ABCDCDCDBAACBDDBCACBADBCBDABCDBACCBDDABC'
encoded = encode_answers(original_answers)
decoded = decode_answers(encoded)

print(f"Original: {original_answers}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
