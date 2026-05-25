from bruker import Innbygger, Helsepersonell, Saksbehandler, Administrator
from journal import Pasientjournal, TilgangAvslåttError
from tilgang import Tilgangslogg, Tilgangskontroll

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