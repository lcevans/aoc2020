with open('input.txt') as f:
    rules, messages = f.read().split('\n\n')
    messages = messages.split('\n')
    rules = {rule.split(': ')[0]: rule.split(': ')[1]  for rule in rules.split('\n')}

# PART 1

# Memoize for great speed!
import functools
@functools.lru_cache(maxsize=None)
def matches(message, rule):
    if rule == '"a"':
        return message == "a"
    elif rule == '"b"':
        return message == "b"
    elif ' | ' in rule:
        rule1, rule2 = rule.split(' | ')
        return matches(message, rule1) or matches(message, rule2)
    elif ' ' in rule:
        rule1, rule2 = rule.split(' ', 1)
        for i in range(1, len(message)):
            if matches(message[0:i], rule1) and matches(message[i:], rule2):
                return True
        return False
    else: # number
        rule = rules[rule]
        return matches(message, rule)

print(sum(1 for message in messages if matches(message, rules['0'])))


# PART 2

## RULES CHANGES
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

# Memoize for great speed!
import functools
@functools.lru_cache(maxsize=None)
def matches(message, rule):
    if rule == '"a"':
        return message == "a"
    elif rule == '"b"':
        return message == "b"
    elif ' | ' in rule:
        rule1, rule2 = rule.split(' | ')
        return matches(message, rule1) or matches(message, rule2)
    elif ' ' in rule:
        rule1, rule2 = rule.split(' ', 1)
        for i in range(1, len(message)):
            if matches(message[0:i], rule1) and matches(message[i:], rule2):
                return True
        return False
    else: # number
        rule = rules[rule]
        return matches(message, rule)

print(sum(1 for message in messages if matches(message, rules['0'])))
