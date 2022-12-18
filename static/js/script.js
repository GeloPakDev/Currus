/* /* Main */


try {
    var slogan = document.getElementById('slogan');
    var text = slogan.innerHTML;
    slogan.innerHTML = '';
    var i = 0;
} catch (error) {
    console.log("OKOK");
}


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
/* Login scroll button */

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
        }, 100)
        
    });
});
/* Login scroll button */

