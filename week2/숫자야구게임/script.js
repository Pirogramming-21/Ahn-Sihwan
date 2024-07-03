let attemptsLeft = 9;
let answer = [];
let gameOver = false;
const inputFields = document.querySelectorAll('.input-field');
const resultDisplay = document.querySelector('.result-display');
const gameResultImg = document.querySelector('#game-result-img');
const submitButton = document.querySelector('.submit-button');

function initializeGame() {
    attemptsLeft = 9;
    gameOver = false;
    answer = generateRandomNumbers();
    inputFields.forEach(input => input.value = '');
    resultDisplay.innerHTML = ''; // 초기 상태로 설정
    gameResultImg.src = '';
    submitButton.disabled = false;
}

initializeGame();

function generateRandomNumbers() {
    let numbers = [];
    while (numbers.length < 3) {
        let num = Math.floor(Math.random() * 10);
        if (!numbers.includes(num)) {
            numbers.push(num);
        }
    }
    return numbers;
}

// '확인하기' 버튼 입력 시 작동 코드
function check_numbers() {
    if (gameOver) return;

    let guess = Array.from(inputFields, input => parseInt(input.value));
    if (guess.includes(NaN)) {
        inputFields.forEach(input => input.value = '');
        alert('모든 칸을 숫자로 채워주세요.');
        return;
    }

    let result = calculateResult(guess);
    displayResult(guess, result);
    checkGameOver(result);
}

// 숫자야구 계산
function calculateResult(guess) {
    let strikes = 0;
    let balls = 0;

    guess.forEach((num, idx) => {
        if (num === answer[idx]) {
            strikes++;
        } else if (answer.includes(num)) {
            balls++;
        }
    });

    if (strikes === 0 && balls === 0) {
        return 'O';
    } else {
        return `${strikes} S ${balls} B`;
    }
}

// 결과 보여주기
function displayResult(guess, result) {
    const resultElement = document.createElement('div');
    resultElement.className = 'check-result';
    let leftPart = document.createElement('div');
    leftPart.className = 'left';
    leftPart.textContent = guess.join(' ');

    let rightPart = document.createElement('div');
    rightPart.className = 'right';
    
    if (result === 'O') {
        rightPart.innerHTML = `<div class="out num-result">O</div>`;
    } else {
        const [strikes, balls] = result.split(' ').filter(x => x !== 'S' && x !== 'B');
        rightPart.innerHTML = `${strikes} <div class="strike num-result">S</div> ${balls} <div class="ball num-result">B</div>`;
    }

    resultElement.appendChild(leftPart);
    resultElement.appendChild(rightPart);
    resultDisplay.appendChild(resultElement);
    attemptsLeft--;
}

function checkGameOver(result) {
    if (result === '3 S 0 B') {
        gameResultImg.src = 'success.png';
        gameOver = true;
    } else if (attemptsLeft === 0) {
        gameResultImg.src = 'fail.png';
        gameOver = true;
    }

    if (gameOver) {
        submitButton.disabled = true;
    }
}

