// Логика для скрытия шапки и футера при прокрутке
let lastScrollTop = 0;
const header = document.querySelector('header');
const footer = document.querySelector('footer');

window.addEventListener('scroll', () => {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    // Скрытие шапки при прокрутке вниз и появление при прокрутке вверх
    if (scrollTop > lastScrollTop) {
        header.style.top = '-60px';  // Прячем шапку
        footer.style.bottom = '-60px'; // Прячем футер
    } else {
        header.style.top = '0';  // Показываем шапку
        footer.style.bottom = '0'; // Показываем футер
    }
    lastScrollTop = scrollTop;
});

// Бургер-меню для мобильных версий
const burgerMenu = document.getElementById('burgerMenu');
const navLinks = document.querySelector('.nav-links');

burgerMenu.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    burgerMenu.classList.toggle('toggle');
});



