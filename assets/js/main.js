/*
 * Flexarion — script unique, chargé en « defer ».
 * 1. Menu burger (mobile)
 * 2. Bouton « retour en haut »
 * 3. Reconstitution de l'adresse e-mail masquée (page contact)
 */
(function () {
  "use strict";

  // 1. Menu burger
  var burger = document.querySelector(".burger");
  var menu = document.getElementById("menu-principal");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = burger.getAttribute("aria-expanded") === "true";
      burger.setAttribute("aria-expanded", String(!open));
      burger.setAttribute("aria-label", open ? "Ouvrir le menu" : "Fermer le menu");
      menu.classList.toggle("is-open", !open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && burger.getAttribute("aria-expanded") === "true") {
        burger.click();
        burger.focus();
      }
    });
  }

  // 2. Retour en haut (le défilement doux est géré en CSS et respecte prefers-reduced-motion)
  var toTop = document.querySelector(".to-top");
  if (toTop) {
    var update = function () {
      toTop.classList.toggle("is-visible", window.scrollY > 300);
    };
    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  // 3. Adresse e-mail
  var email = document.getElementById("email");
  if (email) {
    var address = email.getAttribute("data-u") + "@" + email.getAttribute("data-d");
    email.href = "mailto:" + address;
    email.textContent = address;
  }
})();
