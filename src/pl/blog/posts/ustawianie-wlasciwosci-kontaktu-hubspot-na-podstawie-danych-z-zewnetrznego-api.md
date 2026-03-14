---
title: "Jak ustawiać właściwości kontaktu HubSpot na podstawie danych z zewnętrznego API"
description: Instrukcja krok po kroku pokazująca, jak w HubSpot Workflows ustawić właściwość kontaktu na podstawie odpowiedzi z zewnętrznego API.
date: 2025-03-20
image: /images/blog/external-api-data-workflows.jpg
imageAlt: "Wykorzystanie danych z zewnętrznego API w HubSpot Workflows"
imageWidth: 1200
imageHeight: 628
tags:
  - hubspot
  - workflows
  - integrations
  - postPl
alternateLangs:
  en: /blog/setting-hubspot-crm-contact-properties-based-on-external-api-data-in-workflows/
  pl: /pl/blog/ustawianie-wlasciwosci-kontaktu-hubspot-na-podstawie-danych-z-zewnetrznego-api/
---

Jeśli chcesz, aby workflow w HubSpot ustawiał właściwość kontaktu na podstawie odpowiedzi z zewnętrznego API, możesz to zrobić przy pomocy `Custom code action` oraz Private App.

W tym poradniku pokazuję uproszczony, ale praktyczny scenariusz: po ustawieniu adresu email na kontakcie workflow odpytuje zewnętrzny serwis, sprawdza czy email znajduje się na liście zwróconej przez API, a następnie ustawia wartość właściwości kontaktu.

## Założenie scenariusza

Proces wygląda tak:

1. kontakt otrzymuje lub zmienia adres email
2. workflow uruchamia custom code
3. kod wysyła request do zewnętrznego API
4. odpowiedź jest analizowana
5. właściwość kontaktu w HubSpot jest aktualizowana

## Przygotowanie

Na potrzeby przykładu potrzebujesz:

- własnego endpointu API, który zwraca dane do sprawdzenia
- custom property w obiekcie Contact, np. `Found in external API`
- Private App z odpowiednimi scope'ami do odczytu i zapisu kontaktów

Jeżeli nie masz jeszcze custom property, zacznij od jej utworzenia w ustawieniach kontaktów w HubSpot.

## Krok 1: skonfiguruj Private App

W HubSpot przejdź do:

`Settings -> Integrations -> Private Apps`

Utwórz nową aplikację i nadaj jej uprawnienia:

- `crm.objects.contacts`
- `crm.schemas.contacts`

Najczęściej potrzebujesz zarówno `Read`, jak i `Write`.

Po utworzeniu aplikacji skopiuj token. Będzie potrzebny w workflow jako secret.

## Krok 2: utwórz workflow

Stwórz workflow typu `Contact-based` i ustaw trigger na zmianę właściwości `Email` z warunkiem `is known`.

Następnie dodaj akcję `Custom code` z sekcji `Data ops`.

## Krok 3: dodaj secret i input field

W custom code:

- dodaj secret z tokenem Private App, np. pod nazwą `SECRET`
- dodaj input field `email`, mapując go do właściwości `Email`

To pozwoli wykorzystać adres email z rekordu kontaktu w kodzie.

## Krok 4: użyj kodu Node.js

Przykładowa logika wygląda tak:

```js
const hubspot = require('@hubspot/api-client');

exports.main = async (event, callback) => {
  let contactFoundInExternalAPI = false;
  const email = event.inputFields['email'];

  const response = await fetch('https://your-api.example.com/test');
  const data = await response.json();

  if (data) {
    contactFoundInExternalAPI = data.includes(email);

    const hubspotClient = new hubspot.Client({
      accessToken: process.env.SECRET,
    });

    const contactID = event.object.objectId;

    await hubspotClient.crm.contacts.basicApi.update(contactID, {
      properties: {
        found_in_external_api: contactFoundInExternalAPI,
      },
    });
  }

  callback({
    outputFields: {
      contactFound: contactFoundInExternalAPI,
    }
  });
};
```

## Co robi ten kod

- pobiera email z input fields workflow
- odpytuje zewnętrzne API
- sprawdza, czy email znajduje się w zwróconych danych
- łączy się z HubSpot API przez Private App
- aktualizuje właściwość `found_in_external_api` na bieżącym kontakcie

## O czym trzeba pamiętać

### Nazwa właściwości

HubSpot zapisuje wewnętrzną nazwę właściwości z underscore, więc etykieta `Found in external API` może mieć internal name `found_in_external_api`.

### Obsługa błędów

W realnym wdrożeniu warto dodać:

- walidację odpowiedzi API
- obsługę błędów `fetch`
- timeouty
- logowanie wyjątków

### Bezpieczeństwo

Token Private App powinien być przechowywany wyłącznie jako secret w workflow, a nie wpisany na sztywno w kodzie.

## Kiedy to podejście ma sens

Ten model sprawdza się wtedy, gdy HubSpot ma reagować na dane z systemu, który nie jest natywnie zintegrowany, np.:

- własnego scoring API
- wewnętrznej bazy klientów
- zewnętrznego systemu weryfikacji
- narzędzia ryzyka, finansów lub operacji

## Podsumowanie

HubSpot Workflows z custom code daje dużą elastyczność. Jeśli potrzebujesz ustawiać właściwości kontaktu na podstawie danych z zewnętrznego API, to jest jedno z najpraktyczniejszych podejść, szczególnie gdy chcesz zachować pełną kontrolę nad logiką.

[Skontaktuj się z nami](/pl/kontakt/), jeśli chcesz wdrożyć podobny workflow w HubSpot.
