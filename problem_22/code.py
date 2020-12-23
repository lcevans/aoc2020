with open('input.txt') as f:
    player1, player2 = f.read().strip().split('\n\n')
    player1 = [int(c) for c in player1.split('\n')[1:]]
    player2 = [int(c) for c in player2.split('\n')[1:]]

# PART 1

while len(player1) > 0 and len(player2) > 0:
    c1 = player1.pop(0)
    c2 = player2.pop(0)
    if c1 > c2:
        player1.append(c1)
        player1.append(c2)
    else:
        player2.append(c2)
        player2.append(c1)

winner = player1 if len(player1) > 0 else player2

print(sum(c*(i+1) for i, c in enumerate(reversed(winner))))


# PART 2

# Reload b/c modified in PART 1
with open('input.txt') as f:
    player1, player2 = f.read().strip().split('\n\n')
    player1 = ','.join([c for c in player1.split('\n')[1:]])
    player2 = ','.join([c for c in player2.split('\n')[1:]])


# I misread the instructions => tried to use memoization to speed it up. After fixing the logic per the instructions
# I may not need the memoization but I kept it in
import functools
@functools.lru_cache(maxsize=None)
def play(deck1_str, deck2_str, is_main):
    # Returns winner and final decks
    deck1 = deck1_str.split(',')
    deck2 = deck2_str.split(',')
    seen = set()
    while True:
        id_str = f"{','.join(deck1)} {','.join(deck2)}"
        if is_main:
            print(len(seen))
        if id_str in seen:
            # Automatic Player 1 win
            return (1, None, None)
        seen.add(id_str)

        c1 = int(deck1.pop(0))
        c2 = int(deck2.pop(0))
        if len(deck1) >= c1 and len(deck2) >= c2:
            # Recurse!
            winner, _, _ = play(','.join(deck1[:c1]), ','.join(deck2[:c2]), False)
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            deck1.append(str(c1))
            deck1.append(str(c2))
        else:
            deck2.append(str(c2))
            deck2.append(str(c1))

        if len(deck1) == 0 or len(deck2) == 0:
            return (winner, deck1, deck2)

winner, final_deck1, final_deck2 = play(player1, player2, True)
winning_deck = final_deck1 if winner == 1 else final_deck2

print(sum(int(c)*(i+1) for i, c in enumerate(reversed(winning_deck))))
