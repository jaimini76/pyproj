import logging

def palindrome(s):

    low = 0
    high = len(s) - 1

    while ( high > low):
        if s[high] != s[low]:
            logging.info(f"String : {s} is not palindrome")
            return
        high -= 1
        low += 1

    logging.info(f"String : {s} is palindrome")


s1 = "ABCDCBA"
s2 = "ABDBA"
s3 = "ABDJBA"

logging.getLogger().setLevel(logging.INFO)
palindrome(s1)
palindrome(s2)
palindrome(s3)