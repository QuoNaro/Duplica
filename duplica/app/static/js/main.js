
$(document).ready(function() {
    
    // Получаем текущий URL
    var currentUrl = window.location.pathname;
    console.log(currentUrl)

    // Убираем класс active у всех ссылок
    $('.link').removeClass('active');

    // Проверяем, соответствует ли текущий URL какому-либо id
    $('.link').each(function() {
        var linkId = $(this).attr('id');
        if (currentUrl.includes(linkId)) {
            $(this).addClass('active'); // Добавляем класс active к соответствующей ссылке
        }
    });
});

