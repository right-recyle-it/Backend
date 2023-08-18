const applyButton = document.getElementById("apply_btn");
const applyImage = document.getElementById("apply_image");
let selectedRadioValue = null;

// 라디오 버튼 클릭 시 버튼 이미지 및 활성화 상태 변경 함수
function updateButtonState() {
    const radioButtons = document.querySelectorAll('input[name="contact"]');
    let checkedRadioButton = false;

    radioButtons.forEach(radioButton => {
        if (radioButton.checked) {
            checkedRadioButton = true;
            selectedRadioValue = radioButton.value; // 선택한 라디오 버튼의 값을 저장
        }
    });

    if (checkedRadioButton) {
        applyButton.disabled = false;
        applyImage.src = "../img/apply_btn.svg";
    } else {
        applyButton.disabled = true;
        applyImage.src = "../img/not_apply_btn.svg";
    }
}

// 라디오 버튼 클릭 이벤트 리스너 등록
const radioInputs = document.querySelectorAll('input[name="contact"]');
radioInputs.forEach(radioInput => {
    radioInput.addEventListener("click", updateButtonState);
});
// 초기 버튼 상태 설정
updateButtonState();

// 뒤로 가기 버튼 클릭 시 페이지 이동
const backButton = document.getElementById("back_btn");
backButton.addEventListener("click", function() {
    window.location.href = "information-sharing.html"; // 이동할 페이지의 경로를 입력하세요
});

// "적용" 버튼 클릭 시 선택한 라디오 버튼 값에 따라 링크로 이동
applyButton.addEventListener("click", function() {
    if (selectedRadioValue === "galaxy-tab") {
        window.location.href = "https://www.samsung.com/sec/event/galaxy-tabs9/launching/?cid=sec_paid_ppc_google_tab_ecommerce_searchad_text_tab-s9-launching_%EA%B0%A4%EB%9F%AD%EC%8B%9C%ED%83%AD_pfm&utm_source=google&utm_medium=searchad&utm_campaign=tab&utm_term=%EA%B0%A4%EB%9F%AD%EC%8B%9C%ED%83%AD&_AT=000202C801AD0371807E&gad=1&gclid=CjwKCAjw_uGmBhBREiwAeOfsd2cEHJstL2ZSV5eWgt6dzYRA05QEjV2M0meCjwRus-H3ogKKjEV8RRoCrPIQAvD_BwE";
    } else if (selectedRadioValue === "ipad-mini") {
        window.location.href = "https://www.apple.com/kr/ipad-mini/?afid=p238%7CsDmAtxN6H-dc_mtid_18707vxu38484_pcrid_639523218141_pgrid_124586082669_pntwk_g_pchan__pexid__&cid=aos-kr-kwgo-ipad--slid---product-";
    } else if (selectedRadioValue === "ipad-air") {
        window.location.href = "https://www.apple.com/kr/ipad-air/?afid=p238%7Csu9zfJENp-dc_mtid_18707vxu38484_pcrid_629271936235_pgrid_124586082429_pntwk_g_pchan__pexid__&cid=aos-kr-kwgo-ipad--slid---product-"; 
    } else if (selectedRadioValue === "lg-notebook") {
        window.location.href = "https://www.lge.co.kr/notebook/16z90q-ea5wk?utm_campaign=20220718_notebook_sa_bc&utm_medium=cpc&utm_source=google-sa&utm_content=03_notebook_pc&utm_term=%EA%B7%B8%EB%9E%A8&gclid=CjwKCAjw_uGmBhBREiwAeOfsd_5xCsVuXlxH4zGHizFQ2zsIzPhd-Ab0fibUbDYuCm3gmRZY-HlH7hoCBLQQAvD_BwE";
    } else if (selectedRadioValue === "samsung-notebook") {
        window.location.href = "https://www.samsung.com/sec/event/galaxy-book3/launching/?cid=sec_paid_ppc_google_pc_ecommerce_searchad_text_gnb_%EC%82%BC%EC%84%B1%EB%85%B8%ED%8A%B8%EB%B6%81_pfm&utm_source=google&utm_medium=searchad&utm_campaign=pc&utm_term=%EC%82%BC%EC%84%B1%EB%85%B8%ED%8A%B8%EB%B6%81&_AT=000202C801AD036F8F24&gad=1&gclid=CjwKCAjw_uGmBhBREiwAeOfsd40T38K0gfzgz_2udvX5SW5_tCugrwZFxuDAc0Z4SZkZEwK7nYb70RoC1dQQAvD_BwE";
    } else if (selectedRadioValue === "macbook") {
        window.location.href = "https://www.apple.com/kr/mac/?afid=p238%7CsRsW2eeOa-dc_mtid_18707vxu38484_pcrid_669213638318_pgrid_124600489586_pntwk_g_pchan__pexid__&cid=aos-kr-kwgo-mac--slid---product-";
    } else if (selectedRadioValue === "iphone") {
        window.location.href = "https://www.apple.com/kr/iphone/?afid=p238%7CsqgwRLdf6-dc_mtid_209254jz40384_pcrid_665690656292_pgrid_143760319569_pexid__&cid=wwa-kr-kwgo-iphone-Brand-iPhoneFamily-Announce-"; 
    } else if (selectedRadioValue === "galaxy-phone") {
        window.location.href = "https://www.samsung.com/sec/event/galaxy-z5/galaxystudio/?gad=1&gclid=CjwKCAjw_uGmBhBREiwAeOfsd2fGyKxej_RpY4SlDHcF9D0Tdlc4QjqbKqz1pSSTBvg4fj_tCNu32RoC0VwQAvD_BwE"; 
    }
});