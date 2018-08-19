class Codec:
    table = {}
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    url = 'https://short.it/'
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        key = ''
        while not key or key in self.table:
            temp = ''
            for i in range(6):
                temp += self.chars[random.randint(0, 61)]
            key = temp
        self.table[key] = longUrl
        return self.url + key
            

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[-6:]
        return self.table[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))