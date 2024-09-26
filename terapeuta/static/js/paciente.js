function filterCards() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const patientRows = document.querySelectorAll('.paciente-card');
    let bandera = false;

    patientRows.forEach((row) => {
        const nombre_paciente = row.querySelector('.card-title').textContent.toLowerCase();
        const rut_paciente = row.querySelector('.card-rut').textContent.toLowerCase();
        const tratamiento_paciente = row.querySelector('.card-trat').textContent.toLowerCase();

        // Verificar si el nombre, rut o tratamiento contiene el texto de búsqueda
        if (nombre_paciente.includes(searchInput) || rut_paciente.includes(searchInput) || tratamiento_paciente.includes(searchInput)) {
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

// Función para obtener el CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let pacienteIdGlobal = null;  //almacenar el ID del paciente temporalmente
// Función que se ejecuta al hacer clic en "Marcar como Inactivo"
function mostrarPopUp(pacienteId, nombre, rut, tratamiento) {
    pacienteIdGlobal = pacienteId;

    const detallesDiv = document.getElementById('popup-paciente-detalles');
    detallesDiv.innerHTML = `
        <p><strong>Nombre:</strong> ${nombre}</p>
        <p><strong>RUT:</strong> ${rut}</p>
        <p><strong>Tratamiento:</strong> ${tratamiento}</p>
    `;
    document.getElementById('popupModal').style.display = 'block';
}

// Función para cerrar el pop-up
function cerrarPopUp() {
    document.getElementById('popupModal').style.display = 'none';
}

// Función para confirmar la desactivación del paciente
function confirmarDesactivacion() {
    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    fetch(`/paciente/cambiar-estado/${pacienteIdGlobal}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Agregar CSRF Token para proteger la solicitud
        }
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                return response.text().then(text => { throw new Error(text) });
            }
        })

        .then(data => {
            if (data.status === "success") {
                alert("PACIENTE DESVINCULADO CORRECTAMENTE");
                cerrarPopUp();
                location.reload();  // Recargar la página
            } else {
                alert("Error: " + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("Hubo un problema al intentar desactivar al paciente.");
        });
}