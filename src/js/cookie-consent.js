(() => {
  const CONSENT_KEY = "etp_cookie_consent_v1";
  const CONSENT_TTL_DAYS = 180;

  const banner = document.getElementById("cookie-banner");
  const fab = document.getElementById("cookie-fab");
  const acceptButton = document.querySelector("[data-cookie-accept]");
  const rejectButton = document.querySelector("[data-cookie-reject]");
  const customizeButton = document.querySelector("[data-cookie-customize]");
  const settingsPanel = document.getElementById("cookie-settings");
  const analyticsToggle = document.getElementById("cookie-analytics-toggle");

  const now = () => Date.now();

  const readConsent = () => {
    try {
      const raw = localStorage.getItem(CONSENT_KEY);
      if (!raw) return null;
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") return null;
      if (!parsed.ts || typeof parsed.ts !== "number") return null;
      const maxAgeMs = CONSENT_TTL_DAYS * 24 * 60 * 60 * 1000;
      if (now() - parsed.ts > maxAgeMs) return null;
      return parsed;
    } catch {
      return null;
    }
  };

  const writeConsent = (consent) => {
    try {
      localStorage.setItem(
        CONSENT_KEY,
        JSON.stringify({
          analytics: Boolean(consent.analytics),
          ts: now(),
        })
      );
    } catch {
      // ignore
    }
  };

  const showBanner = () => {
    if (!banner) return;
    banner.hidden = false;
    if (fab) fab.hidden = true;
  };

  const hideBanner = () => {
    if (!banner) return;
    banner.hidden = true;
    if (fab) fab.hidden = false;
  };

  const syncToggle = (consent) => {
    if (!analyticsToggle) return;
    analyticsToggle.checked = Boolean(consent && consent.analytics);
    const switchEl = analyticsToggle.closest(".cookie-switch");
    if (switchEl) switchEl.classList.toggle("is-on", analyticsToggle.checked);
  };

  analyticsToggle?.addEventListener("change", () => {
    const next = { analytics: Boolean(analyticsToggle?.checked) };

    const switchEl = analyticsToggle.closest(".cookie-switch");
    if (switchEl) switchEl.classList.toggle("is-on", analyticsToggle.checked);

    writeConsent(next);
    applyConsent(next);
    hideBanner();
  });

  const applyConsent = (consent) => {
    void consent;
  };

  const init = () => {
    // Default: no analytics unless explicitly accepted.
    const existing = readConsent();
    if (existing) {
      applyConsent(existing);
      syncToggle(existing);
      hideBanner();
      return;
    }

    applyConsent({ analytics: false });
    syncToggle({ analytics: false });
    if (fab) fab.hidden = true;
    if (settingsPanel) settingsPanel.hidden = true;
    showBanner();
  };

  acceptButton?.addEventListener("click", () => {
    const consent = { analytics: true };
    writeConsent(consent);
    applyConsent(consent);
    syncToggle(consent);
    if (settingsPanel) settingsPanel.hidden = true;
    hideBanner();
  });

  rejectButton?.addEventListener("click", () => {
    const consent = { analytics: false };
    writeConsent(consent);
    applyConsent(consent);
    syncToggle(consent);
    if (settingsPanel) settingsPanel.hidden = true;
    hideBanner();
  });

  customizeButton?.addEventListener("click", () => {
    showBanner();
    const existing = readConsent() || { analytics: false };
    syncToggle(existing);
    if (settingsPanel) settingsPanel.hidden = !settingsPanel.hidden;
  });

  fab?.addEventListener("click", () => {
    showBanner();
    const existing = readConsent() || { analytics: false };
    syncToggle(existing);
    if (settingsPanel) settingsPanel.hidden = false;
  });

  init();
})();
