import { alumnos } from './alumnos.js';

const $prevButton = document.getElementById('data-carousel-prev_2');
const $nextButton = document.getElementById('data-carousel-forward_2');
const titulo = document.getElementById("titulo2");
const parrafo = document.getElementById("parrafo2");

let indicePersona = 0; // índice inicial de la persona

$prevButton.addEventListener('click', () => {
    indicePersona--;
    if (indicePersona < 0) {
        indicePersona = alumnos.length - 1;
    }
    titulo.textContent = alumnos[indicePersona].nombre;
    parrafo.textContent = alumnos[indicePersona].texto_informativo;
});

$nextButton.addEventListener('click', () => {
    indicePersona++;
    if (indicePersona >= alumnos.length) {
        indicePersona = 0;
    }
    titulo.textContent = alumnos[indicePersona].nombre;
    parrafo.textContent = alumnos[indicePersona].texto_informativo;
});

// Establecer el título y el párrafo inicial con la primera persona en el JSON
titulo.textContent = alumnos[indicePersona].nombre;
parrafo.textContent = alumnos[indicePersona].texto_informativo;

console.log("si")