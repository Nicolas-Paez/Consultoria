const input = document.querySelector('input');
const addBtn = document.querySelector('.btn-add');
const ul = document.querySelector('ul');
const empty = document.querySelector('.empty');

addBtn.addEventListener("click", (e) => {
    e.preventDefault();     
    
    const text = input.value;

    const li = document.createElement('li');
    const p = document.createElement('p');
    p.textContent = text;

    li.appendChild(p);
    ul.appendChild(li);
})

document.addEventListener('DOMContentLoaded', function () {
    const patientsPerPage = 5; // Número de pacientes por página
    const patients = document.querySelectorAll('.paciente'); // Seleccionar todos los pacientes
    const totalPages = Math.ceil(patients.length / patientsPerPage); // Calcular total de páginas
    let currentPage = 1; // Página inicial

    // Función para mostrar los pacientes de la página actual
    function showPage(page) {
        const start = (page - 1) * patientsPerPage;
        const end = start + patientsPerPage;

        patients.forEach((patient, index) => {
            // Mostrar u ocultar pacientes según la página
            if (index >= start && index < end) {
                patient.style.display = 'block'; // Mostrar
            } else {
                patient.style.display = 'none'; // Ocultar
            }
        });

        // Actualizar el número de página
        document.getElementById('pageNumber').textContent = page;
    }

    // Evento para el botón "Siguiente"
    document.getElementById('nextPage').addEventListener('click', function () {
        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
        }
    });

    // Evento para el botón "Anterior"
    document.getElementById('prevPage').addEventListener('click', function () {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    // Mostrar la primera página al cargar
    showPage(currentPage);
});

// Función de búsqueda que será reutilizada
function filterPatients() {
    let searchQuery = document.getElementById('searchBar').value.toLowerCase(); // Obtener valor de búsqueda
    let patients = document.querySelectorAll('.paciente'); // Seleccionar todos los pacientes

    // Recorrer cada paciente para verificar si coincide con el valor de búsqueda
    patients.forEach(function(patient) {
        let name = patient.querySelector('p:nth-child(1)').textContent.toLowerCase();
        let rut = patient.querySelector('p:nth-child(2)').textContent.toLowerCase();
        let treatment = patient.querySelector('p:nth-child(4)').textContent.toLowerCase();

        if (name.includes(searchQuery) || rut.includes(searchQuery) || treatment.includes(searchQuery)) {
            patient.style.display = ''; // Mostrar paciente si coincide
        } else {
            patient.style.display = 'none'; // Ocultar paciente si no coincide
        }
    });
}

// Evento para cuando se escriba en la barra de búsqueda (keyup)
document.getElementById('searchBar').addEventListener('keyup', filterPatients);

// Evento para cuando se haga clic en el icono de la lupa
document.getElementById('searchIcon').addEventListener('click', filterPatients);

