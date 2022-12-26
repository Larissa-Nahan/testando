django.jQuery = jQuery;

django.jQuery(document).ready(function () {
    if (document.querySelector('[name="_save"]')) {
        var liberar_avaliacao_usuario = document.querySelector('#id_nome-0-liberar_avaliacao');
        var liberar_avaliacao_colaborador = document.querySelector('#id_avaliarcolaborador-0-liberar_avaliacao');
        var btn_salvar = document.querySelector('[name="_save"]');

        btn_salvar.onclick = function () {
            liberar_avaliacao_usuario.checked = true
            liberar_avaliacao_colaborador.checked = true
        }
    }
})