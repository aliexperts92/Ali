/* =========================================================================
   Signature Restaurant — vanilla JS
   - Transparent -> solid nav on scroll
   - Mobile full-screen menu toggle
   - Scroll-reveal via IntersectionObserver
   - Gallery lightbox (keyboard accessible)
   - Current year in footer
   ========================================================================= */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    initNav();
    initMobileMenu();
    initScrollReveal();
    initLightbox();
    initYear();
  });

  /* ----------------------------------------------------------------- */
  function initNav() {
    var nav = document.getElementById("site-nav");
    if (!nav) return;

    var threshold = 60;
    function onScroll() {
      if (window.scrollY > threshold) {
        nav.classList.add("is-solid");
      } else {
        nav.classList.remove("is-solid");
      }
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ----------------------------------------------------------------- */
  function initMobileMenu() {
    var toggle = document.getElementById("nav-toggle");
    var menu = document.getElementById("mobile-menu");
    if (!toggle || !menu) return;

    function close() {
      menu.classList.remove("is-open");
      menu.setAttribute("aria-hidden", "true");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open menu");
      document.body.classList.remove("menu-open");
    }
    function open() {
      menu.classList.add("is-open");
      menu.setAttribute("aria-hidden", "false");
      toggle.setAttribute("aria-expanded", "true");
      toggle.setAttribute("aria-label", "Close menu");
      document.body.classList.add("menu-open");
    }

    toggle.addEventListener("click", function () {
      if (menu.classList.contains("is-open")) {
        close();
      } else {
        open();
      }
    });

    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", close);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) close();
    });
  }

  /* ----------------------------------------------------------------- */
  function initScrollReveal() {
    var items = document.querySelectorAll(".reveal");
    if (!items.length) return;

    var reduce =
      window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (reduce || !("IntersectionObserver" in window)) {
      items.forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );

    items.forEach(function (el) {
      observer.observe(el);
    });
  }

  /* ----------------------------------------------------------------- */
  function initLightbox() {
    var triggers = document.querySelectorAll("[data-lightbox]");
    var box = document.getElementById("lightbox");
    if (!triggers.length || !box) return;

    var imgEl = document.getElementById("lightbox-img");
    var capEl = document.getElementById("lightbox-caption");
    var closeBtn = document.getElementById("lightbox-close");
    var lastFocused = null;

    function open(src, alt) {
      lastFocused = document.activeElement;
      imgEl.setAttribute("src", src);
      imgEl.setAttribute("alt", alt || "");
      capEl.textContent = alt || "";
      box.classList.add("is-open");
      box.setAttribute("aria-hidden", "false");
      document.body.classList.add("menu-open");
      closeBtn.focus();
    }
    function close() {
      box.classList.remove("is-open");
      box.setAttribute("aria-hidden", "true");
      document.body.classList.remove("menu-open");
      imgEl.setAttribute("src", "");
      if (lastFocused) lastFocused.focus();
    }

    triggers.forEach(function (el) {
      el.addEventListener("click", function () {
        open(el.getAttribute("data-lightbox"), el.getAttribute("data-alt"));
      });
      el.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          open(el.getAttribute("data-lightbox"), el.getAttribute("data-alt"));
        }
      });
    });

    closeBtn.addEventListener("click", close);
    box.addEventListener("click", function (e) {
      if (e.target === box) close();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && box.classList.contains("is-open")) close();
    });
  }

  /* ----------------------------------------------------------------- */
  function initYear() {
    var el = document.getElementById("year");
    if (el) el.textContent = new Date().getFullYear();
  }
})();
