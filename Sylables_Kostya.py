 VOWELS = ('а', 'о', 'у', 'е', 'и', 'і', 'я', 'ю', 'є', 'ї')
 PunctSymb = (',', '.', '!', '?', ' ')
 Devider = "-"

 def isVowels (symbol):
    if symbol in VOWELS:
        return True
    else:
        return False

def isConsonant (symbol):
    if symbol not in isVowels (symbol):
        return True
    else:
        return False

def isLastSymbolInWord (symbol, next_symbol):
    if symbol == None or symbol in PunctSymb:
        return True
    else
        return False

def symbol ()
    if i < len(text):
        return symbol(i)
    else:
        return None


def sylables (text):
    result = ' '
    for i, symbol in enumerate (text):
        result += symbol
        current_symbol = symbol.lower()
        next_symbol = text[i+1]
        very_next_symbol = text[i+2]

        if isVowels (current_symbol):
            if not (isConsonant (next_symbol)) and isLastSymbolInWord (very_next_symbol):
                if not isLastSymbolInWord (next_symbol):
                    result += "-"
    return result