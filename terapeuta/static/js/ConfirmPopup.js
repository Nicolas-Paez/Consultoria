// Obtener datos
const guardarBtn = document.getElementById('guardarBtn');
const popupConfirmacion = document.getElementById('popupConfirmacion');
const confirmarBtn = document.getElementById('confirmarBtn');
const cancelarBtn = document.getElementById('cancelarBtn');

// Mostrar el popup al hacer click en el boton "Guardar"
guardarBtn.addEventListener('click', () => {
    popupConfirmacion.style.display = 'flex';
});

// Confirmar
confirmarBtn.addEventListener('click', () => {
    alert('Cambios guardados con éxito.');
    popupConfirmacion.style.display = 'none';
});

// Cancelar
cancelarBtn.addEventListener('click', () => {
    popupConfirmacion.style.display = 'none';
});