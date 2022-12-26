django.jQuery = jQuery;

window.addEventListener('load', function () {
    django.jQuery(document).ready(function () {
        
        var inicio = document.querySelector('#content-main').querySelector('#avaliarcolaborador_form').querySelector('.module');
        var campo_criterio = document.querySelector('.field-criterio');
        var field = document.createElement('fieldset');
        field.classList.add('module', 'aligned')
        field.innerHTML = '<h2>' + campo_criterio.innerHTML + '</h2>';
        inicio.after(field)
        
        campo_criterio.remove()
        document.querySelector('label[for="id_criterio"]').remove();
        
        var dropdown_criterio = document.querySelector('#id_criterio');
        // console.log(dropdown_criterio.value.options)
        
        function onChange() {
        for(var j = 0; j < document.querySelector('#id_avaliacao_chefes').childElementCount; j++){
            // for(var i = 1; i < dropdown_criterio.length; i++){
                var pergunta = document.querySelector('#id_avaliacao_chefes_'+[j]).nextSibling.nodeValue;
                var criterio_pergunta = pergunta.split(' ').splice(-2).join(" ");
                
                    var value = dropdown_criterio.value;
                    var text = dropdown_criterio.options[dropdown_criterio.selectedIndex].text;
                    
                    if(criterio_pergunta == text){
                        console.log("as");
                        
                    }
                }
                // console.log(lastWord);
                
                // if(dropdown_criterio.option == )
                // console.log(str)
                
                // console.log(j)
                // document.querySelector(".id_criterio").selectedIndex = i+1;
            }
            dropdown_criterio.onchange = onChange;
            onChange();
        // }
        
        // if (document.querySelector('[name="_save"]')) {
        //     var selects = document.querySelectorAll('.field-escala');
        //     for(var i = 0; i < selects.length-1; i++){
        //         document.querySelector("#id_avaliacao_set-"+i+"-escala").selectedIndex = i+1;
        //     }
        // }

    })
})
