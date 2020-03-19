#problem 271 / encode and decode strings
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for s in strs:
            res += self.len_to_str(s)
            res += s.encode('utf-8')
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i,n = 0, len(s)
        res = []
        while i < n:
            length = self.str_to_int(s[i:i+4])
            i += 4
            res.append(s[i:i+length])
            i += length
        return res
        
    def len_to_str(self,x):
        n = len(x)
        bytes = [chr(n>>(i*8)) for i in range(4)]
        bytes.reverse()
        return ''.join(bytes)
    
    def str_to_int(self,x):
        res = 0
        for ch in x:
            res = res*256+ord(ch)
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))