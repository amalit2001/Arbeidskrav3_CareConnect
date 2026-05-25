from bruker import Innbygger, Helsepersonell, Saksbehandler, Administrator
from journal import Pasientjournal, TilgangAvslåttError
from tilgang import Tilgangslogg, Tilgangskontroll

    @property
    def bruker_id(self) -> int:
        return self.__bruker_id

    @property
    def navn(self) -> str:
        return self.__navn

    @property
    def epost(self) -> str:
        return self.__epost

    @property
    def rolle(self) -> Rolle:
        return self.__rolle

    def logg_inn(self) -> bool:
        print(f"{self.__navn} har logget inn.")
        return True

    def logg_ut(self) -> None:
        print(f"{self.__navn} har logget ut.")

    @abstractmethod
    def har_tilgang(self, ressurs: str, eier_id: int | None = None) -> bool: 
       if ressurs == "pasientjournal":
            return eier_id == self.bruker_id
            return False
       #Innbygger får lese egen journal, men ikke andre ressurser
    """ Dette er en polymorf metode som gjør at underklassene selv bestemmer
        hva de har tilgang til."""
pass

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


def vis_logger(tilgangslogg: Tilgangslogg) -> None:
    print("\n--- Tilgangslogg ---")
    for logg in tilgangslogg.hent_logger():
        print(
            f"{logg.tidspunkt} | "
            f"bruker_id={logg.bruker_id} | "
            f"rolle={logg.rolle.value} | "
            f"ressurs={logg.ressurs} | "
            f"handling={logg.handling} | "
            f"resultat={logg.resultat}"
        )


def main() -> None:
    tilgangslogg = Tilgangslogg()
    tilgangskontroll = Tilgangskontroll(tilgangslogg)

    innbygger = Innbygger(
        bruker_id=1,
        navn="Amalie Innbygger",
        epost="amalie@example.no"
    )

    helsepersonell = Helsepersonell(
        bruker_id=2,
        navn="Tove Sykepleier",
        epost="tove@example.no",
        ansatt_id=1001,
        pasient_ids=[1]
    )

    saksbehandler = Saksbehandler(
        bruker_id=3,
        navn="Herman Saksbehandler",
        epost="herman@example.no"
    )

    administrator = Administrator(
        bruker_id=4,
        navn="Ali Administrator",
        epost="ali@example.no"
    )

    journal = Pasientjournal(
        journal_id=101,
        eier_id=1,
        helseopplysninger="Journal(fiktiv): Innbygger har en avtale med sykepleier."
    )

    print("--- CareConnect demo ---\n")

    innbygger.logg_inn()

    print("\n1. Innbygger leser journalen sin:")
    print(journal.hent_journal(innbygger, tilgangskontroll))

    print("\n2. Helsepersonell leser journalen til innbygger de følger opp:")
    print(journal.hent_journal(helsepersonell, tilgangskontroll))

    print("\n3. Saksbehandler prøver å lese pasientjournal:")
    try:
        print(journal.hent_journal(saksbehandler, tilgangskontroll))
    except TilgangAvslåttError as error:
        print(error)

    print("\n4. Administrator prøver å lese pasientjournal:")
    try:
        print(journal.hent_journal(administrator, tilgangskontroll))
    except TilgangAvslåttError as error:
        print(error)

    vis_logger(tilgangslogg)


if __name__ == "__main__":
    main()