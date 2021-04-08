// 輪播效果
// ========簡單輪播圖 圖片自動切換========
// setInterval(function() {
//         var li = document.querySelector('.img_li');
//         var ul = document.getElementById('imgs');

//         ul.appendChild(li); //向父元素添加最後一個子元素
//     }, 3000)


// ========簡單輪播圖 鼠標懸浮切換圖片(CSS控制顯示以及隱藏)======== 
// 先獲取所有的dot
function userCarousel() {
    var dot_lis = document.querySelectorAll('.dot');

    // 指定所有鼠標漂浮事件
    for (var i = 0; i < dot_lis.length; i++) {
        // 各個事件
        dot_lis[i].onmouseover = function() {
            // 先隱藏所有圖片 & dot
            var img_lis = document.querySelectorAll('.img_li');
            for (var j = 0; j < img_lis.length; j++) {
                img_lis[j].style.display = 'none'; //隱藏所有圖片
                dot_lis[j].style.backgroundColor = '' //隱藏所有dot

            }

            // 再讓選取的dot增加背景色
            this.style.backgroundColor = "rgb(226, 45, 32)"
                // 顯示對應的圖片
                // console.log(this);
                // console.log(this.getAttribute('data'));
            var index = this.getAttribute('data');
            img_lis[index].style.display = 'block';
        }
    }
}

// 首頁隱藏原本的動態字詞"none"讓它顯示
function textNone() {
    var successBtn = document.getElementById("successBtn");
    var success = document.getElementById("success");

    successBtn.onclick = function() {
        success.style.display = 'block';
    }
}