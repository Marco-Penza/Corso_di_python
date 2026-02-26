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
    "p": "\u2660"}

RANK_VALUE = {r: i for i, r in enumerate(RANKS,start=2)}


"""for i, r in enumerate(RANKS, start=2):
    print(i,r)"""

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

def create_deck():
    return [r + s for r in RANKS for s in SEMI]

"""quello che vediamo con il createDeck"""
"""deck = []
for r in RANKS:
    for s in SEMI:
        deck.append(r + s)
        
print(deck)"""

""" Associamo i somboli alle carte """

def pretty_cards(cards):
    return " ".join([c[0] + SEMI_SIMBOLI.get(c[1], c[1]) for c in cards])

def is_straight(values):
    if len(values) < 5:
        return False, None
    
    wheel = {14, 5, 4, 3, 2,}
    if set(values) >= wheel:
        return True, 5
    
    vals = sorted(set(values), reverse=True)
    for i in range(len(vals) - 4):
        window = vals[i:i+5]
        if window[0] - window[4] == 4:
            return True, window[0]
    return False, None

""" Valuta una mano di 5 carte (funzione evaluate_5 1 di 4)"""

def evaluate_5(cards5):
    values = sorted([RANK_VALUE[c[0]] for c in cards5], reverse=True)
    semi = [c[1] for c in cards5]

    counts = Counter(values)
    counts_groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    flush = len(set(semi)) == 1
    unique_values = sorted(set(values), reverse=True)
    straight, straight_high = is_straight(unique_values)

    if flush and straight:
        if straight_high == 14:
            return(9,)
        return (8, straight_high)
    
    if counts_groups[0][1] == 4:
        quad = counts_groups[0][0]
        kicker = max(v for v in values if v != quad)
        return (7, quad, kicker)
    
    if counts_groups[0][1] == 3 and counts_groups [1] [1] == 2:
        return(6, counts_groups[0][0], counts_groups[1][0])
    
    if flush:
        return (5, *values)
    
    if straight:
        return (4, straight_high)
    
    if counts_groups[0][1] == 3:
        trips = counts_groups[0][0]
        kickers = sorted([v for v in values if v != trips], reverse=True)
        return (3, trips, *kickers)
    
    if counts_groups[0][1] == 2 and counts_groups[1][1] == 2:
        highPair = max(counts_groups[0][0], counts_groups [1][0])
        lowPair = min(counts_groups[0][0], counts_groups[1][0])
        kicker = max(v for v in values if v not in (highPair, lowPair))
        return (2, highPair, lowPair, kicker)
    
    if counts_groups[0][1] == 2:
        pair = counts_groups[0][0]
        kicker = sorted([v for v in values if v != pair], reverse=True)
        return (1, pair, *kicker)
    
    return (0, *values)

def best_hand(cards7):
    best = None
    best5 = None
    n = len(cards7)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    for m in range(l + 1, n):
                        combo = [cards7[i], cards7[j], cards7[k], cards7[l], cards7[m]]
                        score = evaluate_5(combo)
                        if best is None or score > best:
                            best = score
                            best5 = combo
    return best, best5

def hand_name(score):
    return HAND_NAMES.get(score[0], "Sconosciuto")

def play_round(player_name):
    deck = create_deck()
    random.shuffle(deck)

    player_hole = [deck.pop(), deck.pop()]
    cpu_hole = [deck.pop(), deck.pop()]
    print("\n--- PREFLOP ---")
    print("Le tue carte:", pretty_cards(player_hole))
    input("Premi INVIO per il flop...")

    flop = [deck.pop(), deck.pop(), deck.pop()]
    print("\n--- FLOP ---")
    print("Comuni:", pretty_cards(flop))
    input("Premi INVIO per il turn...")

    turn = deck.pop()
    community = flop + [turn]
    print("\n--- TURN ---")
    print("Comuni:", pretty_cards(community))
    input("Premi INVIO per il river...")

    river = deck.pop()
    community.append(river)
    print("\n--- RIVER ---")
    print("Comuni:", pretty_cards(community))
    input("Premi INVIO per lo showdown...")
    print("\n--- SHOWDOWN ---")
    print("Carte CPU:", pretty_cards(cpu_hole))

    player_score, player_best5 = best_hand(player_hole + community)
    cpu_score, cpu_best5 = best_hand(cpu_hole + community)

    print("\nMiglior mano giocatore:", hand_name(player_score))
    print("Carte vincenti giocatore:", pretty_cards(player_best5))

    print("\nMiglior mano CPU:", hand_name(cpu_score))
    print("Carte vincenti CPU:", pretty_cards(cpu_best5))

    if player_score > cpu_score:
        winner = "GIOCATORE"
        print("Hai vinto.")
    elif cpu_score > player_score:
        winner = "CPU"
        print("Ha vinto la CPU.")
    else:
        winner = "PAREGGIO"
        print("Pareggio.")

    save_result(player_name, winner)
    
    return winner

def load_result():
    if not os.path.exists(FILE_RISULTATI):
        return []
    try:
        with open(FILE_RISULTATI, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# Salviamo i risultati
def save_result(player_name, winner):
    data = load_result()
    data.append({
        "giocatore": player_name,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vincitore": winner
    })
    with open(FILE_RISULTATI, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Mostriamo le statistiche dei giocatori (leaderboards)

def show_leaderboard():
    data = load_result()
    stats = {}

    for r in data:
        p = r["giocatore"]
        if p not in stats:
            stats[p] = {"vittorie": 0, "partite": 0}
        stats[p]["partite"] += 1
        if r["vincitore"] == "GIOCATORE":
            stats[p]["vittorie"] += 1

    orderer = sorted(stats.items(), key=lambda x: x[1]["vittorie"], reverse=True)

    print("\nClassifica:")
    for i, (name, s) in enumerate(orderer, 1):
        print(f"{i}, {name} - Vittorie: {s['vittorie']} - Partite: {s['partite']}")

    