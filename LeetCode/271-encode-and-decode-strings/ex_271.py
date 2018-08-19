class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = []
        for s in strs:
            chars = []
            for c in s:
                chars.append(str(ord(c)))
            encoded.append(' '.join(chars))
        return ','.join(encoded) if encoded else 'None'

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s == 'None':   return []
        strs = []
        decoded = s.split(',')
        for s in decoded:
            chars = s.split()
            char_list = []
            for c in chars:
                char_list.append(chr(int(c)))
            strs.append(''.join(char_list))
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))