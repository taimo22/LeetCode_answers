#648. Replace Words
#https://leetcode.com/problems/replace-words/submissions/
#my ans(passed)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        sentence = sentence.split(" ")
        for i in range(len(sentence)):

            for s in dictionary:
                if len(sentence[i]) < len(s):
                    continue

                if sentence[i][:len(s)] == s:
                    sentence[i] = s

        return " ".join(sentence)

