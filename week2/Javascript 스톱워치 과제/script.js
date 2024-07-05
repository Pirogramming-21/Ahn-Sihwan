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

const recordCheckBtn = document.querySelector('.record-check');
const removeRecordBtn = document.querySelector('.deleteBtn');
const checkAllBtn = document.querySelector('.checkAll');

function updateCheckAllBtn() {
    const recordLogAll = document.querySelectorAll('.record-log');
    const checkedLogAll = document.querySelectorAll('.record-log.checked');
    if (checkedLogAll.length === recordLogAll.length && recordLogAll.length > 0) {
        checkAllBtn.classList.add('checked');
    } else {
        checkAllBtn.classList.remove('checked');
    }
}

const startBtn = document.querySelector('.start');
const stopBtn = document.querySelector('.stop');
const resetBtn = document.querySelector('.reset');

startBtn.addEventListener('click', startTimer);

stopBtn.addEventListener('click', () => {
    stopTimer(); // 시간 스탑

    const recordLog = document.createElement('div');
    recordLog.className = 'record-log';
    
    const recordCheckBtn = document.createElement('button');
    recordCheckBtn.className = 'record-check record-btn';
    
    const recordTime = document.createElement('p');
    recordTime.className = 'record-time';

    const stoppedTime = timer.innerText;
    recordTime.innerText = stoppedTime;
    
    recordLog.append(recordCheckBtn, recordTime);
    
    const recordBottom = document.querySelector('.record-bottom');
    recordBottom.appendChild(recordLog); // 기록 추가
    recordBottom.scrollTop = recordBottom.scrollHeight;
    
    // 버튼 토글기능 추가
    recordCheckBtn.addEventListener('click', () => {
        recordCheckBtn.classList.toggle('checked');
        recordLog.classList.toggle('checked');

        updateCheckAllBtn();
    });

    updateCheckAllBtn();
});

resetBtn.addEventListener('click', resetTimer);

removeRecordBtn.addEventListener('click', () => {
    const checkedLogAll = document.querySelectorAll('.record-log.checked');
    checkedLogAll.forEach(log => log.remove());
    recordCheckBtn.classList.remove('checked');
    updateCheckAllBtn();
});

checkAllBtn.addEventListener('click', () => {
    checkAllBtn.classList.toggle('checked');
    const isChecked = checkAllBtn.classList.contains('checked');
    const recordLogAll = document.querySelectorAll('.record-log');

    recordLogAll.forEach(log => {
        const recordCheck = log.querySelector('.record-check');
        if (isChecked) {
            log.classList.add('checked');
            recordCheck.classList.add('checked');
        } else {
            log.classList.remove('checked');
            recordCheck.classList.remove('checked');
        }
    })
    updateCheckAllBtn();
});

