def reversed_string(string):
    words = string.strip().split()
    reversed_words = words[::-1]

    return " ".join(reversed_words)

string = "the sky is blue"
print(reversed_string(string))
