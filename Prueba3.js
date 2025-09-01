const prompt = require("prompt-sync")();

let backend = 'Back-End';
let frontend = 'Front-End';

let area = prompt(`¿Qué area te gustaría seguir? (${backend} o ${frontend}): `);

let area_backend1= 'C#';
let area_backend2= 'JAVA';
let area_fronted1= 'REACT';
let area_fronted2= 'VUE';

while (true) {
    if (area = backend) {
    prompt(`¿Te gustaría aprender ${area_backend1} O ${area_backend2}?: `);
    break;
} else if (area = frontend){
    prompt(`Te gustaría aprender ${area_fronted1} o ${area_fronted2}?: `);
    break;
} else{
    prompt('Respuesta invalida, vuelve a intentarlo.');
}

}

let especializacion = 'Especializacion'
let fullstack = 'Fullstack'
let elección = prompt(`¿Quieres seguir una ${especializacion}  o convertirte en ${fullstack}: `);

console.log (`Quieres seguir en ${elección}`)

// Lista para guardar las tecnologías que diga el usuario
let tecnologias = [];

// Preguntar la primera tecnología
let tecnologia = prompt("¿En qué tecnología te gustaría especializarte o aprender? ");
tecnologias.push(tecnologia);
console.log(`¡Excelente elección! ${tecnologia} es muy interesante.`);

// Mientras el usuario responda "ok", seguir preguntando
while (true) {
    let continuar = prompt("¿Hay alguna otra tecnología que te gustaría aprender? (ok para continuar / no para terminar): ").toLowerCase();

    if (continuar === "ok") {
        let nuevaTec = prompt("Escribe el nombre de la tecnología: ");
        tecnologias.push(nuevaTec);
        console.log(`¡Genial! ${nuevaTec} es una gran opción para tu crecimiento.`);
    } else {
        console.log("Gracias por compartir tus intereses en tecnología.");
        break;
    }
}

// Mostrar todas las tecnologías elegidas
console.log("\nResumen de tecnologías que quieres aprender:");
tecnologias.forEach((t, i) => console.log(`${i + 1}. ${t}`));
