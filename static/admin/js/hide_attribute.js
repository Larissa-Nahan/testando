django.jQuery = jQuery;

hide_nivel = true;
django.jQuery(document).ready(function(){
    if (django.jQuery('#id_efetivo').is(':checked')) {
        django.jQuery("#id_nivel").attr('disabled', false);
        hide_nivel = false;
    } else {
        django.jQuery("#id_nivel").attr('disabled', true);
        hide_nivel = true;
    }
    django.jQuery("#id_efetivo").click(function(){
        hide_nivel =! hide_nivel;
        if (hide_nivel) {
            django.jQuery("#id_nivel").attr('disabled', true);
        } else {
            django.jQuery("#id_nivel").attr('disabled',false);
        }
    })
})
