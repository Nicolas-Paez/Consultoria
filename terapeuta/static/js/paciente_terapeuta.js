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

    // Mostrar la primera página después de aplicar el filtro
    currentPage = 1; // Resetear a la primera página
    showPage(currentPage); // Mostrar la primera página
}

// Evento para cuando se escriba en la barra de búsqueda (keyup)
document.getElementById('searchBar').addEventListener('keyup', filterPatients);

// Evento para cuando se haga clic en el icono de la lupa
document.getElementById('searchIcon').addEventListener('click', filterPatients);
