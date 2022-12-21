django.jQuery = jQuery;

django.jQuery(document).ready(function () {
    if (document.querySelector('#id_meritos_colaboradores')) {
        var meritos = document.querySelectorAll('[name="meritos_colaboradores"]');
        var demeritos = document.querySelectorAll('[name="demeritos_colaboradores"]');
    } else {
        var meritos = document.querySelectorAll('[name="meritos_chefes"]');
        var demeritos = document.querySelectorAll('[name="demeritos_chefes"]');
    }
    
    var calculo = document.querySelector('#id_calculo');
    // var calculo = document.querySelector('.field-calculo').querySelector('.readonly');
    
    var meritos_total = meritos.length;
    var demeritos_total = demeritos.length;
    var meritos_empregado = 0;
    var demeritos_empregado = 0;
    var fd = 0;
    
    if (calculo && calculo.value != 0){
        for (var i = 0; i < meritos.length; i++) {
                console.log(i)
                if(meritos[i].checked){
                    meritos_empregado++;
                }
            }
            for (var i = 0; i < demeritos.length; i++) {
                if(demeritos[i].checked){
                    demeritos_empregado++;
                }
            }
            fd = calculo.value;
        }
        
        for (var i = 0; i < meritos.length; i++) {
            $(meritos[i]).change(function () {
                if (this.checked) {
                    meritos_empregado++;
                } else {
                    if (meritos_empregado > 0) {
                        meritos_empregado--;
                    }
                }
                fd = ((100 / meritos_total) * meritos_empregado) - ((100 / demeritos_total) * demeritos_empregado);
                fd = Math.round(fd * 100) / 100
                fd = fd.toFixed(2)

                // calculo.innerHTML = calculo.innerHTML.replace(calculo.innerHTML, fd)
                calculo.value = calculo.value.replace(calculo.value, fd)
            });
        }
        for (var i = 0; i < demeritos.length; i++) {
            $(demeritos[i]).change(function () {
                if (this.checked) {
                    demeritos_empregado++;
                } else {
                    if (demeritos_empregado > 0) {
                        demeritos_empregado--;
                    }
                }
                fd = ((100 / meritos_total) * meritos_empregado) - ((100 / demeritos_total) * demeritos_empregado);
                fd = Math.round(fd * 100) / 100
                fd = fd.toFixed(2)

                // calculo.innerHTML = calculo.innerHTML.replace(calculo.innerHTML, fd)
                calculo.value = calculo.value.replace(calculo.value, fd)
            });
        }
})