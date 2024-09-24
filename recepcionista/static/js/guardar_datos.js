function guardarDatosYContinuar() {
    const formulario = document.getElementById('formularioPaciente');
    const formData = new FormData(formulario);

    // Guardar los datos en sessionStorage
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });
    sessionStorage.setItem('formData', JSON.stringify(data));

    // Redirigir a la nueva ventana o sección
    window.location.href = 'asignar_terapeuta';
}