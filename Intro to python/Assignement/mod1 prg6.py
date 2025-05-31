def replace_not_poor(sentence):
    not_index = sentence.find('not')
    poor_index = sentence.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        result = sentence[:not_index] + 'good' + sentence[poor_index + 4:]
    else:
        result = sentence

    return result

text = input("Enter a sentence: ")

print("Result:", replace_not_poor(text))