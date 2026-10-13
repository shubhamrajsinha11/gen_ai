class TextNormalization:
    def __init__(self,data):
        self.data=data
        self.start()
    def start(self):
        print('''
              1)converting strings to lower case
              2)removing punctuations
              3)removing spl chars
              4)handling emojis
              5)removing extra spaces
              6)contraction handling
              7)correcting the words
              ''')
        
    def lower_case(self,data):
        # converting the string to lower case
        self.data = self.data.lower()
    def removing_punctuations(self,data):
        chars=self.data
        # removing punctuations
        import string
        punctuations=string.punctuation
        for char in punctuations:
            chars=chars.replace(char,'')
        self.data = chars
        
    def removing_spl_chars(self,data):
        chars=self.data
        for char in chars:
            if not char.isalnum() and not ord(char) ==32:
                chars=chars.replace(char,'')
        self.data=chars

    def handling_emojis(self,data):
        # handling emojis
        import emoji
        self.data=emoji.demojize(self.data)
        
    def removing_extra_spaces(self,data):
        # removing extra spaces
        self.data=' '.join(self.data.split())
        
    def contraction_handling(self,data):
        # handling contractions
        import contractions
        self.data=contractions.fix(self.data)
        
    def correcting_words(self,data):
        # correcting the words
        from textblob import TextBlob
        self.data=str(TextBlob(self.data).correct())
        
obj=TextNormalization('corrting the wods for txt normalization')
obj.start()
obj.lower_case()
