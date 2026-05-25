from bruker import Bruker
from tilgang import Tilgangskontroll

class TilgangAvslåttError(Exception):
    # Unntak(egendefinert) som brukes når en bruker ikke har tilgang.
    pass

    def hent_logger(self) -> list[TilgangsloggEntry]:
        # Gir tilbake en kopi av listen for å beskytte den interne tilstanden.
        return self.__hendelser.copy()

class Pasientjournal:
    """
    Representerer en pasientjournal med sensitive helseopplysninger.
    """

    def __init__(self, journal_id: int, eier_id: int, helseopplysninger: str):
        self.__journal_id = journal_id
        self.__eier_id = eier_id
        self.__helseopplysninger = helseopplysninger
        self.__notater: list[str] = []