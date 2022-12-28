django.jQuery = jQuery;

window.addEventListener('load', function () {
    django.jQuery(document).ready(function () {
        
        var inicio = document.querySelector('#content-main').querySelector('#avaliarcolaborador_form').querySelector('.module');
        var campo_criterio = document.querySelector('.field-criterio');
        var fieldsets = document.querySelectorAll('fieldset');
        fieldsets[1].insertAdjacentHTML('afterbegin', campo_criterio.innerHTML);
        inicio.after(fieldsets[1])
        
        campo_criterio.remove()
        document.querySelector('label[for="id_criterio"]').remove();
        $('h2')[1].remove();
        
        $('div[data-model-ref="criterio"]').unwrap();
        $('div[data-model-ref="criterio"]').replaceWith( "<h2>" + $('div[data-model-ref="criterio"]').html() + "</h2>" );
        
        var dropdown_criterio = document.querySelector('#id_criterio');

        var showElement = function(el, display) {
            el.style.display = display ? '' : 'none';
        };

        var perguntas = [];
        var topicos = [];
        var criterios = [];
        var input = [];
        for(var j = 0; j < document.querySelector('#id_avaliacao_chefes').childElementCount; j++){
            topicos[j] = $('label[for=id_avaliacao_chefes_'+[j]+']')[0]
            criterios[j] = topicos[j].innerText.split(' ').splice(-2).join(" ");
            perguntas[j] = topicos[j].innerText.split(" - ")
            topicos[j].value = criterios[j]
            input[j] = $('#id_avaliacao_chefes_'+[j])[0]
            topicos[j].innerHTML = perguntas[j][1]
            topicos[j].insertBefore(input[j], topicos[j].firstChild);
            console.log(topicos[j].innerHTML)
            showElement($('label[for=id_avaliacao_chefes_'+[j]+']')[0], false);
        }

        function onChange() {
            var text = dropdown_criterio.options[dropdown_criterio.selectedIndex].text;
            for(var j = 0; j < document.querySelector('#id_avaliacao_chefes').childElementCount; j++){
                if(criterios[j] === text){
                    showElement(topicos[j], true);
                } else {
                    showElement(topicos[j], false);
                }
            }
        }
        dropdown_criterio.onchange = onChange;
        onChange();

    })
})
