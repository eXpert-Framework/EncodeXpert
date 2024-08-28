import tkinter as tk
from tkinter import ttk
import base64

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def encode_text():
    input_text = input_entry.get("1.0", tk.END).strip()
    method = encode_choice.get()
    
    if method == "Binary":
        encoded_text = binary_encode(input_text)
    elif method == "Hexadecimal":
        encoded_text = hexadecimal_encode(input_text)
    elif method == "ROT13":
        encoded_text = rot13_encode(input_text)
    elif method == "Morse":
        encoded_text = morse_encode(input_text)
    elif method == "Base64":
        encoded_text = base64_encode(input_text)
    elif method == "Caesar":
        encoded_text = caesar_encode(input_text)
    else:
        encoded_text = input_text.upper()  # Default to uppercase text
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, encoded_text)

def decode_text():
    input_text = decode_entry.get("1.0", tk.END).strip()
    method = decode_choice.get()
    
    if method == "Binary":
        decoded_text = binary_decode(input_text)
    elif method == "Hexadecimal":
        decoded_text = hexadecimal_decode(input_text)
    elif method == "ROT13":
        decoded_text = rot13_decode(input_text)
    elif method == "Morse":
        decoded_text = morse_decode(input_text)
    elif method == "Base64":
        decoded_text = base64_decode(input_text)
    elif method == "Caesar":
        decoded_text = caesar_decode(input_text)
    else:
        decoded_text = input_text.lower()  # Default to lowercase text
    
    decoded_text_widget.delete("1.0", tk.END)
    decoded_text_widget.insert(tk.END, decoded_text)

def binary_encode(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_decode(text):
    binary_list = text.split()
    decoded_text = ''.join(chr(int(binary, 2)) for binary in binary_list)
    return decoded_text

def hexadecimal_encode(text):
    return ' '.join(format(ord(char), '02X') for char in text)

def hexadecimal_decode(text):
    hex_list = text.split()
    decoded_text = ''.join(chr(int(hex, 16)) for hex in hex_list)
    return decoded_text

def rot13_encode(text):
    return ''.join(rot13_char(char) for char in text)

def rot13_char(char):
    if 'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
    else:
        return char

def rot13_decode(text):
    return ''.join(rot13_char(char) for char in text)

def morse_encode(text):
    text = text.upper()
    encoded_chars = []
    for char in text:
        if char == ' ':
            encoded_chars.append('/')
        elif char in MORSE_CODE_DICT:
            encoded_chars.append(MORSE_CODE_DICT[char])
        else:
            encoded_chars.append(char)
    return ' '.join(encoded_chars)

def morse_decode(text):
    decoded_chars = []
    for symbol in text.split():
        if symbol == '/':
            decoded_chars.append(' ')
        else:
            for key, value in MORSE_CODE_DICT.items():
                if value == symbol:
                    decoded_chars.append(key)
                    break
    return ''.join(decoded_chars)

def base64_encode(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')

def base64_decode(text):
    base64_bytes = text.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('utf-8')

def caesar_encode(text, shift=3):
    encoded_chars = []
    for char in text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A')) if char.isupper() else chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encoded_chars.append(shifted)
        else:
            encoded_chars.append(char)
    return ''.join(encoded_chars)

def caesar_decode(text, shift=3):
    decoded_chars = []
    for char in text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') - shift) % 26 + ord('A')) if char.isupper() else chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decoded_chars.append(shifted)
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)

# Create main window
root = tk.Tk()
root.title("EncodeXpert")

# Configure the main window's grid layout to be responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create notebook (tabbed view)
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")

# Encoding frame
encode_frame = ttk.Frame(notebook)
notebook.add(encode_frame, text="Encoding")

# Decoding frame
decode_frame = ttk.Frame(notebook)
notebook.add(decode_frame, text="Decoding")

# Make the frames fill the available space
encode_frame.columnconfigure(0, weight=1)
encode_frame.rowconfigure(5, weight=1)

decode_frame.columnconfigure(0, weight=1)
decode_frame.rowconfigure(5, weight=1)

# Encode frame contents
input_label = ttk.Label(encode_frame, text="Enter text to encode:")
input_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

input_entry = tk.Text(encode_frame, height=5, width=40)
input_entry.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

encode_choice = ttk.Combobox(encode_frame, values=["Binary", "Hexadecimal", "ROT13", "Morse", "Base64", "Caesar"])
encode_choice.grid(row=2, column=0, padx=10, pady=5, sticky="")
encode_choice.current(0)  # Set default selection

encode_button = ttk.Button(encode_frame, text="Encode", command=encode_text)
encode_button.grid(row=3, column=0, padx=10, pady=10, ipadx=20, sticky="")

result_label = ttk.Label(encode_frame, text="Encoded text:")
result_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

result_text = tk.Text(encode_frame, height=5, width=40)
result_text.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")

# Decoding frame contents
decode_label = ttk.Label(decode_frame, text="Enter text to decode:")
decode_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

decode_entry = tk.Text(decode_frame, height=5, width=40)
decode_entry.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

decode_choice = ttk.Combobox(decode_frame, values=["Binary", "Hexadecimal", "ROT13", "Morse", "Base64", "Caesar"])
decode_choice.grid(row=2, column=0, padx=10, pady=5, sticky="")
decode_choice.current(0)  # Set default selection

decode_button = ttk.Button(decode_frame, text="Decode", command=decode_text)
decode_button.grid(row=3, column=0, padx=10, pady=10, ipadx=20, sticky="")

decoded_label = ttk.Label(decode_frame, text="Decoded text:")
decoded_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

decoded_text_widget = tk.Text(decode_frame, height=5, width=40)
decoded_text_widget.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")

# Run the application
root.mainloop()
