const timer = document.querySelector('#time');
let currentTime;

function startTimer() {
    let second = 0;
    let millisecond = 0;
    let currentTime = setInterval(function() {
        millisecond+= 10;
        if (millisecond >= 1000) { // 밀리초가 1000에 도달하면
            second++; // 초 증가
            millisecond = 0; // 밀리초를 다시 0으로
        }
        if (second >= 60) { // 초가 60에 도달하면
            console.log('1분 초과!')
            second = 0; // 초를 다시 0으로
        }
    let millisec_display = Math.floor(millisecond / 10); // 디스플레이용 - 2자리수 밀리초
    let second_display = second.toString().padStart(2, '0'); // 디스플레이용 - 2자리수 초
    timer.innerText = (`${second_display}:${millisec_display}`);
    }, 10); // 매 10밀리초마다 함수 실행
}


const start = document.querySelector('.start');
const stop = document.querySelector('.stop');
const reset = document.querySelector('.reset');

start.addEventListener('click', startTimer);
