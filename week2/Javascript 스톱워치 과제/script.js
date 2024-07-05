const timer = document.querySelector('#time');
let currentTime;
let second = 0;
let millisecond = 0;

function startTimer() {
    clearInterval(currentTime);
    currentTime = setInterval(function() {
        millisecond+= 10;
        if (millisecond >= 1000) { // 밀리초가 1000에 도달하면
            second++; // 초 증가
            millisecond = 0; // 밀리초를 다시 0으로
        }
        if (second >= 60) { // 초가 60에 도달하면
            console.log('1분 초과!')
            second = 0; // 초를 다시 0으로
        }
    
    // 결과물 화면에 보여주도록 다듬기
    let millisec_display = Math.floor(millisecond / 10).toString().padStart(2, '0');
    let second_display = second.toString().padStart(2, '0');
    timer.innerText = (`${second_display}:${millisec_display}`);
    }, 10); // 10밀리초마다 함수 실행
}
function stopTimer() {
    clearInterval(currentTime);
}
function resetTimer() {
    clearInterval(currentTime);
    second = 0;
    millisecond = 0;
    timer.innerText = "00:00";
}

const startBtn = document.querySelector('.start');
const stopBtn = document.querySelector('.stop');
const resetBtn = document.querySelector('.reset');

startBtn.addEventListener('click', startTimer);
stopBtn.addEventListener('click', stopTimer);
resetBtn.addEventListener('click', resetTimer);

