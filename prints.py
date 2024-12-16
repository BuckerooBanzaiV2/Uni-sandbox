import random

def zeichne_tannenbaum_mit_deko(hoehe):
    dekorationen = ['o', '+']  
    print(' ' * (hoehe - 1) + '★')  
    for i in range(1, hoehe + 1):  
        zeile = ' ' * (hoehe - i)  
        for j in range(2 * i - 1):
            if random.random() > 0.7:  
                zeile += random.choice(dekorationen)
            else:
                zeile += '*'
        print(zeile)
    print(' ' * (hoehe - 1) + '|') 

def main():
    hoehe = 5  
    zeichne_tannenbaum_mit_deko(hoehe)
    
    while True:
        user_input = input("Möchten Sie den Tannenbaum neu zeichnen? (ja/nein): ").strip().lower()
        if user_input == "ja":
            zeichne_tannenbaum_mit_deko(hoehe)
        elif user_input == "nein":
            print("Auf Wiedersehen!")
            break
        else:
            print("Bitte antworten Sie mit 'ja' oder 'nein'.")


if __name__ == "__main__":
    main()
