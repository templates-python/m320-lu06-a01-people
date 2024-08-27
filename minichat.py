""" Provides a simple class to demonstrate communication """
class MiniChat:
    """
    Eine kleine Demo für das Kommunizieren von Klassen.
    """

    def __init__(self, name):
        '''
        Ich muss mich im Chat mit Namen bekannt machen
        '''
        self._name = name

    @property
    def name(self):
        """ returns the name """
        return self._name

    def send_a_message_to(self, receiver, message):
        """
        Sendet eine Mitteilung (message) an einen durch Empfänger (receiver)
        :param message: Inhalt der Mitteilung
        :param receiver: Empfänger der Mitteilung
        """
        print(f'from {self}')
        receiver.get_a_message(f'Content: {message}')

    def get_a_message(self, message):
        """
        Empfängt eine Meldung und gibt diese am Stdout aus.
        :param message: eine Nachricht
        """
        print(f'to {self}\n{message}')

    def __str__(self):
        return self.name
