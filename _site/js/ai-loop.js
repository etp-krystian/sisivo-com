(() => {
  const root = document.getElementById("ai-loop");
  if (!root) return;

  const prefersReducedMotion = window.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches;

  const buttons = Array.from(root.querySelectorAll(".ai-loop-step"));
  const progress = root.querySelector(".ai-loop-progress");
  const currentStep = root.querySelector("#ai-loop-current-step");

  if (!buttons.length) return;

  let active = 0;
  let timer = null;
  let resumeTimer = null;

  const setProgress = (index) => {
    if (!progress) return;
    const r = progress.r?.baseVal?.value;
    if (!r) return;
    const circumference = 2 * Math.PI * r;
    progress.style.strokeDasharray = `${circumference}`;
    const t = buttons.length <= 1 ? 1 : index / (buttons.length - 1);
    progress.style.strokeDashoffset = `${circumference * (1 - t)}`;
  };

  const setActive = (index, { userInitiated = false } = {}) => {
    active = ((index % buttons.length) + buttons.length) % buttons.length;

    for (const button of buttons) {
      const isActive = Number(button.dataset.step) === active;
      button.classList.toggle("is-active", isActive);
      if (isActive) {
        button.setAttribute("aria-current", "step");
      } else {
        button.removeAttribute("aria-current");
      }
    }

    setProgress(active);
    if (currentStep) {
      const activeButton = buttons.find((b) => Number(b.dataset.step) === active) || buttons[active];
      const title = activeButton?.querySelector(".ai-loop-step-title")?.textContent?.trim();
      if (title) currentStep.textContent = title;
    }

    if (userInitiated && !prefersReducedMotion) {
      clearInterval(timer);
      timer = null;
      clearTimeout(resumeTimer);
      resumeTimer = setTimeout(startAuto, 8000);
    }
  };

  const next = () => setActive(active + 1);

  const startAuto = () => {
    if (prefersReducedMotion) return;
    if (timer) return;
    timer = window.setInterval(next, 2200);
  };

  for (const button of buttons) {
    button.addEventListener("click", () => {
      setActive(Number(button.dataset.step), { userInitiated: true });
    });
  }

  // Initial
  setActive(0);
  startAuto();
})();
