class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.first = {}
        self.follow = {}
        self.predict = {}
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

    def calculate_predict(self):
        for lhs in self.productions:
            self.predict[lhs] = set()
            for production in self.productions[lhs]:
                if production == 'ε':
                    self.predict[lhs].update(self.follow[lhs])
                else:
                    first_set = set()
                    for char in production:
                        first_set.update(self.calculate_first(char))
                        if 'ε' not in self.first.get(char, set()):
                            break
                    self.predict[lhs].update(first_set)

    def eliminate_left_recursion(self):
        new_productions = {}
        for A, prods in self.productions.items():
            alpha = [p for p in prods if p[0] == A]  # Recursivas
            beta = [p for p in prods if p[0] != A]   # No recursivas

            if alpha:
                A_prime = A + "'"
                new_productions[A] = beta + [b + A_prime for b in beta]
                new_productions[A_prime] = [a[1:] + A_prime for a in alpha] + ['ε']
            else:
                new_productions[A] = prods
        
        self.productions = new_productions

    def factor_grammar(self):
        new_productions = {}
        for A, prods in self.productions.items():
            common_prefix = {}
            for production in prods:
                prefix = production[0]
                if prefix in common_prefix:
                    common_prefix[prefix].append(production)
                else:
                    common_prefix[prefix] = [production]
            
            for prefix, productions in common_prefix.items():
                if len(productions) > 1:
                    new_symbol = A + "_new"
                    new_productions[A] = [prefix + new_symbol]
                    new_productions[new_symbol] = [p[1:] for p in productions]
                else:
                    new_productions[A] = productions
        
        self.productions.update(new_productions)

    def transform_to_ll1(self):
        self.eliminate_left_recursion()
        self.factor_grammar()

    def calculate(self):
        for non_terminal in self.productions.keys():
            self.calculate_first(non_terminal)

        for non_terminal in self.productions.keys():
            self.calculate_follow(non_terminal)

        self.calculate_predict()

    def display(self):
        print("Producciones transformadas:")
        for key, value in self.productions.items():
            print(f"{key} -> {value}")
        
        print("\nFIRST sets:")
        for key in self.first:
            print(f"FIRST({key}) = {self.first[key]}")

        print("\nFOLLOW sets:")
        for key in self.follow:
            print(f"FOLLOW({key}) = {self.follow[key]}")

        print("\nPREDICT sets:")
        for key in self.predict:
            print(f"PREDICT({key}) = {self.predict[key]}")

# Definición de la gramática
productions = {
    'S': ['Sa', 'b'],
    'A': ['ε', 'a'],
    'B': ['b']
}

grammar = Grammar(productions)
grammar.transform_to_ll1()
grammar.calculate()
grammar.display()
