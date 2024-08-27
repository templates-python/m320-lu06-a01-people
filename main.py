"""
Exercise to experiment with communication
"""

from minichat import MiniChat


def main():
    """
    simple communication between some objects
    :return: 
    """
    # die beteilgten Objekte
    maxi = MiniChat('Max')
    moritz = MiniChat('Moritz')
    lempel = MiniChat('Lempel')
    # die Kommunikation
    maxi.send_a_message_to(moritz, f'hallo {moritz} wollen wir {lempel} ein wenig ärgern?')
    moritz.send_a_message_to(maxi, 'aber sicher')
    lempel.send_a_message_to(maxi, f'Lieber {maxi} das kann für dich und {moritz} böse enden')
    #
    # eigene Kommunikation mit eigenen Objekten
    lulu = MiniChat('Lulu')
    randy = MiniChat('Randy')
    lulu.send_a_message_to(randy, f'hallo {randy.name} wo gehen wir heute essen')
    randy.send_a_message_to(lulu, 'ins Olivo')


if __name__ == "__main__":
    main()
    