# aiflow/lexer.py
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        
        # Define token types
        self.KEYWORDS = ['workflow', 'input', 'step', 'model', 'prompt', 'output', 'return', 'if', 'else']
        self.SPECIAL_CHARS = ['{', '}', ':', ';', '.', '(', ')']
        
    def advance(self):
        """Move to the next character in the input."""
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
            
    def skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
            
    def get_identifier(self):
        """Get an identifier or keyword."""
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
            
        if result in self.KEYWORDS:
            return Token('KEYWORD', result)
        return Token('IDENTIFIER', result)
    
    def get_string(self):
        """Get a string literal."""
        result = ''
        # Skip the opening quote
        self.advance()
        
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
            
        # Skip the closing quote
        if self.current_char == '"':
            self.advance()
            
        return Token('STRING', result)
    
    def tokenize(self):
        """Convert the input text into a list of tokens."""
        tokens = []
        
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
                
            if self.current_char.isalpha() or self.current_char == '_':
                tokens.append(self.get_identifier())
                continue
                
            if self.current_char == '"':
                tokens.append(self.get_string())
                continue
                
            if self.current_char in self.SPECIAL_CHARS:
                tokens.append(Token('SPECIAL', self.current_char))
                self.advance()
                continue
                
            # Handle template variables {{var}}
            if self.current_char == '{' and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '{':
                var_name = ''
                self.advance()  # Skip first {
                self.advance()  # Skip second {
                
                while self.current_char is not None and self.current_char != '}':
                    var_name += self.current_char
                    self.advance()
                    
                if self.current_char == '}' and self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '}':
                    self.advance()  # Skip first }
                    self.advance()  # Skip second }
                    tokens.append(Token('TEMPLATE_VAR', var_name.strip()))
                    continue
            
            # If we get here, we have an unrecognized character
            raise Exception(f"Invalid character: {self.current_char}")
            
        return tokens