// Función para filtrar las cards de pacientes
function filterCards() {
    var input = document.getElementById("searchInput");
    var filter = input.value.toLowerCase();

    var container = document.getElementById("patientsContainer");
    var cards = container.getElementsByClassName("paciente-card");

    var found = false;

    for (var i = 0; i < cards.length; i++) {
        var card = cards[i];
        var name = card.querySelector(".card-title").textContent.toLowerCase();
        var rut = card.querySelector(".card-rut").textContent.toLowerCase();
        var treatment = card.querySelector(".card-treatment").textContent.toLowerCase();

        if (name.indexOf(filter) > -1 || rut.indexOf(filter) > -1 || treatment.indexOf(filter) > -1) {
            card.style.display = "";
            found = true;
        } else {
            card.style.display = "none";
        }
    }

    var errorMessage = document.getElementById("error-message");
    if (!found) {
        errorMessage.style.display = "block";
    } else {
        errorMessage.style.display = "none";
    }
}

// Función para cerrar el mensaje de error
function closeErrorMessage() {
    var errorMessage = document.getElementById("error-message");
    errorMessage.style.display = "none";
}

// Función para detectar el Enter
function checkEnter(event) {
    if (event.key === "Enter") {
        filterCards();
    }
}
