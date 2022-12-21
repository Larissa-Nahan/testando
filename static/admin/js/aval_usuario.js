django.jQuery = jQuery;

django.jQuery(document).ready(function () {
    if (document.querySelector('[name="_save"]')) {
        const delete_button = document.querySelector('.inline-deletelink');
        delete_button.remove()

        var liberar_avaliacao = document.querySelector('#id_nome-0-liberar_avaliacao');
        var btn_salvar = document.querySelector('[name="_save"]');

        btn_salvar.onclick = function () {
            liberar_avaliacao.checked = true
        }
    }
})