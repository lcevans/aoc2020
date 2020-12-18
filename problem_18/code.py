# This was very adhoc... avert your eyes lest ye be blinded

equations = []
with open('input.txt') as f:
    for line in f:
        equations.append(line.strip())


def tokenize(eqn):
    tokens = []
    i = 0
    while i < len(eqn):
        if 48 <= ord(eqn[i]) <= 57: # numeral
            start = i
            while i < len(eqn) and 48 <= ord(eqn[i]) <= 57:
                i += 1
            tokens.append(int(eqn[start:i]))
            continue
        elif eqn[i] == ' ':
            i += 1
            continue
        else:
            tokens.append(eqn[i])
            i += 1
            continue
    return tokens

# PART 1

def evaluate(tokens):
    total = 0
    op = None
    val = None
    i = 0
    while i < len(tokens):
        if tokens[i] == '(':
            # Find matching parenthesis
            start = i
            extra = 1
            while i < len(tokens) and extra > 0:
                i += 1
                if tokens[i] == '(':
                    extra += 1
                elif tokens[i] == ')':
                    extra -= 1
            # print("Evaluating: ", tokens[start+1:i])
            val = evaluate(tokens[start+1: i])
        elif isinstance(tokens[i], int):
            val = tokens[i]
        else:
            op = tokens[i]
        i += 1

        # Reduce
        if op is not None and val is not None:
            if op == '+':
                total += val
            elif op == '-':
                total -= val
            elif op == '*':
                total *= val
            elif op == '/':
                total /= val
            else:
                print(op)
                assert False
            op = None
            val = None
        elif op is None and val is not None:
            total = val
            val = None
    # print("Returning: ", total)
    return total

print(sum(evaluate(tokenize(eqn)) for eqn in equations))


# PART 2

def evaluate(tokens):
    total = 0
    op = None
    val = None
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            return total * evaluate(tokens[i+1:])
        elif tokens[i] == '(':
            # Find matching parenthesis
            start = i
            extra = 1
            while i < len(tokens) and extra > 0:
                i += 1
                if tokens[i] == '(':
                    extra += 1
                elif tokens[i] == ')':
                    extra -= 1
            # print("Evaluating: ", tokens[start+1:i])
            val = evaluate(tokens[start+1: i])
        elif isinstance(tokens[i], int):
            val = tokens[i]
        else:
            op = tokens[i]
        i += 1

        # Reduce
        if op is not None and val is not None:
            if op == '+':
                total += val
            else:
                print(op)
                assert False
            op = None
            val = None
        elif op is None and val is not None:
            total = val
            val = None
    # print("Returning: ", total)
    return total
evaluate(tokenize('1 + 2 * 3 + 4 * 5 + 6'))

print(sum(evaluate(tokenize(eqn)) for eqn in equations))
