Design før kode/Designvalg

Bruker
├── Innbygger
├── Helsepersonell
├── Saksbehandler
└── Administrator

Andre klasser:
- Pasientjournal
- Avtale
- Melding
- Samtykke
- Varsel
- Tilgangslogg

Her får jeg vist:

| OOP-prinsipp | Hvordan du viser det                                              |
| ------------ | ----------------------------------------------------------------- |
| Arv          | Innbygger, Helsepersonell og Administrator arver fra Bruker       |
| Abstraksjon  | Bruker er en abstrakt hovedklasse                                 |
| Polymorfisme | Alle roller har `har_tilgang()`, men metoden fungerer ulikt       |
| Innkapsling  | Journaldata ligger privat og kan bare hentes via tilgangskontroll |
| Sikkerhet    | Tilgang sjekkes før journal vises                                 |
| Logging      | Alle journaloppslag registreres                                   |

Tavlenotatet sier også at OOP gir bedre struktur, enklere vedlikehold, gjenbruk av kode, bedre sikkerhet og enklere videreutvikling, så det passer veldig godt å bruke OOP aktivt i denne oppgaven.