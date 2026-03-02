import json
import os
import random
from datetime import datetime
from collections import Counter

FILE_RISULTATI = "risultati.json"

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K", "A"]
SEMI = ["F", "Q", "C", "P"]
SEMI_SIMBOLI = {
    "F": "\u2663",  
    "Q": "\u2666",  
    "C": "\u2665",  
    "P": "\u2660"   
}
RANK_VALUE = {r: i for i, r in enumerate(RANKS, start=2)}

HAND_NAMES = {
    9: "Scala reale",
    8: "Scala colore",
    7: "Poker",
    6: "Full",
    5: "Colore",
    4: "Scala",
    3: "Tris",
    2: "Doppia coppia",
    1: "Coppia",
    0: "Carta alta",
}

def ascii_card(rank, suit):
    TL = "\u250C" 
    TR = "\u2510"  
    BL = "\u2514"  
    BR = "\u2518"  
    H  = "\u2500"  
    V  = "\u2502"  

    W = 9

    rank = str(rank)
    suit = str(suit)

    top = TL + (H * W) + TR
    bottom = BL + (H * W) + BR

    empty = V + (" " * W) + V

    rank_top = V + " " + f"{rank:<2}" + (" " * (W - 3)) + V

    rank_bottom = V + (" " * (W - 3)) + f"{rank:>2}" + " " + V

    suit_line = V + suit.center(W) + V

    return [
        top,
        rank_top,
        empty,
        suit_line,
        empty,
        rank_bottom,
        bottom
    ]

def create_deck():
    return [r + s for r in RANKS for s in SEMI]

def print_cards(cards):
    card_lines = []

    for c in cards:
        rank = c[0]
        suit_letter = c[1]

        if rank == "X":
            rank_display = "10"
        else:
            rank_display = rank

        suit_symbol = SEMI_SIMBOLI.get(suit_letter, suit_letter)

        card_lines.append(ascii_card(rank_display, suit_symbol))

    for i in range(7):
        for card in card_lines:
            print(card[i], end="  ")
        print()
        
# def pretty_cards(cards):
#    return " ".join([c[0] + SEMI_SIMBOLI.get(c[1], c[1]) for c in cards])


def is_straight(values):
    if len(values) < 5:
        return False, None

    wheel = {14, 5, 4, 3, 2}
    if set(values) >= wheel:
        return True, 5

    vals = sorted(set(values), reverse=True)
    for i in range(len(vals) - 4):
        window = vals[i:i+5]
        if window[0] - window[4] == 4:
            return True, window[0]
    return False, None


def evaluate_5(cards5):
    values = sorted([RANK_VALUE[c[0]] for c in cards5], reverse=True)
    semi = [c[1] for c in cards5]

    counts = Counter(values)
    count_groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    flush = len(set(semi)) == 1
    unique_values = sorted(set(values), reverse=True)
    straight, straight_high = is_straight(unique_values)

    if flush and straight:
        if straight_high == 14:
            return (9,)
        return (8, straight_high)

    if count_groups[0][1] == 4:
        quad = count_groups[0][0]
        kicker = max(v for v in values if v != quad)
        return (7, quad, kicker)

    if count_groups[0][1] == 3 and count_groups[1][1] == 2:
        return (6, count_groups[0][0], count_groups[1][0])

    if flush:
        return (5, *values)

    if straight:
        return (4, straight_high)

    if count_groups[0][1] == 3:
        trips = count_groups[0][0]
        kickers = sorted([v for v in values if v != trips], reverse=True)
        return (3, trips, *kickers)

    if count_groups[0][1] == 2 and count_groups[1][1] == 2:
        high_pair = max(count_groups[0][0], count_groups[1][0])
        low_pair = min(count_groups[0][0], count_groups[1][0])
        kicker = max(v for v in values if v not in (high_pair, low_pair))
        return (2, high_pair, low_pair, kicker)

    if count_groups[0][1] == 2:
        pair = count_groups[0][0]
        kickers = sorted([v for v in values if v != pair], reverse=True)
        return (1, pair, *kickers)

    return (0, *values)


def best_hand(cards7):
    best = None
    best5 = None
    n = len(cards7)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        combo = [cards7[i], cards7[j], cards7[k], cards7[l], cards7[m]]
                        score = evaluate_5(combo)
                        if best is None or score > best:
                            best = score
                            best5 = combo
    return best, best5


def hand_name(score):
    return HAND_NAMES.get(score[0], "Sconosciuta")



def play_round(player_name):
    deck = create_deck()
    random.shuffle(deck)

    player_hole = [deck.pop(), deck.pop()]
    cpu_hole = [deck.pop(), deck.pop()]

    print("\n--- PREFLOP ---")
    print("Le tue carte:")
    print_cards(player_hole)

    input("Premi INVIO per il flop...")

    flop = [deck.pop(), deck.pop(), deck.pop()]
    print("\n--- FLOP ---")
    print("Carte comuni:")
    print_cards(flop)

    input("Premi INVIO per il turn...")

    turn = deck.pop()
    community = flop + [turn]
    print("\n--- TURN ---")
    print("Carte comuni:")
    print_cards(community)

    input("Premi INVIO per il river...")

    river = deck.pop()
    community.append(river)
    print("\n--- RIVER ---")
    print("Carte comuni:")
    print_cards(community)

    input("Premi INVIO per lo showdown...")

    print("\n--- SHOWDOWN ---")

    print("Carte CPU:")
    print_cards(cpu_hole)

    player_score, player_best5 = best_hand(player_hole + community)
    cpu_score, cpu_best5 = best_hand(cpu_hole + community)

    print("\nMiglior mano giocatore:", hand_name(player_score))
    print("Carte vincenti giocatore:")
    print_cards(player_best5)

    print("\nMiglior mano CPU:", hand_name(cpu_score))
    print("Carte vincenti CPU:")
    print_cards(cpu_best5)

    if player_score > cpu_score:
        winner = "GIOCATORE"
        print("\nHai vinto.")
    elif cpu_score > player_score:
        winner = "CPU"
        print("\nHa vinto la CPU.")
    else:
        winner = "PAREGGIO"
        print("\nPareggio.")

    save_result(player_name, winner)

    return winner


def load_results():
    if not os.path.exists(FILE_RISULTATI):
        return []
    try:
        with open(FILE_RISULTATI, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_result(player_name, winner):
    data = load_results()
    data.append({
        "giocatore": player_name,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vincitore": winner
    })
    with open(FILE_RISULTATI, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def show_leaderboard():
    data = load_results()
    stats = {}

    for r in data:
        p = r["giocatore"]
        if p not in stats:
            stats[p] = {"vittorie": 0, "partite": 0}
        stats[p]["partite"] += 1
        if r["vincitore"] == "GIOCATORE":
            stats[p]["vittorie"] += 1

    ordered = sorted(stats.items(), key=lambda x: x[1]["vittorie"], reverse=True)

    print("\nClassifica:")
    for i, (name, s) in enumerate(ordered, 1):
        print(f"{i}. {name} - Vittorie: {s['vittorie']} - Partite: {s['partite']}")


