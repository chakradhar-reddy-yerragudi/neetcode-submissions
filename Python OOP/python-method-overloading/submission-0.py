class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self,s1:str,s2:str=''):
        if s2=='':
            return s1.upper()
        return s1+s2




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
