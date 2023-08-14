// 이벤트 핸들러 함수 정의
function goToIndex1() {
    // device-instructions.html로 이동
    window.location.href = 'device-instructions.html';
}

function goToIndex2() {
    // free-template-download.html로 이동
    window.location.href = 'free-template-download.html';
}

function goToIndex3() {
    // mainpage.html로 이동
    window.location.href = 'mainpage.html';
}

// 버튼 클릭 이벤트에 핸들러 연결
document.addEventListener('DOMContentLoaded', function() {
    var deviceBtn = document.getElementById('device_btn');
    var templateBtn = document.getElementById('template_btn');
    var mainBtn = document.getElementById('back_btn');

    deviceBtn.addEventListener('click', goToIndex1);
    templateBtn.addEventListener('click', goToIndex2);
    mainBtn.addEventListener('click', goToIndex3)
});
