// var angle = 0;
// function galleryspin(sign) {
// spinner = document.querySelector(".scroll");
// if (!sign) { angle = angle + 45; } else { angle = angle - 45; }
// spinner.setAttribute("style","-webkit-transform: rotateY("+ angle +"deg); -moz-transform: rotateY("+ angle +"deg); transform: rotateY("+ angle +"deg);");
// }
$(window).on('scroll',function(){
    if ($(this).scrollTop() > 100) {
        $('.navigation_bar').fadeOut();
        $('.icon_menu').fadeIn();
    }
    else {
        $('.navigation_bar').fadeIn();
        $('.icon_menu').fadeOut();

    }
});
function clickMenu() {
    $('.icon_menu').fadeOut();
    $('.navigation_bar').fadeIn().css("display","block");
}
var slideIndex = 1;
showSlides(slideIndex);
/* Индекс слайда по умолчанию */


/* Функция увеличивает индекс на 1, показывает следующй слайд*/
function plusSlide() {
    showSlides(slideIndex += 1);
}

/* Функция уменьшяет индекс на 1, показывает предыдущий слайд*/
function minusSlide() {
    showSlides(slideIndex -= 1);
}

/* Устанавливает текущий слайд */
function currentSlide(n) {
    showSlides(slideIndex = n);
}

/* Основная функция сладера */
function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("item");
    var dots = document.getElementsByClassName("slider-dots_item");
    if (n > slides.length) {
      slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}
