import random


@staticmethod
def deck_generator():
    stick = ["C", "D", "T", "P"]
    values = ["A"] + [v for v in range(2, 11)] + ["J", "Q", "K"]
    deck = [(values, stick) for stick in stick for value in values]
    return deck


@staticmethod
def mix_deck():
    deck = deck_generator()
    random.shuffle(deck)
    return deck


@staticmethod
def get_value_of_the_hand(cards):
    value = 0
    ace = False
    for card in cards:
        value_of_card = card[0]
        if value_of_card in ("J", "Q", "K"):
            value += 10
        elif value_of_card == "A":
            ace = True
            value += 1
        else:
            value += value_of_card

    if ace and (value + 10) <= 21:
        value += 10

    return value


@staticmethod
def boolean_compare_two_hands(hand_1, hand_2):
    if len(hand_1) == len(hand_2):
        comparator_counter = 0
        for i in range(len(hand_2)):
            for j in range(len(hand_1)):
                if hand_1[i] == hand_2[j]:
                    comparator_counter += 1

        if comparator_counter == len(hand_1):
            return True
        else:
            return False
    else:
        return False


@staticmethod
def compare_value_between_two_hands(hand_1, hand_2):
    if get_value_of_the_hand(hand_1) == get_value_of_the_hand(hand_2):
        print("The hands have the same value.")
    else:
        print("The hands doesn't have the same value.")


@staticmethod
def valor_mano_poker(cards):
    value_array = []
    poker = 0
    for i in range(5):
        if cards in ("J", "Q", "K"):
            value_array.append(10)
        elif cards == "A":
            value_array.append(True)
        else:
            value_array.append(cards[i][0])

    for i in range(5):
        for j in range(5):
            if value_array[i] == value_array[j]:
                poker += 1

    if poker == 2:
        print("2 es un par")
        return 2
    elif poker == 3:
        print("3 es un trio")
        return 3
    elif poker == 4:
        print("4 es un poker")
        return 4
    elif poker == 5:
        print("5 es un full")
        return 5
    else:
        print("0")
        return 0
