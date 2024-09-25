document.addEventListener('DOMContentLoaded', function () {
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    const todayButton = document.getElementById('today');
    const monthYearLabel = document.getElementById('month-year');
    const calendar = document.getElementById('calendar');
    const weekViewButton = document.getElementById('week-view');
    const monthViewButton = document.getElementById('month-view');
    const popup = document.getElementById('popup');
    const closePopupButton = document.getElementById('closePopup');
    
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
            calendarHTML += `<div class="${className}" data-fecha="${day}/${month + 1}/${year}">${day}</div>`;
        }

        const totalCells = adjustedFirstDay + daysInMonth;
        const extraDays = 42 - totalCells;

        for (let i = 0; i < extraDays; i++) {
            calendarHTML += `<div class="empty-day"></div>`;
        }

        calendarHTML += '</div>';
        calendar.innerHTML = calendarHTML;

        // Añadir el evento de clic a cada día
        document.querySelectorAll(".day").forEach(day => {

            day.addEventListenner('click', function(){
                const selectedDate = this.getAttribute("data-fecha");
                showSessions(selectedDate);
            });
            
            // añade evento al hacer doble clic
            day.addEventListener("dblclick", function () {
                const selectedDate = this.getAttribute("data-fecha");
                document.getElementById("fechaSeleccionada").textContent = selectedDate;
                document.getElementById("fecha").value = selectedDate; // Asigna la fecha al campo de fecha del formulario
                popup.style.display = "block"; // Muestra el popup
            });
        });
    }
    // Funcion para mostrar sesiones
    function showSessions(selectedDate){
        const sessionPopup = document.getElementById("session-popup");
        const sessionDetails = document.getElementById("session-details");

        // en caso de haber citas muestra detalles y hora
        const sessionsForDate = appointments[selectedDate] || [];
        sessionDetails.innerHTML = '';
        if (sessionsForDate.lenght > 0) {
            sessionsForDate.forEach(session => {
                const sessionElement = document.createElement('div');
                sessionElement.textContent = `Hora: ${session.time}, Detalles: ${session.details}`;
                sessionDetails.appendChild(sessionElement);
            });
        }
        // en caso de que no haya muestra ese mensaje 
        else{
            sessionDetails.textContent = 'No hay sesiones para este día';
        }
        // Mostrar el popup
        sessionPopup.style.display = 'block';

        const rect = this.getBoundingClientRect();
        sessionPopup.style.top =`${rect.bottom + window.scrollY}px`;
        sessionPopup.style.left = `${rect.left}px`;
    }

    // Cerrar popup al hacer clic en el botón
    document.getElementById("closeSessionPopup").addEventListener("click", function(){
        document.getElementById("session-popup").style.display = 'none';
    });

    // Cerrar popup si se clickea fuera
    window.addEventListener("click", function(event){
        const sessionPopup = document.getElementById("session-popup");
        if (event.target === sessionPopup) {
            sessionPopup.style.display = 'none';
        }
    });

    // Vista semanal con scrollbar y eventos para abrir el popup
    function generateWeekView() {
        const startOfWeek = getStartOfWeek(currentDate);
        const endOfWeek = new Date(startOfWeek);
        endOfWeek.setDate(endOfWeek.getDate() + 6);

        const weekRange = `${formatDate(startOfWeek)} - ${formatDate(endOfWeek)}`;
        monthYearLabel.textContent = weekRange;

        let calendarHTML = `
            <div class="week-view-container">
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

        // Genera las horas de 8:00 AM a 8:00 PM
        for (let hour = 8; hour <= 20; hour++) {
            calendarHTML += `<tr><td class="time-slot">${hour}:00</td>`;
            for (let day = 0; day < 7; day++) {
                calendarHTML += `<td class="week-hour" data-hour="${hour}:00" data-day="${day}"></td>`;
            }
            calendarHTML += '</tr>';
        }

        calendarHTML += '</tbody></table></div>';
        calendar.innerHTML = calendarHTML;

        // Añadir evento para que al hacer clic en una celda de hora se abra el popup
        document.querySelectorAll(".week-hour").forEach(hourCell => {
            hourCell.addEventListener("click", function () {
                const selectedHour = this.getAttribute("data-hour");
                const selectedDay = this.getAttribute("data-day");

                // Asigna la fecha y la hora seleccionadas al popup
                document.getElementById("fechaSeleccionada").textContent = `${selectedHour}, Día ${parseInt(selectedDay) + 1}`;
                document.getElementById("hora").value = selectedHour; // Asigna la hora al campo del formulario
                popup.style.display = "block"; // Muestra el popup
            });
        });
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

    // Cerrar el pop-up al hacer clic en el botón de cerrar
    closePopupButton.addEventListener("click", function () {
        popup.style.display = "none";
    });

    // Cerrar el pop-up si se hace clic fuera del contenido
    window.addEventListener("click", function (event) {
        if (event.target === popup) {
            popup.style.display = "none";
        }
    });

    // Inicializar el calendario con la vista mensual
    updateCalendar();
});
