
// Nav

      var nav = document.querySelector('nav');

      window.addEventListener('scroll', function () {
        if (window.pageYOffset > 50) {
          nav.classList.add('shadow');
        } else {
          nav.classList.remove('shadow');
        }
      });

// END NAV

new WOW().init();s