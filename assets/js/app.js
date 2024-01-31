
setTimeout(function() {
    var message_timeout = document.getElementById('message-time');
    if(message_timeout){
        message_timeout.style.display = 'none';
    }
}, 3000);


document.onreadystatechange = function () {
    var state = document.readyState;
    if (state == 'loading') {
        document.getElementById('preloader-spin').classList.add('show');
    } else if (state == 'complete') {
        setTimeout(function () {
            document.getElementById('preloader-spin').classList.remove('show');
        }, 50);
    }
}