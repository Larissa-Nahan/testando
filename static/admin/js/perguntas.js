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
        function onChange() {
            var showElement = function(el, display) {
                el.style.display = display ? '' : 'none';
            };

            var pergunta = [];
            var criterio_pergunta = [];
            for(var j = 0; j < document.querySelector('#id_avaliacao_chefes').childElementCount; j++){
                pergunta[j] = document.querySelector('#id_avaliacao_chefes_'+[j]).nextSibling.nodeValue;
                criterio_pergunta[j] = pergunta[j].split(' ').splice(-2).join(" ");
                showElement($('label[for=id_avaliacao_chefes_'+[j]+']')[0], false);
            }

              
            
            for(var j = 0; j < document.querySelector('#id_avaliacao_chefes').childElementCount; j++){
                
                var text = dropdown_criterio.options[dropdown_criterio.selectedIndex].text;
                
                if(criterio_pergunta[j] == text){
                    // pergunta[j].setAttribute("hidden", false);
                    showElement($('label[for=id_avaliacao_chefes_'+[j]+']')[0], true);
                } else {
                    showElement($('label[for=id_avaliacao_chefes_'+[j]+']')[0], false);
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
