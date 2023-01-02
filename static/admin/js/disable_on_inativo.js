django.jQuery = jQuery;

inativo = false;

// rever estrategia
django.jQuery(document).ready(function(){
    if (django.jQuery('#id_inativo').is(':checked')) {
        django.jQuery("#id_usuario").attr('disabled', true);
        django.jQuery("#id_cpf").attr('disabled', true);
        django.jQuery("#id_matricula").attr('disabled', true);
        django.jQuery("#id_email").attr('disabled', true);
        django.jQuery("#id_data_admissao_usuario").attr('disabled', true);
        django.jQuery("#id_efetivo").attr('disabled', true);
        django.jQuery("#id_nivel").attr('disabled', true);
        django.jQuery("#id_diretoria").attr('disabled', true);
        django.jQuery("#id_gerencia").attr('disabled', true);
        django.jQuery("#id_funcao").attr('disabled', true);
        django.jQuery("#id_classe").attr('disabled', true);
        django.jQuery("#id_setor").attr('disabled', true);
        django.jQuery("#id_cargo").attr('disabled', true);
        inativo = true;
    } else {
        django.jQuery("#id_usuario").attr('disabled', false);
        django.jQuery("#id_cpf").attr('disabled', false);
        django.jQuery("#id_matricula").attr('disabled', false);
        django.jQuery("#id_email").attr('disabled', false);
        django.jQuery("#id_data_admissao_usuario").attr('disabled', false);
        django.jQuery("#id_efetivo").attr('disabled', false);
        django.jQuery("#id_nivel").attr('disabled', false);
        django.jQuery("#id_diretoria").attr('disabled', false);
        django.jQuery("#id_gerencia").attr('disabled', false);
        django.jQuery("#id_funcao").attr('disabled', false);
        django.jQuery("#id_classe").attr('disabled', false);
        django.jQuery("#id_setor").attr('disabled', false);
        django.jQuery("#id_cargo").attr('disabled', false);
        inativo = false;
    }
    django.jQuery("#id_inativo").click(function(){
        inativo =! inativo;
        if (inativo) {
            django.jQuery("#id_usuario").attr('disabled', true);
            django.jQuery("#id_cpf").attr('disabled', true);
            django.jQuery("#id_matricula").attr('disabled', true);
            django.jQuery("#id_email").attr('disabled', true);
            django.jQuery("#id_data_admissao_usuario").attr('disabled', true);
            django.jQuery("#id_efetivo").attr('disabled', true);
            django.jQuery("#id_nivel").attr('disabled', true);
            django.jQuery("#id_diretoria").attr('disabled', true);
            django.jQuery("#id_gerencia").attr('disabled', true);
            django.jQuery("#id_funcao").attr('disabled', true);
            django.jQuery("#id_classe").attr('disabled', true);
            django.jQuery("#id_setor").attr('disabled', true);
            django.jQuery("#id_cargo").attr('disabled', true);
        } else {
            django.jQuery("#id_usuario").attr('disabled',false);
            django.jQuery("#id_cpf").attr('disabled', false);
            django.jQuery("#id_matricula").attr('disabled', false);
            django.jQuery("#id_email").attr('disabled', false);
            django.jQuery("#id_data_admissao_usuario").attr('disabled', false);
            django.jQuery("#id_efetivo").attr('disabled', false);
            django.jQuery("#id_nivel").attr('disabled', false);
            django.jQuery("#id_diretoria").attr('disabled', false);
            django.jQuery("#id_gerencia").attr('disabled', false);
            django.jQuery("#id_funcao").attr('disabled', false);
            django.jQuery("#id_classe").attr('disabled', false);
            django.jQuery("#id_setor").attr('disabled', false);
            django.jQuery("#id_cargo").attr('disabled', false);
        }
    })
})
