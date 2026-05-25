from bruker import Bruker
from tilgang import Tilgangskontroll


class TilgangAvslåttError(Exception):
    # Brukes når en rolle prøver å hente/endre journal med uautorisert tilgang.
    pass


class Pasientjournal:
    """
    Modell for en pasientjournal som inneholder sensitive data.
    """

    def __init__(self, journal_id: int, eier_id: int, helseopplysninger: str):
        self.__journal_id = journal_id
        self.__eier_id = eier_id
        self.__helseopplysninger = helseopplysninger
        self.__notater: list[str] = []
        # Innkapsling for å hindre direkte tilgang til journaldata utenfra.

    @property
    def journal_id(self) -> int:
        return self.__journal_id

    @property
    def eier_id(self) -> int:
        return self.__eier_id

    def hent_journal(
        self,
        bruker: Bruker,
        tilgangskontroll: Tilgangskontroll
    ) -> str:
        tilgang = tilgangskontroll.sjekk_tilgang(
            bruker=bruker,
            ressurs="pasientjournal",
            eier_id=self.__eier_id,
            handling="hent_journal"
        )

        if not tilgang:
            raise TilgangAvslåttError(
                f"Tilgang avslått: {bruker.navn} har ikke tilgang til å se journal {self.__journal_id}."
            )

        return self.__helseopplysninger

    def legg_til_notat(
        self,
        bruker: Bruker,
        notat: str,
        tilgangskontroll: Tilgangskontroll
    ) -> None:
        tilgang = tilgangskontroll.sjekk_tilgang(
        # Journalen returneres kun om tilgangskontrollen godkjenner brukeren.
            bruker=bruker,
            ressurs="journal_notat",
            eier_id=self.__eier_id,
            handling="legg_til_notat"
        )

        if not tilgang:
            raise TilgangAvslåttError(
                f"Tilgang avslått: {bruker.navn} har ikke tilgang til å endre journal {self.__journal_id}."
            )

        self.__notater.append(notat)