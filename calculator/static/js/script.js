// Función para sumar dos números
function sumar(a, b) {
    return a + b;
}

// Función para restar dos números
function restar(a, b) {
    return a - b;
}

// Función para multiplicar dos números
function multiplicar(a, b) {
    return a * b;
}

// Función para dividir dos números
function dividir(a, b) {
    if (b === 0) {
        return "Error: No se puede dividir entre cero";
    }
    return a / b;
}

// Función para calcular el cuadrado de un número
function cuadrado(a) {
    return a * a;
}

// Función para calcular la raíz cuadrada de un número
function raizCuadrada(a) {
    if (a < 0) {
        return "Error: No se puede calcular la raíz cuadrada de un número negativo";
    }
    return Math.sqrt(a);
}

// Función para calcular el factorial de un número
function factorial(a) {
    if (a < 0) {
        return "Error: No se puede calcular el factorial de un número negativo";
    }
    let result = 1;
    for (let i = 1; i <= a; i++) {
        result *= i;
    }
    return result;
}

// Función para guardar el operador seleccionado
function guardarOperador(operador) {
    let operadoresPermitidos = ['+', '-', '*', '/'];
    if (operadoresPermitidos.includes(operador)) {
        // Guardar el operador seleccionado en una variable global o en algún otro lugar
        // Implementar el código necesario para guardar el operador
        console.log("Operador guardado: " + operador);
    } else {
        console.log("Error: Operador no válido");
    }
}

// Función para calcular el resultado de la operación
function calcularResultado(operador) {
    let resultado;
    switch (operador) {
        case '+':
            resultado = sumar(a, b);
            break;
        case '-':
            resultado = restar(a, b);
            break;
        case '*':
            resultado = multiplicar(a, b);
            break;
        case '/':
            resultado = dividir(a, b);
            break;
        default:
            resultado = "Error: Operador no válido";
            break;
    }
    return resultado;
}

// Función para calcular el cuadrado de un número
function calcularCuadrado(a) {
    return a * a;
}

// Función para calcular el cubo de un número
function calcularCubo(a) {
    return a * a * a;
}

// Función para calcular el sumatorio de un conjunto de números
function sumatorio(numeros) {
    let sum = 0;
    for (let i = 0; i < numeros.length; i++) {
        sum += numeros[i];
    }
    return sum;
}

// Función para ordenar un conjunto de números
function ordenar(numeros) {
    return numeros.sort((a, b) => a - b);
}

// Función para revertir un conjunto de números
function revertir(numeros) {
    return numeros.reverse();
}
// Función para quitar el último número de un conjunto
function quitar(numeros) {
    numeros.pop();
    return numeros;
}