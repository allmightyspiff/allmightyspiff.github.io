import random

class deck():
    def __init__(self):
        cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suites = ['H','S','C','D']
        self.deck = []
        for s in suites:
            for c in cards:
                self.deck.append(s + c)
    
    def __str__(self):
        string = ','.join(self.deck)
        return string

    def shuffle(self):
        random.seed()
        new_deck = [0 for i in range(52)]
        positions_checked = 0
        for card in self.deck:
            position = random.randint(0,51) 
            while new_deck[position] != 0:
                position = position + 1
                positions_checked = positions_checked + 1
                if position > 51:
                    position = 0
            new_deck[position] = card
        print("Checked %s positions" % positions_checked)
        self.deck = new_deck

    def shuffleFY(self):
        """Fisher Yates shuffle"""
        random.seed()
        new_deck = []
        cardsLeft = len(self.deck)
        while cardsLeft > 0:
            card = self.deck.pop(random.randint(0,cardsLeft - 1))
            new_deck.append(card)
            cardsLeft = len(self.deck)
        self.deck = new_deck

if __name__ == "__main__":
    deck = deck()
    print(deck)
    deck.shuffleFY()
    print(deck)