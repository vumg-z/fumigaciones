
fetch('./articulos/articulos.json')
  .then(response => response.json())
  .then(data => {
    // Trabajar con los datos del archivo JSON aquí
    asignarURLaEnlaces(data);
  })
  .catch(error => console.error(error));

function asignarURLaEnlaces(data) {
  // Obtener todos los divs con id 'article'
  const divs = document.querySelectorAll('#article');

  // Iterar sobre cada div
  divs.forEach((div, index) => {
    if (data[index]) {
      // Reemplazar espacios con guiones bajos y agregar la extensión .html
      const h5Texto = data[index].h5s[0];
      const url = h5Texto.replace(/\s+/g, '_') + '.html';

      // Obtener todos los elementos de enlace 'a' dentro del div
      const enlaces = div.querySelectorAll('a');

      // Asignar la URL a cada enlace
      enlaces.forEach((enlace) => {
        enlace.setAttribute('href', "./articulos/1/"+url);
      });
    }
  });
}
