from abc import ABC, abstractmethod
from enum import Enum

class Rolle(Enum):
    INNBYGGER = "Innbygger"
    HELSEPERSONELL = "Helsepersonell"
    SAKSBEHANDLER = "Saksbehandler"
    ADMINISTRATOR = "Administrator"

class Bruker(ABC):
    """
    Hovedklasse for alle brukere i systemet.
    Inneholder felles egenskaper og metoder, 
    og en abstrakt metode for tilgangskontroll.
    """

    def __init__(self, bruker_id: int, navn: str, epost: str, rolle: Rolle):
        self.__bruker_id = bruker_id
        self.__navn = navn
        self.__epost = epost
        self.__rolle = rolle

class Innbygger(Bruker):
    def __init__(self, bruker_id: int, navn: str, epost: str):
        super().__init__(bruker_id, navn, epost, Rolle.INNBYGGER)

    def se_egne_opplysninger(self) -> None:
        print(f"{self.navn} ser egne opplysninger.")

    def bestill_avtale(self) -> None:
        print(f"{self.navn} bestiller en avtale.")

    def administrer_samtykke(self) -> None:
        print(f"{self.navn} administrerer samtykker.")

    def har_tilgang(self, ressurs: str, eier_id: int | None = None) -> bool:
        # Innbygger får bare lese egen pasientjournal.
        if ressurs == "pasientjournal":
            return eier_id == self.bruker_id

        return False

class Helsepersonell(Bruker):
    def __init__(
        self,
        bruker_id: int,
        navn: str,
        epost: str,
        ansatt_id: int,
        pasient_ids: list[int]
    ):
        super().__init__(bruker_id, navn, epost, Rolle.HELSEPERSONELL)
        self.__ansatt_id = ansatt_id
        self.__pasient_ids = pasient_ids

    @property
    def ansatt_id(self) -> int:
        return self.__ansatt_id

    def se_pasientjournal(self) -> None:
        print(f"{self.navn} prøver å se pasientjournal.")

    def dokumenter_kommunikasjon(self) -> None:
        print(f"{self.navn} dokumenterer kommunikasjon.")

    def administrer_avtale(self) -> None:
        print(f"{self.navn} administrerer avtale.")

    def har_tilgang(self, ressurs: str, eier_id: int | None = None) -> bool:
        if ressurs in ["pasientjournal", "journal_notat"]:
            return eier_id in self.__pasient_ids
# Helsepersonell kan bare lese journaler kun til innbyggere de følger opp.
        return False

class Saksbehandler(Bruker):
    def __init__(self, bruker_id: int, navn: str, epost: str):
        super().__init__(bruker_id, navn, epost, Rolle.SAKSBEHANDLER)

    def behandle_sak(self) -> None:
        print(f"{self.navn} behandler en sak.")

    def se_relevant_dokumentasjon(self) -> None:
        print(f"{self.navn} ser relevant dokumentasjon.")

    def har_tilgang(self, ressurs: str, eier_id: int | None = None) -> bool:
        # Saksbehandler kan se dokumentasjon, men ikke pasientjournal.
        return ressurs == "dokumentasjon"

class Administrator(Bruker):
    def __init__(self, bruker_id: int, navn: str, epost: str):
        super().__init__(bruker_id, navn, epost, Rolle.ADMINISTRATOR)

    def opprett_bruker(self) -> None:
        print(f"{self.navn} lager en bruker.")

    def endre_rolle(self) -> None:
        print(f"{self.navn} endrer rolle for bruker.")

    def se_tilgangslogger(self) -> None:
        print(f"{self.navn} ser tilgangslogger.")

    def har_tilgang(self, ressurs: str, eier_id: int | None = None) -> bool:
        # Administrator kan administrere systemet,
        # men skal ikke automatisk ha tilgang til pasientjournaler.
        return ressurs in ["brukeradministrasjon", "tilgangslogg"]