---
layout: base
title: Contact Sisivo
description: "Talk to Sisivo about pipeline chaos, qualification, and whether a CSV-based pilot makes sense for your team."
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
    <p class="contact-kicker">Start with one real pipeline</p>
    <h2 id="contact-intro-title">Tell us where deals are getting lost</h2>
    <p>
      Most teams reach out when the pipeline looks busy, but nobody trusts it. Stages are loose, follow-up drags on, and too many deals die after interest.
    </p>
    <ul class="contact-points">
      <li>We review whether ICP and qualification are too broad</li>
      <li>We check where stages and next-step discipline break down</li>
      <li>We assess whether a Sisivo pilot makes sense now or later</li>
    </ul>

    <h3>Best fit before the call</h3>
    <ul class="contact-steps">
      <li>You already have an active B2B pipeline.</li>
      <li>Someone owns sales, usually the founder or Head of Sales.</li>
      <li>You can export a recent CSV from your CRM.</li>
    </ul>
  </section>

<section class="contact-form-card" aria-labelledby="contact-form-title">
    <h2 id="contact-form-title">Request a pipeline review</h2>
    <p>
      Best for teams that want a clear answer on fit, likely ROI, and the next step toward a pilot.
    </p>
    <div id="lead-plan-context"></div>
    <div class="hubspot-form-wrap" id="hubspot-contact-form"></div>
  </section>
</div>

<script charset="utf-8" type="text/javascript" src="https://js-eu1.hsforms.net/forms/embed/v2.js"></script>
<script>
  (function () {
    const params = new URLSearchParams(window.location.search);
    if (params.get("intent") !== "lead-plan") return;

    const labels = [
      ["company", "Company"],
      ["website", "Website"],
      ["role", "Role"],
      ["team_type", "Team type"],
      ["workflow_to_improve", "Main workflow"],
      ["crm_system", "CRM / system"],
      ["monthly_lead_volume", "Monthly lead volume"],
      ["bottleneck", "Main bottleneck"],
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

    const summary = "Sisivo pipeline review request\n" + lines.join("\n");
    window.__leadPlanSummary = summary;

    const context = document.getElementById("lead-plan-context");
    if (!context) return;

    const panel = document.createElement("section");
    panel.className = "lead-plan-panel";
    panel.innerHTML = [
      "<p><strong>Pipeline review context detected.</strong> We pre-filled your notes so we can quickly assess fit and likely bottlenecks.</p>",
      "<ul class=\"lead-plan-list\">" + lines.map(function (line) { return "<li>" + line + "</li>"; }).join("") + "</ul>"
    ].join("");
    context.appendChild(panel);
  })();

  hbspt.forms.create({
    portalId: "144979550",
    formId: "642de580-8f23-4f25-909b-639fa30fcbe4",
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

<section class="content-page-cta" aria-label="Contact page CTA">
  <h2>Prefer a live conversation first?</h2>
  <p>Book a short call if you want to walk through your current sales setup before sending data.</p>
  <div class="home-cta">
    <a class="btn btn-primary" href="https://calendar.app.google/R21jua9szDGa7T7c9">{% ms "calendar_month" %}<span>Book Pipeline Review</span></a>
    <a class="btn btn-ghost btn-see-services" href="/services/ai-solutions-development/"><span>See the System</span><span class="btn-icon" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3.5 8H12.5" stroke-width="1.8" stroke-linecap="round" /><path d="M8.8 4.3L12.5 8L8.8 11.7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" /></svg></span></a>
  </div>
</section>

## Prefer direct contact?

Krystian Sulek  
Email: [krystian@easytechpartners.com](mailto:krystian@easytechpartners.com)  
LinkedIn: [linkedin.com/in/krystiansulek](https://www.linkedin.com/in/krystiansulek/)
