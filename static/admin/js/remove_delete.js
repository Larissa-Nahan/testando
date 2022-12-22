django.jQuery = jQuery;

window.addEventListener('load', function () {
    django.jQuery(document).ready(function () {
        if (document.querySelector('[name="_save"]')) {
            var delete_button = document.querySelectorAll('.inline-deletelink');
            for(var i = 0; i < delete_button.length; i++){
                delete_button[i].remove()
            }
        }
    })
})
