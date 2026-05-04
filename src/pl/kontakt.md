---
layout: base
draft: true
locale: pl
title: Kontakt | Sisivo
heading: Kontakt
description: "Porozmawiajmy o wdrożeniu AI, agentach AI, RAG i automatyzacji procesów w Twojej firmie."
permalink: /pl/kontakt/
alternateLangs:
  en: /contact-us/
  pl: /pl/kontakt/
---

<div class="contact-layout">
  <section class="contact-intro" aria-labelledby="contact-intro-title">
    <figure class="contact-photo">
      <img
        src="/images/contact-us-krystian.jpg"
        alt="Krystian Sulek"
        width="1200"
        height="800"
        loading="lazy"
        decoding="async"
      />
    </figure>
    <p class="contact-kicker">Zacznij od procesu</p>
    <h2 id="contact-intro-title">Powiedz nam, co chcesz usprawnić przy pomocy AI</h2>
    <p>
      Najczęściej kontaktują się z nami firmy, które chcą skrócić czas pracy zespołu, uporządkować dostęp do wiedzy, przyspieszyć obsługę lub bezpiecznie wdrożyć AI w istniejących procesach.
    </p>
    <ul class="contact-points">
      <li>Wdrożenia AI dla firm i automatyzacja procesów</li>
      <li>Agenci AI dla sprzedaży, operacji i obsługi klienta</li>
      <li>RAG dla firm i praca na dokumentach oraz wiedzy organizacji</li>
    </ul>

    <h3>Co dzieje się dalej</h3>
    <ul class="contact-steps">
      <li>Analizujemy Twój proces i główny cel biznesowy.</li>
      <li>Wskazujemy najlepszy pierwszy zakres wdrożenia AI.</li>
      <li>Ustalamy systemy, harmonogram i sposób pomiaru efektów.</li>
    </ul>
  </section>

  <section class="contact-form-card" aria-labelledby="contact-form-title">
    <h2 id="contact-form-title">Formularz kontaktowy</h2>
    <p>
      Najlepsza opcja, jeśli chcesz dostać konkretną rekomendację, od czego zacząć wdrożenie AI w firmie.
    </p>
    <div id="lead-plan-context"></div>
    <div class="hubspot-form-wrap" id="hubspot-contact-form"></div>
  </section>
</div>

<script charset="utf-8" type="text/javascript" src="//js-eu1.hsforms.net/forms/embed/v2.js"></script>
<script>
  (function () {
    const params = new URLSearchParams(window.location.search);
    if (params.get("intent") !== "lead-plan") return;

    const labels = [
      ["company", "Firma"],
      ["website", "Strona"],
      ["role", "Rola"],
      ["team_type", "Typ zespolu"],
      ["workflow_to_improve", "Glowny proces"],
      ["crm_system", "CRM / system"],
      ["monthly_lead_volume", "Miesieczny wolumen leadow"],
      ["bottleneck", "Glowne waskie gardlo"],
      ["email", "Email"]
    ];

    const lines = [];
    labels.forEach(function (pair) {
      const key = pair[0];
      const label = pair[1];
      const value = (params.get(key) || "").trim();
      if (value) lines.push(label + ": " + value);
    });

    if (!lines.length) return;

    const summary = "Prosba o plan wdrozenia AI\n" + lines.join("\n");
    window.__leadPlanSummary = summary;

    const context = document.getElementById("lead-plan-context");
    if (!context) return;

    const panel = document.createElement("section");
    panel.className = "lead-plan-panel";
    panel.innerHTML = [
      "<p><strong>Wykryto kontekst zapytania.</strong> Uzupelnilismy podsumowanie ponizej, aby szybciej zaproponowac pierwszy zakres wdrozenia AI.</p>",
      "<ul class=\"lead-plan-list\">" + lines.map(function (line) { return "<li>" + line + "</li>"; }).join("") + "</ul>"
    ].join("");
    context.appendChild(panel);
  })();

  hbspt.forms.create({
    portalId: "144979550",
    formId: "f0baccb1-d32c-43a8-998c-1fcfbe6b8b15",
    region: "eu1",
    target: "#hubspot-contact-form",
    onFormReady: function ($form) {
      try {
        const summary = window.__leadPlanSummary;
        if (!summary) return;
        const formEl = $form && $form[0] ? $form[0] : null;
        if (!formEl) return;
        const messageField = formEl.querySelector("textarea");
        if (!messageField || messageField.value) return;
        messageField.value = summary;
        messageField.dispatchEvent(new Event("input", { bubbles: true }));
        messageField.dispatchEvent(new Event("change", { bubbles: true }));
      } catch (e) {
      }
    }
  });
</script>

<section class="content-page-cta" aria-label="Polish contact CTA">
  <h2>Wybierz kolejny krok</h2>
  <p>Umów konsultację, jeśli chcesz omówić proces na żywo, albo zacznij od wskazania obszaru, w którym AI ma dać realny efekt.</p>
  <div class="home-cta">
    <a class="btn btn-primary" href="https://calendar.app.google/R21jua9szDGa7T7c9">{% ms "calendar_month" %}<span>Umów konsultację</span></a>
    <a class="btn btn-ghost btn-see-services" href="/pl/wdrozenia-ai-dla-firm/"><span>Zobacz, od czego zacząć</span><span class="btn-icon" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3.5 8H12.5" stroke-width="1.8" stroke-linecap="round" /><path d="M8.8 4.3L12.5 8L8.8 11.7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" /></svg></span></a>
  </div>
</section>

## Preferujesz bezpośredni kontakt?

Krystian Sulek  
Telefon: [+48 505 316 553](tel:+48505316553)  
Email: [krystian@easytechpartners.com](mailto:krystian@easytechpartners.com)  
LinkedIn: [linkedin.com/in/krystiansulek](https://www.linkedin.com/in/krystiansulek/)
