document.addEventListener("DOMContentLoaded", function () {
    let newsItems = document.querySelectorAll(".telegram-news-item");
    let currentIndex = 0;
    let autoSwitchInterval;

    function showNews(index) {
        newsItems.forEach((item, i) => {
            item.style.display = i === index ? "block" : "none";
        });
    }

    function startAutoSwitch() {
        stopAutoSwitch(); // На всякий случай очищаем, чтобы избежать дублирования
        autoSwitchInterval = setInterval(function () {
            currentIndex = (currentIndex < newsItems.length - 1) ? currentIndex + 1 : 0;
            showNews(currentIndex);
        }, 10000);
    }

    function stopAutoSwitch() {
        clearInterval(autoSwitchInterval);
    }

    // Управление навигационными кнопками
    document.getElementById("telegram-prev-news").addEventListener("click", function () {
        stopAutoSwitch();
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : newsItems.length - 1;
        showNews(currentIndex);
        startAutoSwitch(); // Перезапуск авто-смены после ручного переключения
    });

    document.getElementById("telegram-next-news").addEventListener("click", function () {
        stopAutoSwitch();
        currentIndex = (currentIndex < newsItems.length - 1) ? currentIndex + 1 : 0;
        showNews(currentIndex);
        startAutoSwitch(); // Перезапуск авто-смены после ручного переключения
    });

    // Обработка событий проигрывания видео
    newsItems.forEach((item) => {
        const videoElement = item.querySelector("video");
        if (videoElement) {
            videoElement.addEventListener("play", function () {
                stopAutoSwitch(); // Остановить авто-смену при проигрывании видео
            });
            videoElement.addEventListener("pause", function () {
                startAutoSwitch(); // Возобновить авто-смену при паузе
            });
            videoElement.addEventListener("ended", function () {
                startAutoSwitch(); // Возобновить авто-смену при завершении видео
            });
        }
    });

    // Начать показ первой новости
    showNews(currentIndex);
    startAutoSwitch(); // Начать автоматическую смену новостей
});
