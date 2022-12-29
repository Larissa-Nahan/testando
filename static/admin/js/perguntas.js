django.jQuery = jQuery;

window.addEventListener('load', function () {
    django.jQuery(document).ready(function () {
        // pega o campo criterio (inicialmente junto com os dados do usuario)
        var inicio = document.querySelector('#content-main').querySelector('#avaliarcolaborador_form').querySelector('.module');
        var campo_criterio = document.querySelector('.field-criterio');
        var fieldsets = document.querySelectorAll('fieldset');
        fieldsets[1].insertAdjacentHTML('afterbegin', campo_criterio.innerHTML);
        inicio.after(fieldsets[1])
        
        // remove o campo de criterio da parte do usuario e deleta o conteudo anterior
        campo_criterio.remove()
        document.querySelector('label[for="id_criterio"]').remove();
        $('h2')[1].remove();

        // insere o campo no h2 titulo
        $('div[data-model-ref="criterio"]').unwrap();
        $('div[data-model-ref="criterio"]').replaceWith( "<h2>" + $('div[data-model-ref="criterio"]').html() + "</h2>" );
        
        // cria os btn e add ids
        const btn_seta_esquerda = document.createElement("button");
        const btn_seta_direita = document.createElement("button");
        btn_seta_esquerda.setAttribute("id", "btn_seta_esquerda")
        btn_seta_direita.setAttribute("id", "btn_seta_direita")
        // cria as imagens e add a scr + tamanho
        const seta_esquerda = document.createElement("img");
        const seta_direita = document.createElement("img");
        seta_esquerda.src = "/static/admin/imgs/arrow_left.png" 
        seta_direita.src = "/static/admin/imgs/arrow_right.png"
        seta_esquerda.height = 25
        seta_direita.height = 25

        // coloca as imgs dentro dos btn e os insere ao lado do criterio no h2
        btn_seta_esquerda.appendChild(seta_esquerda)
        btn_seta_direita.appendChild(seta_direita)
        $("#id_criterio")[0].after(btn_seta_esquerda);
        btn_seta_esquerda.after(btn_seta_direita);

        var dropdown_criterio = document.querySelector('#id_criterio');

        // funcao para exibir ou esconder as perguntas
        var showElement = function(el, display) {
            el.style.display = display ? '' : 'none';
        };

        var perguntas = [];
        var topicos = [];
        var criterios = [];
        var input = [];
        for(var j = 0; j < document.querySelector('#id_avaliacao_chefes').childElementCount; j++){
            topicos[j] = $('label[for=id_avaliacao_chefes_'+[j]+']')[0]
            criterios[j] = topicos[j].innerText.split(' ').splice(-2).join(" ");  // pega e armazena somente o critério
            perguntas[j] = topicos[j].innerText.split(" - ")  // divide o que vem escrito [escala - pergunta - criterio]
            input[j] = $('#id_avaliacao_chefes_'+[j])[0]
            topicos[j].innerHTML = perguntas[j][1]  // suubstitui o conteudo anterior por somente as perguntas
            topicos[j].insertBefore(input[j], topicos[j].firstChild);  // insere o input (checkbox) no inicio das perguntas
            showElement($('label[for=id_avaliacao_chefes_'+[j]+']')[0], false);
        }

        // funcao para mudar as perguntas exibidas a partir da selecao do dropdown
        function onChange() {
            var text = dropdown_criterio.options[dropdown_criterio.selectedIndex].text;  // pegas as opcoes do dropdown
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
