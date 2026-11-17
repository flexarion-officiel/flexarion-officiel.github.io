/* Reconstitue l'adresse e-mail (masquée aux robots collecteurs). */
(function(){var a=document.getElementById("email");if(!a)return;var m=a.getAttribute("data-u")+"@"+a.getAttribute("data-d");a.href="mailto:"+m;a.textContent=m;})();
