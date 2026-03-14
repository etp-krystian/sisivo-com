---
title: "Jak znaleźć Association ID dla relacji Custom Object w HubSpot"
description: Instrukcja krok po kroku, jak znaleźć Association ID dla relacji Custom Object w HubSpot przy użyciu CRM API.
date: 2025-04-03
image: /images/blog/association-ids/simple-hubl-template.png
imageAlt: "Podgląd prostego szablonu HubL"
imageWidth: 655
imageHeight: 423
tags:
  - hubspot
  - integrations
  - custom-objects
  - postPl
alternateLangs:
  en: /blog/how-to-find-association-ids-for-custom-object-relationships-in-hubspot/
  pl: /pl/blog/jak-znalezc-association-id-dla-relacji-custom-object-w-hubspot/
---

Jeśli pracujesz z Custom Objects w HubSpot, prędzej czy później trafisz na problem odnalezienia właściwego `Association ID`. Dla standardowych relacji HubSpot publikuje listę identyfikatorów w dokumentacji. Dla relacji niestandardowych nie jest to już tak oczywiste.

W tym wpisie pokazuję prosty sposób, jak znaleźć `Association ID` przy pomocy CRM API.

## Przykładowy scenariusz

Załóżmy, że masz dwa Custom Objects:

- `Car`
- `AutomotiveService`

Obiekt `Car` jest połączony z Contact, a `AutomotiveService` z obiektem `Car`.

Chcesz pobrać relacje w HubL, korzystając z funkcji:

- `crm_objects`
- `crm_associations`

To właśnie tutaj potrzebujesz poprawnego `associationId`.

## Jak działa crm_associations

Funkcja ma taką strukturę:

```text
crm_associations(objectId, associationCategory, associationId, query, property, formatting)
```

Trzy pierwsze parametry są obowiązkowe:

- `objectId` to ID obiektu źródłowego, np. Contact
- `associationCategory` to zwykle `HUBSPOT_DEFINED` albo `USER_DEFINED`
- `associationId` to identyfikator relacji, którego właśnie szukamy

## Gdzie znaleźć Association ID dla relacji niestandardowej

### Krok 1: utwórz Private App

Najpierw utwórz Private App w HubSpot i nadaj mu dostęp do Contacts oraz schematów Custom Objects.

Przydadzą się odpowiednie scope'y związane z odczytem obiektów i ich schematów.

### Krok 2: użyj Associations API

Następnie przejdź do Associations API i użyj endpointu listującego skojarzenia dla konkretnego obiektu.

W praktyce podajesz:

- typ obiektu źródłowego, np. Contact
- konkretne `objectId`
- typ obiektu docelowego, np. Car

### Krok 3: odczytaj `typeId`

W odpowiedzi API otrzymasz dane relacji. Właśnie pole `typeId` jest wartością, której potrzebujesz jako `associationId`.

To ten identyfikator później podstawiasz do `crm_associations`.

## Dlaczego to jest przydatne

Ten sposób pozwala pobierać niestandardowe relacje i budować widoki oparte o Custom Objects, np.:

- kontakty i przypisane samochody
- subskrypcje i przypisane kontrakty
- urządzenia i powiązane zgłoszenia serwisowe

## Podsumowanie

HubSpot nie pokazuje czytelnie `Association ID` dla wszystkich niestandardowych relacji, ale da się je łatwo znaleźć przez CRM API. Jeśli pracujesz na Custom Objects i HubL, to jedna z tych rzeczy, które warto mieć opanowane od początku.

[Skontaktuj się z nami](/pl/kontakt/), jeśli potrzebujesz pomocy przy Custom Objects lub integracjach HubSpot.
