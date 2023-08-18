// 뒤로 가기 버튼 클릭 시 페이지 이동
const backButton = document.getElementById("back_btn");
backButton.addEventListener("click", function() {
    window.location.href = "information-sharing.html"; // 이동할 페이지의 경로를 입력하세요
});

document.addEventListener("DOMContentLoaded", function() {
    const diaryBtn = document.querySelector(".diary_btn");
    diaryBtn.addEventListener("click", function() {
        window.location.href = "https://www.notion.so/ko-kr/personal";
    });

    const noteBtn = document.querySelector(".note_btn");
    noteBtn.addEventListener("click", function() {
        window.location.href = "https://www.goodnotes.com/kr"; // 여기에 원하는 다른 링크 주소를 넣으세요.
    });
});
