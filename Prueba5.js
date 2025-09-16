const prompt = require("prompt-sync")();

// Definición de los diccionarios (objetos)
let categorias = {
  "frutas": ['banana', 'fresa', 'mora', 'manzana', 'pera', 'uva', 'piña', 'limón', 'naranja', 'sandia'],
  "verduras": ['zanahoria', 'lechuga', 'tomate', 'pepino', 'espinaca'],
  "lacteos": ['leche', 'queso', 'yogur', ],
  "congelados": ['pollo', 'carne', 'pescado', 'jamon'],
  "dulce": ['chocolate', 'galletas', 'helado'],
  "granos": ['arroz', 'frijoles', 'lentejas']
};

// Se crea un objeto 'lista_compras' con las mismas categorías,
// pero con arrays vacíos.
let lista_compras = {};
for (let categoria in categorias) {
  lista_compras[categoria] = [];
}

// Bucle principal para solicitar la entrada del usuario
function agregarAlimento() {
  let pregunta = prompt('¿Deseas agregar un alimento a tu lista de compras? (si/no)').toLowerCase();

  if (pregunta === 'si') {
    let alimento = prompt('Indica el nombre del alimento: ').toLowerCase();
    
    let encontrado = false;
    for (let categoria in categorias) {
      if (categorias[categoria].includes(alimento)) {
        lista_compras[categoria].push(alimento);
        console.log(`${alimento} agregado a ${categoria}. ¡Genial!`);
        encontrado = true;
        break; // Sale del bucle una vez que el alimento se encuentra
      }
    }

    if (!encontrado) {
      console.log(`El alimento "${alimento}" no está en las categorías registradas.`);
      console.log('Categorías disponibles:');
      for (let categoria in categorias) {
        console.log(`- ${categoria.charAt(0).toUpperCase() + categoria.slice(1)}`);
      }

      let nueva_categoria = prompt('Ingresa la categoría a la que pertenece (o escribe "salir" para no agregarlo): ').toLowerCase();

      if (nueva_categoria !== 'salir') {
        if (categorias.hasOwnProperty(nueva_categoria)) {
          categorias[nueva_categoria].push(alimento);
          lista_compras[nueva_categoria].push(alimento);
          console.log(`${alimento} agregado a ${nueva_categoria} y a la lista de compras. ¡Listo!`);
        } else {
          console.log('Categoría no válida. El alimento no se agregó.');
        }
      }
    }
    agregarAlimento(); // Llama a la función de nuevo para continuar el bucle
  } else if (pregunta === 'no') {
    console.log('\n--- Fin de la lista de compras ---');
    for (let categoria in lista_compras) {
      if (lista_compras[categoria].length > 0) {
        console.log(`- ${categoria.charAt(0).toUpperCase() + categoria.slice(1)}: ${lista_compras[categoria].join(', ')}`);
      }
    }
  } else {
    console.log('Por favor, responde "si" o "no".');
    agregarAlimento(); // Llama a la función de nuevo para una respuesta válida
  }
}

// Inicia la ejecución del programa
agregarAlimento();