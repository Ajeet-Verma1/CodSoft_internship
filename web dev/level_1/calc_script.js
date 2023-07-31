let display = document.getElementById('display');
let expression = '';

function appendToDisplay(value) {
    expression += value;
    display.innerText = expression;
}

function clearDisplay() {
    expression = '';
    display.innerText = '0';
}

function calculateResult() {
    try {
        const result = eval(expression);
        expression = result.toString();
        display.innerText = result;
    } catch (error) {
        display.innerText = 'Error';
    }
}