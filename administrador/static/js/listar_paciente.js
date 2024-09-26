document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.paciente-checkbox');
    const selectAllCheckbox = document.getElementById('select-all');
    const inactivarBtn = document.getElementById('inactivar-btn');
    const restaurarBtn = document.getElementById('restaurar-btn');

    // Seleccionar o deseleccionar todos los checkboxes
    selectAllCheckbox.addEventListener('change', function() {
        checkboxes.forEach(checkbox => {
            checkbox.checked = selectAllCheckbox.checked;
        });
        updateButtonsState();
    });

    // Manejar el cambio de estado de los checkboxes
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', updateButtonsState);
    });

    // Activar o desactivar botones
    function updateButtonsState() {
        const selectedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked);
    
        if (selectedCheckboxes.length === 0) {
            inactivarBtn.disabled = true;
            restaurarBtn.disabled = true;
            return;
        }
    
        const anyActive = selectedCheckboxes.some(checkbox => {
            const badge = checkbox.closest('tr').querySelector('td:nth-child(4) .badge');
            return badge.textContent.trim() === 'Activo';
        });
    
        const anyInactive = selectedCheckboxes.some(checkbox => {
            const badge = checkbox.closest('tr').querySelector('td:nth-child(4) .badge');
            return badge.textContent.trim() === 'Inactivo';
        });
    
        inactivarBtn.disabled = !anyActive; 
        restaurarBtn.disabled = !anyInactive; 
    }

    // Acción de pasar a inactivo
    inactivarBtn.addEventListener('click', function() {
        const selectedIds = Array.from(checkboxes).filter(cb => cb.checked).map(cb => cb.value);
        fetch("{% url 'cambiar_estado_inactivo' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({ pacientes_ids: selectedIds })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                location.reload();
            } else {
                alert('Error al inactivar los pacientes.');
            }
        });
    });

    // Acción de restaurar pacientes inactivos
    restaurarBtn.addEventListener('click', function() {
        const selectedIds = Array.from(checkboxes).filter(cb => cb.checked).map(cb => cb.value);
        fetch("{% url 'restaurar_paciente' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}',
            },
            body: JSON.stringify({ pacientes_ids: selectedIds })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                location.reload();
            } else {
                alert('Error al restaurar los pacientes.');
            }
        });
    });
});
