'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    '''
    方法一：核心：找到重复字符的位置，然后从重复字符开始往后继续找，比较找到的这些子串中最长的那个
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxString = ''
        maxLength = 0
        for i in range(len(s)):
            flag = s[i] in maxString
            maxString += s[i]

            if flag:
                lastMatchedIndex = s[0:i].rfind(s[i])
                maxString = s[i-1] if s[i-1] == s[i] else s[lastMatchedIndex+1:i+1]
            
            if len(maxString) > maxLength:
                maxLength = len(maxString)
        return maxLength

    '''
    方法二：核心思想和方法一相同，只是方法一通过索引查找，方法二通过while循环逐个遍历对比，这种方法的速度比方法一快，可能是方法一使用rfind，影响了效率。
    '''
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        track = ""
        for char in s:
            if char in track:
                while True:
                    if track[0] == char:
                        track = track[1:]
                        track += char
                        break
                    else:
                        track = track[1:]
            else:
                track += char
            if len(track) > output:
                output = len(track)
        return output

solution = Solution()
str = 'abcdgrmklgregvsdlkhsdkfja,.#@%#^I&*'
print(solution.lengthOfLongestSubstring2(str))