import random

class Card:
    SUITS = ["diamond", "heart", "club", "spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __gt__(self, other):
        return (self.rank, self.suit) > (other.rank, other.suit)

    def __str__(self):
        return "{} of {}".format(Card.RANKS[self.rank], Card.SUITS[self.suit])


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        st = ""
        for c in self.cards:
            st += str(c) + "\n"
        return st

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self):
        return self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)

    @staticmethod
    def get_wincard(cards):
        winner = cards[0]
        for c in cards[1:]:
            # if (winner.rank, winner.suit) < (c.rank, c.suit):
            if winner < c:
                winner = c
        return winner


class Hand(Deck):
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.win = 0
        self.committed = 0


    def winner(self):
        self.win += 1

    def __lt__(self, other):
        return self.win < other.win


def play():
    deck = Deck()
    deck.shuffle()
    print(deck.cards[0]<deck.cards[1])
    print("After Shuffle", deck)

    # c1 = deck.cards[0]
    # c2 = deck.cards[1]
    # print(c1,"<", c2, "=",  c1<c2)

    hands = []
    for i in range(1, 5):
        hand = Hand("Player %d" % i)
        hands.append(hand)

    while len(deck.cards) > 0:
        for hand in hands:
            card = deck.remove_card()
            hand.add_card(card)

    for hand in hands:
        print("Cards for", hand.name, "are", hand)

    for i in range(13):
        floors = []
        for hand in hands:
            floors.append(hand.remove_card())
        # win_card = max(floors)
        win_card = Deck.get_wincard(floors)
        win_index = floors.index(win_card)
        win_hand = hands[win_index]
        win_hand.winner()
        # hands[floors.index(deck.get_wincard(floors))].winner()
        for card in floors:
            print(card)
        print("Win card=", win_card, "win_index=", win_index, "Winner=", win_hand.name)
        input()

    print("Final score")
    hands = sorted(hands, reverse=True)
    # hands.sort(reverse=True)
    for hand in hands:
        print(hand.name, " = ", hand.win)


def main():
    choice = "y"
    while choice == "y":
        play()
        choice = input("Play again? (y/n) : ")
    print("See you again!")

if __name__ == '__main__':
    main()
