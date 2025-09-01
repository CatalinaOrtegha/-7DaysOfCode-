// Importamos prompt-sync
const prompt = require("prompt-sync")();

// Pedimos los datos al usuario
let nombre = prompt("¿Cuál es tu nombre? ");
let edad = parseInt(prompt("¿Cuál es tu edad? "));
let lenguaje = prompt("¿Qué lenguaje de programación estás estudiando? ");

// Mostramos el resultado
console.log(`Hola ${nombre}, tienes ${edad} años y estás estudiando ${lenguaje}.`);

console.log(`¿Te gusta estudiar ${lenguaje}`);

while (true) {
    let opcion= prompt('Responde con el número 1 para SÍ o 2 para NO: ');

    if (opcion === '1') {
        console.log('¡Muy bien! Sigue estudiando y tendrás mucho éxito');
        break;
    }
    else if (opcion === '2') {
        console.log('Oh, qué pena... ¿Ya intentaste aprender otros lenguajes?');
        break;
        
    }else {
        console.log('Respuesta invalida');
    }
}