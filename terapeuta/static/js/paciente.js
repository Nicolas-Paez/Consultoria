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
function filterCards() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const patientRows = document.querySelectorAll('.paciente-card');

    let bandera = false;

    patientRows.forEach((row) => {
        const nombre_paciente = row.querySelector('.card-title').textContent.toLowerCase();
        const rut_paciente = row.querySelector('.card-rut').textContent.toLowerCase();
        
        // Verificar si el nombre o el rut contiene el texto de búsqueda
        if (nombre_paciente.includes(searchInput) || rut_paciente.includes(searchInput)) {
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
