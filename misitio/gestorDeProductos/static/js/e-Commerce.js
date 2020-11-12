$(function()
{
    let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
                'ÁÉÍÓÚáéíóú- ';

    $(document).ready(function () {
    $("input[type=text]").on("keyup",function () {
        option=false;
    $("input[type=text]").each(function () {
        if (!this.value) {
            option=true;
        }
        });
        $("input[type=submit]").attr("disabled",option);
        });
        });

    $('.numberTelefono').keypress(function(e) 
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) <0)
            return false;
    }); 

    $('.txtNombre').keypress(function(e) 
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) <0)
            return false;
    });
        let run = '1234567890' +
        'K' +
        'k';
    $('.txtRut').keypress(function(e) 
    {
        let caracter = String.fromCharCode(e.which);
        if(run.indexOf(caracter) <0)
            return false;
    });


    $('.btnRegistrar').click(function()
    {
        
        //creo la variable
        let valor= '';

        //obtengo los valores
        txtrutvalor=$('.txtRut').val();
        
        if(txtrutvalor == '')
        {
            alert('Es importante que llene todos los campos, por favor, introduzca Run.');
            $('.txtRut').focus();
            document.getElementById("btnAceptar").disabled = true;
            return;
            
        }

        valor=$('.txtNombre').val();

        if(valor == '')
        {
            alert('Es importante que llene todos los campos, por favor, introduzca su Nombre Completo.');
            $('.txtNombre').focus();
            return;
        }

        valor=$('.txtEmail').val();

        if(valor == '')
        {
            alert('Es importante que llene todos los campos, por favor, introduzca su Email.');
            $('.txtEmail').focus();
            return;
        }

        let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/	
		if(!emailRegex.test($('.txtEmail').val()))
		{
			alert('El formato del correo no es válido');
			$('.txtEmail').focus();
			return;
		}
		

        valor=$('.txtNacimiento').val();

        if(valor == '')
        {
            alert('Es importante que llene todos los campos, por favor, introduzca su la fecha de su nacimiento.');
            $('.txtNacimiento').focus();
            return;
        }

        valor=$('.numberTelefono').val();

        if(valor == '')
        {
            alert('Es importante que llene todos los campos, por favor, introduzca su Número Telefónico.');
            $('.numberTelefono').focus();
            return;
        }

        valor=$('.btnRegistrar').val();
        
        if(valor != alert)
        {
            document.getElementById("btnAceptar").disabled = false;
        } 
        
    });
})

