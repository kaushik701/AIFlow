# aiflow/parser.py
class ASTNode:
    pass

class ConditionNode(ASTNode):
    def __init__(self, condition, true_step, false_step=None):
        self.condition = condition
        self.true_step = true_step
        self.false_step = false_step

class WorkflowNode(ASTNode):
    def __init__(self, name, input_type, steps, return_var):
        self.name = name
        self.input_type = input_type
        self.steps = steps
        self.return_var = return_var

class StepNode(ASTNode):
    def __init__(self, name, model, prompt, output):
        self.name = name
        self.model = model
        self.prompt = prompt
        self.output = output

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None
        
    def advance(self):
        """Move to the next token."""
        self.pos += 1
        if self.pos >= len(self.tokens):
            self.current_token = None
        else:
            self.current_token = self.tokens[self.pos]
            
    def eat(self, token_type):
        """Consume the current token if it matches the expected type."""
        if self.current_token.type == token_type:
            token = self.current_token
            self.advance()
            return token
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.type}")
            
    def parse_workflow(self):
        """Parse a workflow definition."""
        self.eat('KEYWORD')  # 'workflow'
        name = self.eat('IDENTIFIER').value
        self.eat('SPECIAL')  # '{'
        
        # Parse input
        self.eat('KEYWORD')  # 'input'
        self.eat('SPECIAL')  # ':'
        input_type = self.eat('IDENTIFIER').value
        self.eat('SPECIAL')  # ';'
        
        # Parse steps
        steps = []
        while self.current_token is not None and (
            (self.current_token.type == 'KEYWORD' and self.current_token.value == 'step') or
            (self.current_token.type == 'KEYWORD' and self.current_token.value == 'if')
        ):
            if self.current_token.value == 'step':
                steps.append(self.parse_step())
            elif self.current_token.value == 'if':
                steps.append(self.parse_condition())
            
        # Parse return
        self.eat('KEYWORD')  # 'return'
        self.eat('SPECIAL')  # ':'
        return_var = self.eat('IDENTIFIER').value
        self.eat('SPECIAL')  # ';'
        
        self.eat('SPECIAL')  # '}'
        
        return WorkflowNode(name, input_type, steps, return_var)
    
    def parse_step(self):
        """Parse a step definition."""
        self.eat('KEYWORD')  # 'step'
        name = self.eat('IDENTIFIER').value
        self.eat('SPECIAL')  # '{'
        
        # Parse model
        self.eat('KEYWORD')  # 'model'
        self.eat('SPECIAL')  # ':'
        model = self.eat('STRING').value
        self.eat('SPECIAL')  # ';'
        
        # Parse prompt
        self.eat('KEYWORD')  # 'prompt'
        self.eat('SPECIAL')  # ':'
        prompt = self.eat('STRING').value
        self.eat('SPECIAL')  # ';'
        
        # Parse output
        self.eat('KEYWORD')  # 'output'
        self.eat('SPECIAL')  # ':'
        output = self.eat('IDENTIFIER').value
        self.eat('SPECIAL')  # ';'
        
        self.eat('SPECIAL')  # '}'
        
        return StepNode(name, model, prompt, output)
    
    def parse_condition(self):
        """Parse a conditional statement."""
        self.eat('KEYWORD')  # 'if'
        self.eat('SPECIAL')  # '('
        
        # Parse condition - this needs to handle conditions like 'exists:analysis'
        condition_str = ""
        
        # Keep consuming tokens until we hit the closing parenthesis
        while self.current_token is not None and (self.current_token.type != 'SPECIAL' or self.current_token.value != ')'):
            if self.current_token.type == 'IDENTIFIER':
                condition_str += self.current_token.value
            elif self.current_token.type == 'SPECIAL' and self.current_token.value == ':':
                condition_str += ':'
            self.advance()
        
        if not condition_str:
            raise Exception("Empty condition in if statement")
        
        self.eat('SPECIAL')  # ')'
        self.eat('SPECIAL')  # '{'
        
        # Parse true branch
        true_step = self.parse_step()
        
        self.eat('SPECIAL')  # '}'
        
        # Check if there's an else branch
        false_step = None
        if self.current_token is not None and self.current_token.type == 'KEYWORD' and self.current_token.value == 'else':
            self.eat('KEYWORD')  # 'else'
            self.eat('SPECIAL')  # '{'
            false_step = self.parse_step()
            self.eat('SPECIAL')  # '}'
        
        return ConditionNode(condition_str, true_step, false_step)
    
    def parse(self):
        """Parse the tokens into an AST."""
        return self.parse_workflow()