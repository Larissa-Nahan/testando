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
        
        
        // cria as imagens e add a scr + tamanho + ids
        const seta_esquerda = document.createElement("img");
        const seta_direita = document.createElement("img");
        seta_esquerda.setAttribute("id", "seta_esquerda")
        seta_direita.setAttribute("id", "seta_direita")
        seta_esquerda.src = "/static/admin/imgs/arrow_left.png" 
        seta_direita.src = "/static/admin/imgs/arrow_right.png"
        seta_esquerda.height = 25
        seta_direita.height = 25     
        
        // coloca as imgs dentro dos btn e os insere ao lado do criterio no h2
        $("#id_criterio")[0].after(seta_esquerda);
        seta_esquerda.after(seta_direita);
        
        
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
            perguntas[j] = topicos[j].innerText.split(" - ")  // divide o que vem escrito [escala - pergunta - criterio]
            criterios[j] = perguntas[j][2];  // pega e armazena somente o critério
            input[j] = $('#id_avaliacao_chefes_'+[j])[0]
            topicos[j].innerHTML = perguntas[j][1]  // suubstitui o conteudo anterior por somente as perguntas
            topicos[j].insertBefore(input[j], topicos[j].firstChild);  // insere o input (checkbox) no inicio das perguntas
            showElement($('label[for=id_avaliacao_chefes_'+[j]+']')[0], false);
        }
        
        var dropdown_criterio = document.querySelector('#id_criterio');
        
        // funcao para mudar as perguntas exibidas a partir da selecao do dropdown
        function onChange() {
            var text = dropdown_criterio.options[dropdown_criterio.selectedIndex].text;  // pegas as opcoes do dropdown
            for(var j = 0; j < document.querySelector('#id_avaliacao_chefes').childElementCount; j++){
                if(criterios[j] == text){
                    showElement(topicos[j], true);
                } else {
                    showElement(topicos[j], false);
                }
            }
        }
        dropdown_criterio.onchange = onChange;
        onChange();
                        
        
        // funcao para mudar as perguntas exibidas a partir da selecao dos btns
        function change(x) {
            if (x.value === 'direita') {
                dropdown_criterio.selectedIndex = dropdown_criterio.selectedIndex + 1
                // pular a opcao -1 (vazio) e voltar para o inicio
                if(dropdown_criterio.selectedIndex == -1){
                    dropdown_criterio.selectedIndex = 0
                }
            } else {
                dropdown_criterio.selectedIndex = dropdown_criterio.selectedIndex - 1
                // pular a opcao -1 (vazio) e ir para o fim
                if(dropdown_criterio.selectedIndex == -1){
                    dropdown_criterio.selectedIndex = dropdown_criterio.length - 1
                }
            }
            dropdown_criterio.onchange = onChange;
            onChange()
        };
        seta_esquerda.onclick = function() {change(this)};
        seta_direita.onclick = function() {change(this)};
        
    })
})
