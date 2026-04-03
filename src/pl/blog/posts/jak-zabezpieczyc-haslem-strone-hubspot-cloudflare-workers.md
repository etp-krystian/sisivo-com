---
title: "Jak zabezpieczyć hasłem stronę HubSpot przy użyciu Cloudflare Workers"
description: Jak dodać ochronę hasłem do strony HubSpot przy użyciu Cloudflare Workers i Basic Auth. Prosty sposób na zabezpieczenie preview lub stagingu.
date: 2025-04-11
image: /images/blog/how-to-password-protect-a-hubspot-website.jpg
imageAlt: "Jak zabezpieczyć hasłem stronę HubSpot przy użyciu Cloudflare Workers"
imageWidth: 1200
imageHeight: 628
tags:
  - hubspot
  - cloudflare
  - security
  - postPl
alternateLangs:
  en: /en/blog/how-to-password-protect-a-hubspot-website-using-cloudflare-workers/
  pl: /pl/blog/jak-zabezpieczyc-haslem-strone-hubspot-cloudflare-workers/
---

HubSpot bardzo dobrze nadaje się do hostowania stron marketingowych, ale nie daje prostego sposobu na zabezpieczenie hasłem całej witryny, bloga czy środowiska testowego. Standardowo można chronić tylko landing pages.

Jeśli chcesz ograniczyć dostęp do stagingu, wersji podglądowej albo strony tylko dla klienta, możesz zrobić to przy użyciu Cloudflare Workers.

## Kiedy to rozwiązanie ma sens

To podejście sprawdza się, gdy:

- chcesz ukryć staging przed przypadkowymi odwiedzającymi
- potrzebujesz dostępu tylko dla klienta lub wewnętrznego zespołu
- nie masz własnego backendu i chcesz dodać prostą warstwę autoryzacji

## Krok 1: podłącz domenę do Cloudflare

Załóż konto w Cloudflare i przejdź przez proces podłączenia domeny. Będziesz musiał zmienić nameservery u rejestratora domeny, aby Cloudflare zarządzał DNS-em.

Następnie zaloguj się do HubSpot i dodaj domenę w `Settings -> Website -> Domains & URLs`. Skopiuj rekordy DNS z HubSpot do ustawień DNS w Cloudflare.

Ważne: rekord `www` powinien być proxied, czyli mieć włączoną pomarańczową chmurkę. Bez tego Worker nie zadziała.

## Krok 2: utwórz Worker z Basic Auth

W panelu Cloudflare przejdź do `Workers & Pages`, wybierz utworzenie nowej aplikacji i stwórz Workera HTTP.

Wklej kod podobny do poniższego:

```js
addEventListener("fetch", event => {
  event.respondWith(handleRequest(event.request))
})

const username = "admin"
const password = "secretpassword"
const encoded = btoa(`${username}:${password}`)

async function handleRequest(request) {
  const authHeader = request.headers.get("Authorization")

  if (!authHeader || authHeader !== `Basic ${encoded}`) {
    return new Response("Unauthorized", {
      status: 401,
      headers: {
        "WWW-Authenticate": 'Basic realm="Protected Area"',
      },
    })
  }

  return fetch(request)
}
```

Po zapisaniu i wdrożeniu Worker będzie wymagał loginu i hasła przed wpuszczeniem użytkownika na stronę.

## Krok 3: podepnij Workera do adresu URL

Dodaj route w formacie:

```txt
www.twojadomena.pl/*
```

Jeszcze raz upewnij się, że rekord `www` jest proxied. Jeśli nie, Worker nie będzie obsługiwał ruchu.

## Co dostajesz

To rozwiązanie nie wymaga backendu, nie wymaga ingerencji w HubSpot po stronie hostingu i dobrze sprawdza się jako szybka ochrona środowisk testowych.

## O czym warto pamiętać

- to prosty Basic Auth, więc nadaje się głównie do stagingu i środowisk roboczych
- dla bardziej zaawansowanych scenariuszy warto rozważyć mocniejszą kontrolę dostępu
- dobrze jest zarządzać danymi dostępowymi poza kodem, np. przez sekrety w Cloudflare

## Podsumowanie

Jeśli potrzebujesz szybko zabezpieczyć stronę HubSpot hasłem, Cloudflare Workers daje czyste i praktyczne rozwiązanie bez stawiania backendu.

[Skontaktuj się z nami](/pl/kontakt/), jeśli chcesz wdrożyć podobne rozwiązanie na swojej stronie HubSpot.
