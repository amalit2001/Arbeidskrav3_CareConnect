from dataclasses import dataclass, field
from datetime import datetime
from bruker import Bruker, Rolle

@dataclass(frozen=True)
class TilgangsloggEntry:
    bruker_id: int
    rolle: Rolle
    ressurs: str
    handling: str
    resultat: str
    tidspunkt: datetime = field(default_factory=datetime.now)

class Tilgangslogg:
    """
    Registrerer tilgangsforsøk i systemet, både godkjente og nektede.
    (Dette ville blitt lagret i en sikker database i en ekte løsning.)
    """

    def __init__(self):
        self.__hendelser: list[TilgangsloggEntry] = []

    def registrer_tilgang(
        self,
        bruker: Bruker,
        ressurs: str,
        handling: str,
        resultat: str
    ) -> None:
        hendelse = TilgangsloggEntry(
            bruker_id=bruker.bruker_id,
            rolle=bruker.rolle,
            ressurs=ressurs,
            handling=handling,
            resultat=resultat
        )
        self.__hendelser.append(hendelse)
    ...

class Tilgangskontroll:
    """
    Sjekker om brukeren har tilgang og logger alle forsøk i Tilgangsloggen.
    """

    def __init__(self, tilgangslogg: Tilgangslogg):
        self.__tilgangslogg = tilgangslogg

    def sjekk_tilgang(
        self,
        bruker: Bruker,
        ressurs: str,
        eier_id: int | None,
        handling: str
    ) -> bool:
        har_tilgang = bruker.har_tilgang(ressurs, eier_id)

        resultat = "GODKJENT" if har_tilgang else "AVSLÅTT"

        self.__tilgangslogg.registrer_tilgang(
            bruker=bruker,
            ressurs=ressurs,
            handling=handling,
            resultat=resultat
        )

        return har_tilgang