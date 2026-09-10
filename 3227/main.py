""" pai taro """

card = input().strip()

rank_char = card[:-1].upper()
suit_char = card[-1].upper()

rank_dict = {
    'A': 'ace',
    'J': 'jack',
    'Q': 'queen',
    'K': 'king'
}

suit_dict = {
    'D': 'diamonds',
    'H': 'hearts',
    'S': 'spades',
    'C': 'clubs'
}

rank = rank_dict.get(rank_char, rank_char)
suit = suit_dict.get(suit_char, "")

print(f"{rank} of {suit}")
