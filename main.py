from minichat import MiniChat


def main():
    # die beteilgten Objekte
    max = MiniChat('Max')
    moritz = MiniChat('Moritz')
    lempel = MiniChat('Lempel')
    # die Kommunikation
    max.send_a_message_to(moritz, f'hallo {moritz} wollen wir {lempel} ein wenig ärgern?')
    moritz.send_a_message_to(max, f'aber sicher')
    lempel.send_a_message_to(max, f'Lieber {max} das kann für dich und {moritz} böse enden')
    #
    # eigene Kommunikation mit eigenen Objekten


if __name__ == "__main__":
    main()