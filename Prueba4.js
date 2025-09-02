const prompt = require("prompt-sync")();

let numero = Math.floor(Math.random() * 11);  // número aleatorio entre 0 y 10
let intentos = 3;

console.log('Adivina el número secreto entre 0 y 10');
console.log(`Tienes ${intentos} intentos`);

for (let i = 0; i < intentos; i++) {
    let adivina = parseInt(prompt("Escribe el número:"));

    if (adivina === numero) {
        console.log('🎉 Adivinaste el número');
        break;
    } else {
        if (i < intentos - 1) {
            if (adivina < numero) {
                console.log('El número secreto es mayor 📈');
            } else {
                console.log('El número secreto es menor 📉');
            }
            console.log(`Te quedan ${intentos - (i + 1)} intentos`);
        } else {
            console.log(`❌ Usaste todos los intentos. El número era ${numero}`);
        }
    }
}