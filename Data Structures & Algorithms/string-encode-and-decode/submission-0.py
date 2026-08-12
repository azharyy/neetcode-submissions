class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded+=str(len(s))+"#"+s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i <len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            content = s[j+1:length+j+1]
            result.append(content)
            i = j + length +1
        return result