from bruker import Bruker
from tilgang import Tilgangskontroll


class TilgangAvslåttError(Exception):
    # Egendefinert unntak som brukes når en bruker ikke har tilgang.
    pass


class Pasientjournal:
    """
    Representerer en pasientjournal med sensitive helseopplysninger.
    """

    def __init__(self, journal_id: int, eier_id: int, helseopplysninger: str):
        self.__journal_id = journal_id
        self.__eier_id = eier_id
        self.__helseopplysninger = helseopplysninger
        self.__notater: list[str] = []

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
                f"Tilgang avslått: {bruker.navn} har ikke tilgang til journal {self.__journal_id}."
            )

        return self.__helseopplysninger

    def legg_til_notat(
        self,
        bruker: Bruker,
        notat: str,
        tilgangskontroll: Tilgangskontroll
    ) -> None:
        tilgang = tilgangskontroll.sjekk_tilgang(
            bruker=bruker,
            ressurs="journal_notat",
            eier_id=self.__eier_id,
            handling="legg_til_notat"
        )

        if not tilgang:
            raise TilgangAvslåttError(
                f"Tilgang avslått: {bruker.navn} har ikke tilgang til journal {self.__journal_id}."
            )

        self.__notater.append(notat)