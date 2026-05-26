# Designvalg

## Valgt programmeringsspråk
Jeg valgte å bruke Python fordi det støtter OOP og gjør det enkelt å vise arv, abstrakte klasser, polymorfisme og innkapsling.

## Arkitektur
Systemet modelleres med sentrale domeneobjekter som Bruker, Innbygger, Helsepersonell, Administrator, Saksbehandler, Pasientjournal, Avtale, Melding, Samtykke, Varsel og Tilgangslogg.

## Sikkerhet
Tilgang til pasientjournal skal kontrolleres gjennom rollebasert tilgangskontroll. Alle forsøk på tilgang skal logges.

## Avgrensning
Kodeeksempelet er ikke en full applikasjon, men en demonstrasjon av sentrale OOP-prinsipper og sikker tilgangsstyring i CareConnect.

## Design før kode

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

## Kobling mellom design og OOP-prinsipper

OOP-prinsipper: arv, abstraksjon, polymorfisme, innkapsling, sikkerhet og logging.

Slik vises det:
- Arv: Innbygger, Helsepersonell, Administrator og Saksbehandler arver fra Bruker.
- Abstraksjon: Hovedklassen Bruker er abstrakt.
- Polymorfisme: Alle roller har `har_tilgang()`, men metoden fungerer ulikt.
- Innkapsling: Journaldata ligger privat og kan kun hentes via tilgangskontroll.
- Sikkerhet: Tilgangen sjekkes før journal vises.
- Logging: Alle journaloppslag blir registrert.

Personlig synes jeg OOP er en ryddig måte å modellere journaler, tilgangskontroll og brukerroller på. Slik blir koden også enklere å videreutvikle og vedlikeholde.