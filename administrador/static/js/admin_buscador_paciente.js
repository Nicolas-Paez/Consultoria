function filtrarPacientes(event) {
    event.preventDefault(); 

    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const filasPacientes = document.querySelectorAll('tbody tr:not(#no-coincidencias):not(.table-empty)'); // Excluir la fila de no coincidencias y la fila vacía

    let bandera = false; // Bandera para saber si hay coincidencias

    filasPacientes.forEach((fila) => {
        const nombre_paciente = fila.cells[0].textContent.toLowerCase();
        const rut_paciente = fila.cells[1].textContent.toLowerCase();
        
        // Verificar si el nombre o el rut contiene el texto de búsqueda
        if (nombre_paciente.includes(searchInput) || rut_paciente.includes(searchInput)) {
            fila.style.display = ''; // Mostrar la fila que coincida
            bandera = true; // Si encontramos un resultado, actualizamos la bandera
        } else {
            fila.style.display = 'none'; // Ocultar la fila que no coincida
        }
    });

    // Mostrar el mensaje de error si no hay coincidencias y la búsqueda no está vacía
    const mensajeError = document.getElementById('no-coincidencias');
    if (!bandera && searchInput !== '') {
        mensajeError.style.display = 'table-row';
    } else {
        mensajeError.style.display = 'none';
    }
}

function verificarEnter(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); 
        filtrarPacientes(event);
    }
}

document.querySelector('.busqueda-input input').addEventListener('keypress', verificarEnter);
