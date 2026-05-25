# Designvalg

## Valgt programmeringsspråk
Jeg bruker Python fordi det støtter objektorientert programmering og gjør det enkelt å vise arv, abstrakte klasser, polymorfisme og innkapsling.

## Arkitektur
Systemet modelleres med sentrale domeneobjekter som Bruker, Innbygger, Helsepersonell, Administrator, Pasientjournal, Avtale, Melding, Samtykke og Tilgangslogg.

## Sikkerhet
Tilgang til pasientjournal skal kontrolleres gjennom rollebasert tilgangskontroll. Alle forsøk på tilgang skal logges.

## Avgrensning
Kodeeksempelet er ikke en full applikasjon, men en demonstrasjon av sentrale OOP-prinsipper og sikker tilgangsstyring i CareConnect.

# Design før kode

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

Jeg valgte OOP fordi det gir en ryddig måte å modellere brukerroller, journaler og tilgangskontroll på. Det gjør også koden enklere å vedlikeholde og videreutvikle.