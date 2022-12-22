django.jQuery = jQuery;

window.addEventListener('load', function () {
    django.jQuery(document).ready(function () {
        if (document.querySelector('[name="_save"]')) {
            var selects = document.querySelectorAll('.field-escala');
            for(var i = 0; i < selects.length-1; i++){
                document.querySelector("#id_avaliacao_set-"+i+"-escala").selectedIndex = i+1;
            }
        }
    })
})
