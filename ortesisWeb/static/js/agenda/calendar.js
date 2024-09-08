document.addEventListener('DOMContentLoaded', function () {
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    const todayButton = document.getElementById('today');
    const monthYearLabel = document.getElementById('month-year');
    const calendar = document.getElementById('calendar');
    const weekViewButton = document.getElementById('week-view');
    const monthViewButton = document.getElementById('month-view');

    let currentDate = new Date();
    let currentView = 'month';  // 'month' o 'week'

    // Función para actualizar la vista del calendario
    function updateCalendar() {
        if (currentView === 'month') {
            generateMonthView();
        } else {
            generateWeekView();
        }
    }

    // Vista mensual
    function generateMonthView() {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        // Actualizar el encabezado
        monthYearLabel.textContent = `${getMonthName(month)} ${year}`;

        const firstDayOfMonth = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        const adjustedFirstDay = (firstDayOfMonth === 0) ? 6 : firstDayOfMonth - 1;
        let calendarHTML = '<div class="calendar-grid">';

        const dayNames = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];
        dayNames.forEach((day, index) => {
            const className = index >= 5 ? 'day-name weekend' : 'day-name';
            calendarHTML += `<div class="${className}">${day}</div>`;
        });

        // Días vacíos antes del inicio del mes
        for (let i = 0; i < adjustedFirstDay; i++) {
            calendarHTML += `<div class="empty-day"></div>`;
        }

        // Días del mes
        for (let day = 1; day <= daysInMonth; day++) {
            const isToday = (day === new Date().getDate() && year === new Date().getFullYear() && month === new Date().getMonth());
            const className = isToday ? 'day today' : 'day';
            calendarHTML += `<div class="${className}">${day}</div>`;
        }

        const totalCells = adjustedFirstDay + daysInMonth;
        const extraDays = 42 - totalCells;

        for (let i = 0; i < extraDays; i++) {
            calendarHTML += `<div class="empty-day"></div>`;
        }

        calendarHTML += '</div>';
        calendar.innerHTML = calendarHTML;
    }

    // Vista semanal
    function generateWeekView() {
        const startOfWeek = getStartOfWeek(currentDate);
        const endOfWeek = new Date(startOfWeek);
        endOfWeek.setDate(endOfWeek.getDate() + 6);

        const weekRange = `${formatDate(startOfWeek)} - ${formatDate(endOfWeek)}`;
        monthYearLabel.textContent = weekRange;

        let calendarHTML = `
            <table class="week-view">
                <thead>
                    <tr>
                        <th>Hora</th>
                        <th>Lunes</th>
                        <th>Martes</th>
                        <th>Miércoles</th>
                        <th>Jueves</th>
                        <th>Viernes</th>
                        <th>Sábado</th>
                        <th>Domingo</th>
                    </tr>
                </thead>
                <tbody>`;

        for (let hour = 8; hour <= 20; hour++) {
            calendarHTML += `<tr><td>${hour}:00</td>`;
            for (let day = 0; day < 7; day++) {
                calendarHTML += `<td></td>`;
            }
            calendarHTML += '</tr>';
        }

        calendarHTML += '</tbody></table>';
        calendar.innerHTML = calendarHTML;
    }

    function getStartOfWeek(date) {
        const dayOfWeek = date.getDay() === 0 ? 6 : date.getDay() - 1;
        const startOfWeek = new Date(date);
        startOfWeek.setDate(date.getDate() - dayOfWeek);
        return startOfWeek;
    }

    function formatDate(date) {
        const day = date.getDate().toString().padStart(2, '0');
        const month = (date.getMonth() + 1).toString().padStart(2, '0');
        const year = date.getFullYear();
        return `${day}/${month}/${year}`;
    }

    function getMonthName(monthIndex) {
        const monthNames = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ];
        return monthNames[monthIndex];
    }

    // Event listeners para cambiar entre vistas
    prevButton.addEventListener('click', function () {
        if (currentView === 'month') {
            currentDate.setMonth(currentDate.getMonth() - 1);
        } else {
            currentDate.setDate(currentDate.getDate() - 7);
        }
        updateCalendar();
    });

    nextButton.addEventListener('click', function () {
        if (currentView === 'month') {
            currentDate.setMonth(currentDate.getMonth() + 1);
        } else {
            currentDate.setDate(currentDate.getDate() + 7);
        }
        updateCalendar();
    });

    todayButton.addEventListener('click', function () {
        currentDate = new Date();
        updateCalendar();
    });

    weekViewButton.addEventListener('click', function () {
        currentView = 'week';
        updateCalendar();
    });

    monthViewButton.addEventListener('click', function () {
        currentView = 'month';
        updateCalendar();
    });

    // Inicializar el calendario con la vista mensual
    updateCalendar();

    // Abrir el pop-up al hacer clic en un día del calendario
const dias = document.querySelectorAll(".dia");
dias.forEach(dia => {
    dia.addEventListener("click", function() {
        const fecha = this.getAttribute("data-fecha");
        document.getElementById("fechaSeleccionada").textContent = fecha;
        document.getElementById("fecha").value = fecha; // Asignar fecha al campo de fecha
        document.getElementById("popup").style.display = "block";
    });
});

// Cerrar el pop-up al hacer clic en la "X"
document.getElementById("closePopup").addEventListener("click", function() {
    document.getElementById("popup").style.display = "none";
});

// Cerrar el pop-up si se hace clic fuera del contenido
window.addEventListener("click", function(event) {
    if (event.target == document.getElementById("popup")) {
        document.getElementById("popup").style.display = "none";
    }
});
// Cerrar el pop-up al hacer clic en el botón "Cancelar"
document.getElementById("cancelarBtn").addEventListener("click", function() {
    document.getElementById("popup").style.display = "none";
});
// Agendar la cita
document.getElementById("formCita").addEventListener("submit", function(event) {
    event.preventDefault();
    const titulo = document.getElementById("titulo").value;
    const paciente = document.getElementById("paciente").value;
    const hora = document.getElementById("hora").value;
    const fecha = document.getElementById("fecha").value;

    alert(`Cita agendada para ${paciente} el ${fecha} a las ${hora}`);

    // Cerrar el pop-up después de agendar la cita
    document.getElementById("popup").style.display = "none";
});
});
