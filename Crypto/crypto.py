import base64
import binascii

# Problem 1: Convert hex to base64 and back
def hex_to_base64(hex_str):
    bytes_data = bytes.fromhex(hex_str)
    base64_str = base64.b64encode(bytes_data).decode('utf-8')
    return base64_str

def base64_to_hex(base64_str):
    bytes_data = base64.b64decode(base64_str)
    hex_str = bytes_data.hex()
    return hex_str

# Problem 2: Fixed XOR
def fixed_xor(hex_str1, hex_str2):
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)
    xor_result = bytes(a ^ b for a, b in zip(bytes1, bytes2))
    return xor_result.hex()

# Problem 3: Single-character XOR Cipher
def single_char_xor_cipher(hex_str):
    bytes_data = bytes.fromhex(hex_str)
    best_score = None
    best_result = None
    best_key = None

    for key in range(256):
        decoded = ''.join(chr(b ^ key) for b in bytes_data)
        score = score_text(decoded)
        if best_score is None or score > best_score:
            best_score = score
            best_result = decoded
            best_key = key

    return best_key, best_result

def score_text(text):
    # Simple scoring based on character frequency in English
    frequency = {
        'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881,
        'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
        'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563,
        's': 0.0515760, 't': 0.0729357, 'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
        'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    return sum(frequency.get(char, 0) for char in text.lower())

# Example usage
if __name__ == "__main__":
    # Problem 1
    with open('hex_input.txt', 'r') as file:
        hex_str = file.read().strip()
    base64_str = hex_to_base64(hex_str)
    with open('base64_output.txt', 'w') as file:
        file.write(base64_str)
    with open('hex_output.txt', 'w') as file:
        file.write(base64_to_hex(base64_str))

    # Problem 2
    with open('xor_input1.txt', 'r') as file:
        hex_str1 = file.read().strip()
    with open('xor_input2.txt', 'r') as file:
        hex_str2 = file.read().strip()
    xor_result = fixed_xor(hex_str1, hex_str2)
    with open('xor_output.txt', 'w') as file:
        file.write(xor_result)

    # Problem 3
    with open('single_char_xor_input.txt', 'r') as file:
        hex_str = file.read().strip()
    key, message = single_char_xor_cipher(hex_str)
    with open('single_char_xor_output.txt', 'w') as file:
        file.write(f"Key: {key}\nMessage: {message}")
