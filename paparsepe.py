input_string = input("Enter string: ")

def paparsepe(input_string):
    prev_letter = ""
    output_string = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in input_string:
        output_string += letter
        if letter in vowels and letter != prev_letter:
            output_string += ("p" + letter)
        prev_letter = letter
    return output_string

print(paparsepe(input_string))