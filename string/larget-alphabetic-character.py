# https://www.geeksforgeeks.org/find-the-largest-alphabetic-character-present-in-the-string/
# microsoft codility
"""
Given a string str, our task is to find the Largest Alphabetic Character, whose both uppercase and lowercase are present in the string.
The uppercase character should be returned. If there is no such character then return -1 otherwise print the uppercase letter of the character.
"""

# Time Complexity: O(N)
# Space Complexity: O(1)
def largest_alphabetic_charcater(text: str) -> chr:
    text = list(text)
    lower = [False]*27
    upper = [False]*27

    a = ord('a')
    A = ord('A')
    for index, ch in enumerate(text):
        if ch.islower(): lower[ord(ch)-a] = True  # we can make the complexity of this step to O(1) by storing the numerical value of characters in dict
        else: upper[ord(ch)-A]  = True

    for index in range(26,-1,-1):
        if lower[index] and upper[index]:
            return chr(index + ord("A"))
    return -1

if __name__ == '__main__':
    text = "admeDCAB"
    #text = "dAeB"
    ch = largest_alphabetic_charcater(text)
    print(ch)
