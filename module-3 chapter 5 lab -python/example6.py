# 6. Replace All Occurrences of a Substring
def replace_substring(s, old, new):
    return s.replace(old, new)

# Example usage
input_string = "Hello, World! Hello, everyone!"
print(replace_substring(input_string, "Hello", "Hi"))  # Output: "Hi, World! Hi, everyone!"