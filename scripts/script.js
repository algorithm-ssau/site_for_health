var angle = 0;
var b = $('.navigation_bar');
function galleryspin(sign) {
spinner = document.querySelector(".scroll");
if (!sign) { angle = angle + 45; } else { angle = angle - 45; }
spinner.setAttribute("style","-webkit-transform: rotateY("+ angle +"deg); -moz-transform: rotateY("+ angle +"deg); transform: rotateY("+ angle +"deg);");
}
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