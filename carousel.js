import { personas } from './text.js';

const $prevButton = document.getElementById('data-carousel-prev');
const $nextButton = document.getElementById('data-carousel-next');
const titulo = document.getElementById("titulo");
const parrafo = document.getElementById("parrafo");

let indicePersona = 0; // índice inicial de la persona

$prevButton.addEventListener('click', () => {
    indicePersona--;
    if (indicePersona < 0) {
        indicePersona = personas.length - 1;
    }
    titulo.textContent = personas[indicePersona].nombre;
    parrafo.textContent = personas[indicePersona].texto_informativo;
});

$nextButton.addEventListener('click', () => {
    indicePersona++;
    if (indicePersona >= personas.length) {
        indicePersona = 0;
    }
    titulo.textContent = personas[indicePersona].nombre;
    parrafo.textContent = personas[indicePersona].texto_informativo;
});

// Establecer el título y el párrafo inicial con la primera persona en el JSON
titulo.textContent = personas[indicePersona].nombre;
parrafo.textContent = personas[indicePersona].texto_informativo;