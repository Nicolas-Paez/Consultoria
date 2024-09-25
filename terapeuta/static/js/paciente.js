function filterCards() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const patientRows = document.querySelectorAll('.paciente-card');

    let bandera = false;

    patientRows.forEach((row) => {
        const nombre_paciente = row.querySelector('.card-title').textContent.toLowerCase();
        const rut_paciente = row.querySelector('.card-rut').textContent.toLowerCase();
        const tratamiento_paciente = row.querySelector('.card-trat').textContent.toLowerCase();
        
        // Verificar si el nombre o el rut contiene el texto de búsqueda
        if (nombre_paciente.includes(searchInput) || rut_paciente.includes(searchInput) || tratamiento_paciente.includes(searchInput)){
            row.style.display = 'flex';
            bandera = true;
        } else {
            row.style.display = 'none'; 
        }
    });


    const errorMessage = document.getElementById('error-message');
    if (!bandera && searchInput !== '') {
        errorMessage.classList.remove('hidden');
    } else {
        errorMessage.classList.add('hidden');
    }
}

function closeErrorMessage() {
    const errorMessage = document.getElementById('error-message');
    errorMessage.classList.add('hidden');
}

// Función para detectar la tecla Enter y ejecutar la búsqueda
function checkEnter(event) {
    if (event.key === 'Enter') {
        filterCards();
    }
}
