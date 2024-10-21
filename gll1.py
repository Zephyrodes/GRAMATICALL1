class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.first = {}
        self.follow = {}
        self.start_symbol = list(productions.keys())[0]

    def calculate_first(self, symbol):
        if symbol in self.first:
            return self.first[symbol]
        
        first_set = set()
        productions = self.productions.get(symbol, [])

        for production in productions:
            if production == 'ε':
                first_set.add('ε')
            else:
                for char in production:
                    if char.islower():  # Terminal
                        first_set.add(char)
                        break
                    else:  # No terminal
                        first_set.update(self.calculate_first(char))
                        if 'ε' not in self.first.get(char, set()):
                            break
                else:
                    first_set.add('ε')

        self.first[symbol] = first_set
        return first_set

    def calculate_follow(self, symbol):
        if symbol in self.follow:
            return self.follow[symbol]
        
        follow_set = set()
        if symbol == self.start_symbol:
            follow_set.add('$')
        
        for lhs, productions in self.productions.items():
            for production in productions:
                if symbol in production:
                    index = production.index(symbol)
                    if index + 1 < len(production):
                        next_symbol = production[index + 1]
                        follow_set.update(self.calculate_first(next_symbol) - {'ε'})
                        if 'ε' in self.calculate_first(next_symbol):
                            follow_set.update(self.calculate_follow(lhs))
                    else:
                        follow_set.update(self.calculate_follow(lhs))
        
        self.follow[symbol] = follow_set
        return follow_set

    def calculate(self):
        for non_terminal in self.productions.keys():
            self.calculate_first(non_terminal)

        for non_terminal in self.productions.keys():
            self.calculate_follow(non_terminal)

    def display(self):
        print("FIRST sets:")
        for key in self.first:
            print(f"FIRST({key}) = {self.first[key]}")

        print("\nFOLLOW sets:")
        for key in self.follow:
            print(f"FOLLOW({key}) = {self.follow[key]}")

# Definición de la gramática
productions = {
    'S': ['AB', 'a'],
    'A': ['ε', 'a'],
    'B': ['b']
}

grammar = Grammar(productions)
grammar.calculate()
grammar.display()
