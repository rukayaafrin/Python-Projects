"""
Project from codecademy.com
Caesar Cipher: The Project
Step 1: Code a message using the Caesar cipher with a shift/offset of 10.
Step 2: Decode a message using an offset of 10.
Step 3: Solve a Caesar cipher without knowing the shift/offset value.
"""

# Define global variables to avoid repeating code
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "


# Step 1: Code a message using the Caesar cipher with a shift/offset.
def coder(messages, offset):
    messages = messages.lower()
    coded_message = ""
    for letter in messages:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            coded_message += alphabet[(letter_value - offset) % 26]
        else:
            coded_message += letter
    return coded_message


# Test the function
print(coder("Hi Friend! How have you been?", 10))


# Step 2: Decode a message using an offset of 10.
def decoder(messages, offset):
    messages = messages.lower()
    decoded_message = ""
    for letter in messages:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            decoded_message += alphabet[(letter_value + offset) % 26]
        else:
            decoded_message += letter
    return decoded_message


# Test the function
print(decoder("xy vhyudt! xem xqlu oek ruud?", 10))


# Step 3: Solve a Caesar cipher without knowing the shift/offset value.
# Use brute force to generate 25 outcomes (26letters-1) and find the output which is in English

def brute_force(coded_message):
    for i in range(1, 26):
        print("SHIFT/OFFSET VALUE: " + str(i))
        print("\t " + decoder(coded_message, i) + "\n")


# Test the function
brute_force(
    " vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")
