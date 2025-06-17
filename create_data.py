import random
import csv


class Player:
    def __init__(self, cards):
        self.cards = cards
        self.discard_pile = []
        self.active_cards = []
        self.sum_of_starting_hand = sum(cards)

    def draw_cards(self, count):
        # Ensures the player has enough cards reshuffles if needed and draws the right amount of cards
        total_available = len(self.cards) + len(self.discard_pile)
        if total_available < count:
            return False  # Not enough cards to continue

        # Reshuffle if needed
        if len(self.cards) < count:
            self.cards += self.discard_pile
            random.shuffle(self.cards)
            self.discard_pile = []

        # Play card from the top
        self.active_cards += self.cards[:count]
        self.cards = self.cards[count:]
        return True

    def play_turn(self, war=False):
        return self.draw_cards(4 if war else 1)

    def collect_cards(self, cards):
        self.discard_pile += cards

    def total_cards(self):
        return len(self.cards) + len(self.discard_pile)


class Game:
    def __init__(self):
        # Create and shuffle the deck (0–12 repeated 4 times)
        self.deck = [rank for rank in range(13) for _ in range(4)]
        random.shuffle(self.deck)

        # Distribute cards
        self.player1 = Player(self.deck[:26])
        self.player2 = Player(self.deck[26:])
        self.turns = 0
        self.numbers_of_wars = 0
        self.longest_war = 0

        # Get the highest starting hand
        self.starting_hand_difference = self.player1.sum_of_starting_hand - self.player2.sum_of_starting_hand

    def play_game(self):
        while True:
            self.turns += 1

            if not self.player1.play_turn():
                return self.turns, self.numbers_of_wars, self.longest_war, 2, self.starting_hand_difference
            if not self.player2.play_turn():
                return self.turns, self.numbers_of_wars, self.longest_war, 1, self.starting_hand_difference

            result = self.resolve_battle()
            if result is not None:
                return self.turns, self.numbers_of_wars, self.longest_war, result[1], self.starting_hand_difference

    def resolve_battle(self):
        current_war_chain = 0
        while True:
            # Checks top card for each player
            card1 = self.player1.active_cards[-1]
            card2 = self.player2.active_cards[-1]

            if card1 > card2:
                self.player1.collect_cards(self.player1.active_cards + self.player2.active_cards)
                break
            elif card1 < card2:
                self.player2.collect_cards(self.player1.active_cards + self.player2.active_cards)
                break
            else:
                self.numbers_of_wars += 1
                current_war_chain += 1

                if not self.player1.play_turn(war=True):
                    return self.turns, 2
                if not self.player2.play_turn(war=True):
                    return self.turns, 1

        self.player1.active_cards.clear()
        self.player2.active_cards.clear()

        self.longest_war = max(self.longest_war, current_war_chain)

        return None


if __name__ == "__main__":
    data = []
    for i in range(100000000):
        if i % 10000 == 0:
            print(i)
        game = Game()
        result = game.play_game()
        data.append(result)

    data.sort(key=lambda x: x[0])

    with open('data2.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Turns", "Wars", "Longest War", "Winner", "Starting Hand Difference"])
        csvwriter.writerows(data)

