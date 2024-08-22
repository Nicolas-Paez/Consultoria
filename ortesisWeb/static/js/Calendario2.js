document.addEventListener("DOMContentLoaded", function() {

    //definir dias que tienen 30, 31 dias y el primer dia del mes
    const diasEnMes = 31;
    const primerDiaDelMes = 3;
    const diasEnMesAnterior = 31;
    const diasEnMesSiguiente = 30;
    const cuerpoCalendario = document.querySelector(".calendario tbody");

    //Obtiene datos de la fecha actual
    const hoy = new Date();
    const fechaHoy = hoy.getDate();
    const mesHoy = hoy.getMonth();
    const añoHoy = hoy.getFullYear();

    //Funcion para la estructura del calendario
    function generarCalendario() {
        //inicia el dia actual del mes y calcula los dias del mes anterior, tambien estan los dias del mes proximo
        let dia = 1;
        let diasMesAnterior = diasEnMesAnterior - (primerDiaDelMes - 1);
        let diaMesSiguiente = 1;

        //crea las 6 filas del calendario
        for (let i = 0; i < 6; i++) {
            const fila = document.createElement("tr");

            //crea las 7 celdas de cada día
            for (let j = 0; j < 7; j++) {
                const celda = document.createElement("td");
                //determina si la celda corresponde al fin de semana
                const esFinDeSemana = (j === 5 || j === 6);


                if (i === 0 && j < primerDiaDelMes) {
                    celda.textContent = diasMesAnterior++;
                    celda.classList.add("mes-anterior");

                    //agrega una clase "especial" a fin de semana (pinta de rojo las letras)
                    if (esFinDeSemana) {
                        celda.classList.add("mes-anterior-fin-de-semana");
                    }
                } else if (dia > diasEnMes) {
                    //verifica si llego al final del mes para mostrar los dias del mes siguiente
                    celda.textContent = diaMesSiguiente++;
                    celda.classList.add("mes-siguiente");

                    if (esFinDeSemana) {
                        celda.classList.add("mes-siguiente-fin-de-semana");
                    }
                } else {
                    // ya que no pertenece al mes siguiente ni el anterior, los dias pertenecen al mes actual
                    celda.textContent = dia;

                    if (dia === fechaHoy && mesHoy === 7 && añoHoy === 2024) {
                        //verifica que la fecha coincida con la de hoy, si lo es se añade la clase dia seleccionado
                        celda.classList.add("dia-seleccionado");
                    }
                    dia++;
                    if (esFinDeSemana) {
                        //agrega la clase "especial" para fin de semana del mes actual
                        celda.classList.add("fin-de-semana");
                    }
                }
                fila.appendChild(celda);
            }
            cuerpoCalendario.appendChild(fila);
        }
    }
    //genera el calendario
    generarCalendario();
});