class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


def tok_to_str(tokens):
    tok_str = ''

    if(tokens != None):
        for tok in tokens:
            if tok.value:
                tok_str += f'{tok.type: >20}    {tok.value}\n'
            else:
                tok_str += f'{str(tok.type): >20}    {tok.type}\n'

    return tok_str

def print_tokens(fn, tokens):
    text = ''
    text += (f'{"File name:": >20}    {fn}\n')
    text += (f'{"TOKENS": >20}    LEXEMES\n')
    text += ('----------------------------------------\n')
    text += (tok_to_str(tokens))

    return text

def output_to_symbolTable(tokens):
    filename = 'symbolTable.txt'

    with open(filename, "w") as f:
        f.write(f'{"File name:": >20}    {filename}\n')
        f.write(f'{"TOKENS": >20}    LEXEMES\n')
        f.write('----------------------------------------\n')
        f.write(tok_to_str(tokens))