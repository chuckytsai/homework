// 首頁隱藏原本的動態字詞"none"讓它顯示
function textNone() {
    var successBtn = document.getElementById("successBtn");
    var success = document.getElementById("success");

    successBtn.onclick = function() {
        success.style.display = 'block';
    }
}

// 查詢會員名字資料API
window.onload = function() {
    var gogo = document.getElementById('ContentType');
    var OKMassage = document.getElementById("OKMassage");
    var errorMassage = document.getElementById("errorMassage");
    // var data = { "name": "Ultron" }

    gogo.addEventListener('submit', function(event) {
        event.preventDefault();
        var nameStr = document.getElementById("userKey").value;
        var sendData = { "oldName": "Ultron", "name": nameStr }
        fetch("http://127.0.0.1:3000/api/user", {
                method: "POST",
                body: JSON.stringify(sendData),
                headers: ({ 'Content-Type': 'application/json' })
            }).then((response) => response.text())
            .then((data) => {
                OKMassage.style.display = 'block';
                errorMassage.style.display = 'none';
                console.log({
                    "ok": true
                }, data);
            })
            .catch((error) => {
                errorMassage.style.display = 'block';
                OKMassage.style.display = 'none';
                console.log({
                    "error": true
                }, error);
            })
    })
}