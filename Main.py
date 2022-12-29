import functools

SUITS = {"黑桃": 4, "梅花": 3, "红桃": 2, "方块": 1}
NUMBERS = {"A": 1,
           "2": 2,
           "3": 3,
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7,
           "8": 8,
           "9": 9,
           "10": 10,
           "J": 11,
           "Q": 12,
           "K": 13}


def compare(card1, card2):
    if number(card2) != number(card1):
        return number(card1) - number(card2)
    return SUITS[suit(card1)] - SUITS[suit(card2)]


def suit(given_card):
    return given_card[0:2]


def number(given_card):
    return NUMBERS[given_card[2:]]


def find_target_card(first_card, second_card):
    small_card = ""
    large_card = ""
    if number(first_card) > number(second_card):
        small_card = second_card
        large_card = first_card
    else:
        small_card = first_card
        large_card = second_card
    # calculate the distance.
    first_distance = number(large_card) - number(small_card)
    if first_distance <= 6:
        return [first_distance, small_card]
    # if not the first distance, calculate the second distance.
    second_distance = number(small_card) + 13 - number(large_card)
    return [second_distance, large_card]


def sorting(number, all_cards):
    if number == 1:
        # small mid large
        return [all_cards[0], all_cards[1], all_cards[2]]
    elif number == 2:
        # small large mid
        return [all_cards[0], all_cards[2], all_cards[1]]
    elif number == 3:
        # mid small large
        return [all_cards[1], all_cards[0], all_cards[2]]
    elif number == 4:
        # mid large small
        return [all_cards[1], all_cards[2], all_cards[0]]
    elif number == 5:
        # large small mid
        return [all_cards[2], all_cards[0], all_cards[1]]
    elif number == 6:
        # large mid small
        return [all_cards[2], all_cards[1], all_cards[0]]


def find_target(all_cards):
    all_suits = []
    for outer_loop_card in all_cards:
        # if there is, find target card
        if suit(outer_loop_card) in all_suits:
            # find the first card with same suit
            for inner_loop_card in all_cards:
                if suit(inner_loop_card) == suit(outer_loop_card):
                    # return the "closest"
                    target_card = find_target_card(inner_loop_card, outer_loop_card)
                    all_cards.remove(inner_loop_card)
                    all_cards.remove(outer_loop_card)
                    return target_card
        # if there isn't, append the suit
        all_suits.append(suit(outer_loop_card))


def main():
    print("请输入选中的五张牌（如“梅花5”，“方块6”），输入完一张牌按一次回车")
    all_cards = []
    current_card = ""
    # read all cards
    for _ in range(5):
        current_card = input()
        all_cards.append(current_card)
    target_card = find_target(all_cards)
    all_cards = sorted(all_cards, key=functools.cmp_to_key(compare))
    new_all_cards = [target_card[1]] + sorting(target_card[0], all_cards)
    print(new_all_cards)


main()
