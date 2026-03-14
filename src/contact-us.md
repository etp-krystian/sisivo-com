---
layout: base
title: Contact
description: "Talk to us about lead qualification, inbound automation, and revenue workflow AI."
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
    <p class="contact-kicker">Start with your workflow</p>
    <h2 id="contact-intro-title">Tell us what your revenue team wants to automate</h2>
    <p>
      Most teams contact us when lead qualification is slow, sales context is incomplete, or pipeline admin takes too much time.
    </p>
    <ul class="contact-points">
      <li>Inbound lead qualification and routing</li>
      <li>Sales research and account enrichment</li>
      <li>Revenue workflow automation across CRM, forms, and email</li>
    </ul>

    <h3>What happens next</h3>
    <ul class="contact-steps">
      <li>We review your current workflow and goal.</li>
      <li>We suggest the best first implementation scope.</li>
      <li>We align on timeline, systems, and success metrics.</li>
    </ul>
  </section>

<section class="contact-form-card" aria-labelledby="contact-form-title">
    <h2 id="contact-form-title">Contact form</h2>
    <p>
      Best for teams that want a concrete recommendation on what to automate first.
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

    const summary = "AI lead qualification plan request\n" + lines.join("\n");
    window.__leadPlanSummary = summary;

    const context = document.getElementById("lead-plan-context");
    if (!context) return;

    const panel = document.createElement("section");
    panel.className = "lead-plan-panel";
    panel.innerHTML = [
      "<p><strong>Plan request detected.</strong> We pre-filled your context below so we can recommend the best first AI workflow for your team.</p>",
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

<section class="content-page-cta" aria-label="Contact page call to action">
  <h2>Choose your next step</h2>
  <p>Book a discovery call if you want to discuss your workflow live, or get your AI lead qualification plan first.</p>
  <div class="home-cta">
    <a class="btn btn-primary" href="https://calendar.app.google/R21jua9szDGa7T7c9">{% ms "calendar_month" %}<span>Book a discovery call</span></a>
    <a class="btn btn-ghost btn-see-services" href="/ai-lead-qualification-plan/"><span>Get your AI lead qualification plan</span><span class="btn-icon" aria-hidden="true"><svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3.5 8H12.5" stroke-width="1.8" stroke-linecap="round" /><path d="M8.8 4.3L12.5 8L8.8 11.7" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" /></svg></span></a>
  </div>
</section>

## Prefer direct contact?

Krystian Sulek  
Email: [krystian@easytechpartners.com](mailto:krystian@easytechpartners.com)  
LinkedIn: [linkedin.com/in/krystiansulek](https://www.linkedin.com/in/krystiansulek/)
