# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/

# Time Complexity: O(N)
# Space Complexity: O(1)
def reverseWords(text):
	
	text = text.split('.')
	left, right = 0, len(text)-1
	
	while left < right:
		text[left], text[right] = text[right], text[left]
		left +=1
		right -=1
	return '.'.join(text)
	

if __name__ == '__main__':
    text1 = "i.like.this.program.very.much" # much.very.program.this.like.i
    text2 = "pqr.mno" # mno.pqr

    output1 = reverseWords(text1)
    output2 = reverseWords(text2)

    print(output1)
    print(output2)
