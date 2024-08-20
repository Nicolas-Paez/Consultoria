document.addEventListener('DOMContentLoaded', function () {
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    const todayButton = document.getElementById('today');
    const monthYearLabel = document.getElementById('month-year');
    const calendar = document.getElementById('calendar');

    let currentDate = new Date();

    function updateCalendar() {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        // Actualizar el encabezado del calendario con el mes y año actuales
        monthYearLabel.textContent = `${getMonthName(month)} ${year}`;

        // Generar los días del calendario
        calendar.innerHTML = generateMonthView(year, month);
    }

    function generateMonthView(year, month) {
        // Obtener el primer día del mes y el número total de días en el mes
        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        let calendarHTML = '<div class="calendar-grid">';

        // Nombres de los días de la semana
        const dayNames = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'];
        dayNames.forEach(day => {
            calendarHTML += `<div class="day-name">${day}</div>`;
        });

        // Crear los días vacíos antes del primer día del mes
        for (let i = 0; i < firstDay; i++) {
            calendarHTML += `<div class="empty-day"></div>`;
        }

        // Crear los días del mes
        for (let day = 1; day <= daysInMonth; day++) {
            calendarHTML += `<div class="day">${day}</div>`;
        }

        calendarHTML += '</div>';
        return calendarHTML;
    }

    function getMonthName(monthIndex) {
        const monthNames = [
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ];
        return monthNames[monthIndex];
    }

    // Listeners para los botones de navegación
    prevButton.addEventListener('click', function () {
        currentDate.setMonth(currentDate.getMonth() - 1);
        updateCalendar();
    });

    nextButton.addEventListener('click', function () {
        currentDate.setMonth(currentDate.getMonth() + 1);
        updateCalendar();
    });

    todayButton.addEventListener('click', function () {
        currentDate = new Date();
        updateCalendar();
    });

    // Inicializar el calendario con la fecha actual
    updateCalendar();
});
