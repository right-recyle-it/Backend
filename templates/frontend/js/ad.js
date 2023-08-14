    // 이미지 슬라이드에 사용될 이미지들의 배열
    const images = ['../img/ad1.png', '../img/ad2.png', '../img/ad3.png'];

    // 이미지 슬라이드 인덱스
    let currentIndex = 0;

    // 이미지 슬라이드를 위한 함수
    function slideImages() {
        const adContainer = document.getElementById('ad-container');
        adContainer.innerHTML = `<img src="${images[currentIndex]}" style="width: 100%; height: auto; text-align: center;" alt="광고">`;

        // 다음 이미지로 이동
        currentIndex++;
        if (currentIndex >= images.length) {
            currentIndex = 0; // 인덱스 초기화
        }

        // 일정 시간마다 이미지 슬라이드 실행
        setTimeout(slideImages, 3000); // 3초마다 이미지 슬라이드
    }

    // 페이지 로드 시 이미지 슬라이드 시작
    slideImages();