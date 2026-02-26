import poker_modulo as poker

# Rendiamo il programma eseguibile
def main():
    print("TEXAS HOLD'EM")
    player_name = input("Inserisci il tuo nome: ").strip()
    if not player_name:
        player_name = "Giocatore"
    while True:
        print("\nMenu:")
        print("1) Gioca")
        print("2) Classifica")
        print("3) Esci")

        scelta = input("Scelta: ").strip()

        if scelta == "1":
            poker.play_round(player_name)
        elif scelta == "2":
            poker.show_leaderboard()
        elif scelta == "3":
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
#In modo che se importiamo questo file py in un altro file python viene solo importata la funzione ma non parte il programma. Questo parte solo se avviamo il file py direttamente