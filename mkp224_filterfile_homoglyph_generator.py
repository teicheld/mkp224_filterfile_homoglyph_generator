import sys

def generate_homoglyphs(word):
    homoglyphs = {
        'a': ['4'],
        'e': ['3'],
        's': ['5'],
        't': ['7'],
        'z': ['2'],
        'p': ['q'],
        'q': ['p'],
    }
    
    variations = [list(word)]
    
    for char in word:
        if char.lower() in homoglyphs:
            new_variations = []
            for glyph in homoglyphs[char.lower()]:
                for variation in variations:
                    new_variation = variation.copy()
                    new_variation[new_variation.index(char)] = glyph
                    new_variations.append(new_variation)
            variations.extend(new_variations)
    
    homoglyph_words = [''.join(variation) for variation in variations]
    return homoglyph_words

arguments = sys.argv[1:]

for input_word in arguments:
    homoglyphs = generate_homoglyphs(input_word)

    for homoglyph in homoglyphs:
        print(homoglyph)
