def print_alphabets(indices):
    alphabets = ''
    for index in indices:
        letter = chr(index + 96)
        alphabets += letter
    return alphabets

# Example usage
indices = [16, 9, 3, 15, 3, 20, 6, 20,8,5,14,21,13,2,5,18,19,13,1,19,15,14] # Corresponds to letters 'a', 'b', 'c', 'd', 'e'
alphabets =  print_alphabets(indices)
print(alphabets)
