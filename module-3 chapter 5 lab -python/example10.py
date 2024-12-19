# 10. Remove Whitespace from a String
def remove_whitespace(s):
    return ''.join(s.split())

# Example usage
input_string = " Hello, World! "
print(remove_whitespace(input_string))  # Output: "Hello,World!"