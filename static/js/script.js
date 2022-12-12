/* /* Main */
var slogan = document.querySelector('.slogan');
var text = slogan.innerHTML
slogan.innerHTML = '';
var i = 0;


function print_slogan () {
    slogan.innerHTML += text.charAt(i);
    i++;
    if (text.length == i) {
        clearInterval(timer);
    }
    console.log(i);
}
var timer = setInterval(print_slogan, 50)
/* Main */
/* Scroll button */
$(document).ready(function () {
    $(window).scroll(function () { 
        if ($(this).scrollTop() > 500) {
            $('#top').fadeIn();
            
        }
        else{
            $('#top').fadeOut();
        }   
    });
    $('#top').click(function () { 
        $('html').animate({
            scrollTop: 0
        }, 1000)
        
    });
});
/* Scroll button */ 

