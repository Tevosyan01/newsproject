document.addEventListener('DOMContentLoaded', function() {
        const menuToggle = document.querySelector('.menu-toggle');
        const navLinks = document.querySelector('.nav-links');

        /* Переключение класса 'active' для меню и бургер-меню */
        menuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            menuToggle.classList.toggle('active'); /* Анимация для бургер-меню */
        });

        /* Закрытие меню при клике на ссылку */
        document.querySelectorAll('.nav-links a').forEach(function(link) {
            link.addEventListener('click', function() {
                navLinks.classList.remove('active');
                menuToggle.classList.remove('active'); /* Убираем анимацию */
            });
        });
    });