/* Main */
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