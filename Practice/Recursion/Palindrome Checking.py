def is_palindrome(string):
   """
   Return True if input is palindrome, False otherwise.

   Args:
    input(str): input to be checked if it is palindrome
   """
   if len(string) <= 1:
      return True
   if string[0] != string[-1]:
      return False
   return is_palindrome(string[1:-1])


if __name__ == '__main__':
   # Test Cases

   print(is_palindrome('madam')) # True
   print(is_palindrome('cbc')) # True
   print(is_palindrome('')) # True
   print(is_palindrome('abbba')) # True
   print(is_palindrome('a')) # True
   print(is_palindrome('Hello')) # False