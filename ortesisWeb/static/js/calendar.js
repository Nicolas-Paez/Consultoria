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

        // Establecer el día actual al primero del mes para evitar problemas de salto de mes
        currentDate.setDate(1);

        // Actualizar el encabezado del calendario con el mes y año actuales
        monthYearLabel.textContent = `${getMonthName(month)} ${year}`;

        // Generar los días del calendario
        calendar.innerHTML = generateMonthView(year, month);
    }

    function generateMonthView(year, month) {
        const firstDayOfMonth = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        //Lunes como primer dia de la semana
        const startDay = (firstDayOfMonth + 6) % 7;

        let calendarHTML = '<div class="calendar-grid">';
        const dayNames = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];

        dayNames.forEach((day, index) => {
            const className = index >= 5 ? 'day-name weekend' : 'day-name';
            calendarHTML += `<div class="${className}">${day}</div>`;
        });

        // Día desde el mes anterior que completa el primer lunes
        const prevMonthDays = new Date(year, month, 0).getDate();
        for (let i = startDay; i > 0; i--) {
            calendarHTML += `<div class="empty-day"><span>${prevMonthDays - i + 1}</span></div>`;
        }

        // Días del mes actual
        for (let day = 1; day <= daysInMonth; day++) {
            const isToday = (day === new Date().getDate() && year === new Date().getFullYear() && month === new Date().getMonth());
            const className = isToday ? 'day today' : 'day';
            calendarHTML += `<div class="${className}"><span>${day}</span></div>`;
        }

        // Días del mes siguiente para vista de 6 semanas en todos los meses
        let nextMonthDay = 1;
        const totalCells = startDay + daysInMonth;
        for (let i = totalCells; i < 42; i++) {
            calendarHTML += `<div class="empty-day"><span>${nextMonthDay++}</span></div>`;
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

    updateCalendar();
});
