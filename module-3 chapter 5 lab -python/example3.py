# Program 3: Check if a String is a Palindrome
def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Example usage
input_string = "A man, a plan, a canal: Panama"
print(is_palindrome(input_string))