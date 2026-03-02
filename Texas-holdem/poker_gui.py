import tkinter as tk
import random
from poker_modulo import *

root = tk.Tk()
root.title("Texas Hold'em")
root.geometry("900x600")
root.configure(bg="#0b5a2a")

canvas = tk.Canvas(root, width=900, height=500, bg="#0b5a2a", highlightthickness=0)
canvas.pack()


stage = 0
current_deck = []
player_hole = []
cpu_hole = []
community = []
player_name = ""

SEMI_COLORI = {"F": "black", "P": "black", "Q": "red", "C": "red"}

def draw_card(x, y, card):
    rank, suit_letter = card
    rank_display = "10" if rank == "X" else rank
    suit_symbol = SEMI_SIMBOLI[suit_letter]
    color = SEMI_COLORI[suit_letter]

    w, h = 70, 100

    canvas.create_rectangle(x, y, x+w, y+h, fill="white", outline="black", width=2)
    canvas.create_text(x+10, y+15, text=rank_display, fill=color, font=("Arial", 14, "bold"), anchor="nw")
    canvas.create_text(x+w/2, y+h/2, text=suit_symbol, fill=color, font=("Arial", 28, "bold"))
    canvas.create_text(x+w-10, y+h-15, text=rank_display, fill=color, font=("Arial", 14, "bold"), anchor="se")


def draw_hand(label, cards, y_text, y_cards):
    canvas.create_text(250, y_text, text=label,
                       fill="white", font=("Arial", 16, "bold"))

    x_start = 350
    for i, card in enumerate(cards):
        draw_card(x_start + i*90, y_cards, card)


def draw_table():
    canvas.delete("all")
    draw_community_placeholders()
    draw_hand(player_name, player_hole, 400, 350)

    x_start = 200
    for i, card in enumerate(community):
        draw_card(x_start + i*90, 200, card)



def draw_small_card(x, y, card, highlight=False):
    rank, suit_letter = card
    rank_display = "10" if rank == "X" else rank
    suit_symbol = SEMI_SIMBOLI[suit_letter]
    color = SEMI_COLORI[suit_letter]

    w, h = 40, 60
    border_color = "yellow" if highlight else "black"
    border_width = 3 if highlight else 1

    canvas.create_rectangle(x, y, x+w, y+h,
                            fill="white",
                            outline=border_color,
                            width=border_width)

    canvas.create_text(x+5, y+5, text=rank_display,
                       fill=color, font=("Arial", 9, "bold"), anchor="nw")

    canvas.create_text(x+w/2, y+h/2,
                       text=suit_symbol,
                       fill=color, font=("Arial", 14, "bold"))


def draw_best_hand(x_start, y, best5, score):
    categoria = score[0]
    values = [RANK_VALUE[c[0]] for c in best5]
    counts = Counter(values)

    for i, card in enumerate(best5):
        highlight = False
        lift = 0
        value = RANK_VALUE[card[0]]

        if categoria in [1, 2, 3, 6, 7]:
            if counts[value] > 1:
                highlight = True
                lift = -8
        elif categoria in [4, 5, 8, 9]:
            highlight = True
            lift = -8

        draw_small_card(x_start + i*45, y + lift, card, highlight)

def draw_community_placeholders():
    w, h = 70, 100
    x_start = 200
    y = 200

    for i in range(5):
        x = x_start + i*90
        canvas.create_rectangle(
            x, y, x+w, y+h,
            fill="#063b1f",     
            outline="#0a7a35",   
            width=2
        )

def new_hand():
    global current_deck, player_hole, cpu_hole, community, stage

    btn_new.config(state="disabled")
    btn_next.config(state="normal")

    stage = 0
    community = []

    current_deck = create_deck()
    random.shuffle(current_deck)

    player_hole = [current_deck.pop() for _ in range(2)]
    cpu_hole = [current_deck.pop() for _ in range(2)]

    draw_table()
    info_label.config(text="PREFLOP")


def next_stage():
    global stage, community

    if stage == 0:
        community = [current_deck.pop() for _ in range(3)]
        info_label.config(text="FLOP")

    elif stage in (1, 2):
        community.append(current_deck.pop())
        info_label.config(text="TURN" if stage == 1 else "RIVER")

    else:
        showdown()
        return

    stage += 1
    draw_table()


def showdown():
    draw_hand("CPU", cpu_hole, 100, 50)

    player_score, player_best5 = best_hand(player_hole + community)
    cpu_score, cpu_best5 = best_hand(cpu_hole + community)

    draw_best_hand(550, 60, cpu_best5, cpu_score)
    draw_best_hand(550, 360, player_best5, player_score)

    if player_score > cpu_score:
        winner, vincitore = "GIOCATORE", player_name
    elif cpu_score > player_score:
        winner = vincitore = "CPU"
    else:
        winner = vincitore = "Pareggio"

    info_label.config(
        text=f"{player_name}: {hand_name(player_score)}  |  "
             f"CPU: {hand_name(cpu_score)}\n"
             f"Vincitore: {vincitore}"
    )

    btn_new.config(state="normal")
    btn_next.config(state="disabled")

    save_result(player_name, winner)

def show_name_screen():
    canvas.delete("all")

    canvas.create_text(450, 200,
                       text="Inserisci il tuo nome",
                       fill="white",
                       font=("Arial", 24, "bold"))

    name_entry = tk.Entry(root, font=("Arial", 16), justify="center")
    name_entry.place(x=325, y=250, width=250)

    def confirm_name():
        global player_name
        player_name = name_entry.get().strip() or "Giocatore"
        name_entry.destroy()
        start_button.destroy()
        draw_table()
        btn_new.config(state="normal")

    start_button = tk.Button(root,
                             text="Inizia",
                             font=("Arial", 14),
                             command=confirm_name)
    start_button.place(x=400, y=300)


def show_leaderboard_window():
    data = load_results()
    win = tk.Toplevel(root)
    win.title("Classifica")
    win.geometry("400x400")
    win.configure(bg="#0b5a2a")

    tk.Label(win, text="Classifica",
             bg="#0b5a2a", fg="white",
             font=("Arial", 18, "bold")).pack(pady=10)

    if not data:
        tk.Label(win, text="Nessun risultato disponibile.",
                 bg="#0b5a2a", fg="white").pack()
        return

    stats = {}
    for r in data:
        p = r["giocatore"]
        stats.setdefault(p, {"vittorie": 0, "partite": 0})
        stats[p]["partite"] += 1
        if r["vincitore"] == "GIOCATORE":
            stats[p]["vittorie"] += 1

    ordered = sorted(stats.items(),
                     key=lambda x: x[1]["vittorie"],
                     reverse=True)

    for i, (name, s) in enumerate(ordered, 1):
        tk.Label(win,
                 text=f"{i}. {name} - V: {s['vittorie']} - P: {s['partite']}",
                 bg="#0b5a2a", fg="white",
                 font=("Arial", 12)).pack(anchor="w", padx=20)

frame = tk.Frame(root, bg="#0b5a2a")
frame.pack(pady=10)

btn_new = tk.Button(frame, text="Nuova Mano", command=new_hand, state="disabled")
btn_new.pack(side="left", padx=20)

btn_next = tk.Button(frame, text="Avanti", command=next_stage, state="disabled")
btn_next.pack(side="left", padx=20)

btn_leaderboard = tk.Button(frame, text="Classifica", command=show_leaderboard_window)
btn_leaderboard.pack(side="left", padx=20)

info_label = tk.Label(root, text="", bg="#0b5a2a", fg="white", font=("Arial", 14))
info_label.pack()

show_name_screen()
root.mainloop()