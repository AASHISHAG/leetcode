# https://leetcode.com/discuss/interview-question/928806/
# microsoft codility

"""
Given a pattern as the first argument and a string of blobs split by | show the number of times the pattern is present in each blob and the total number of matches.

Input:
The input consists of the pattern (“bc” in the example) which is separated by a semicolon followed by a list of blobs (“bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32” 
in the example). Example input: bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32

Output:
The output should consist of the number of occurrences of the pattern per blob (separated by |). Additionally, the final entry should be the summation of all the occurrences
(also separated by |).

Example output: 3|2|1|2|8 where ‘bc’ was repeated 3 times, 2 times, 1 time, 2 times in the 4 blobs passed in. And 8 is the summation of all the occurrences (3+2+1+2 = 8)
"""

# Time Complexity: O(N)
# Space Complexity: O(1)
def count_substring(substring, text):
    count = 0
    txt_lgt, sub_lgt = len(text), len(substring)
    for index in range(0, txt_lgt - sub_lgt + 1):
        if substring == text[index:sub_lgt+index]: count += 1
    return count

if __name__ == '__main__':
    text = "bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32" # 3|2|1|2|8
    text = "aa;aaaakjlhaa|aaadsaaa|easaaad|sa" # 4|4|2|0|10
    text = "b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32" # 4|2|3|2|11
    text = ";bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32" # 0|0|0|0|0
    substring = text.split(";")[0]
    count = 0
    sm = 0
    output = []
    for target in text.split(";")[1].split("|"):
        count = 0 if substring == "" else count_substring(substring, target)
        sm += count
        output.append(str(count))
    output.append(str(sm))
    output = "|".join(output)

    print(output)
    
