s = 0
N = []
var making = null;

sessionStorage.setItem("style", "china")

function rec() {
    var demo = String(sessionStorage.getItem("demo"))
    var s = String(sessionStorage.getItem("style"))



    $.ajax({
        dataType: 'json', type: 'get',
        url: "php/music_rec.php",
        data: { demo: demo, style: s },
        success: function (msg) {
            console.log(msg);    //控制台输出
        },
        error: function (msg, XMLHttpResponse, textStatus, errorThrown) {
            console.log("1 异步调用返回失败,XMLHttpResponse.readyState:" + XMLHttpResponse.readyState);
            console.log("2 异步调用返回失败,XMLHttpResponse.status:" + XMLHttpResponse.status);
            console.log("3 异步调用返回失败,textStatus:" + textStatus);
            console.log("4 异步调用返回失败,errorThrown:" + errorThrown);
            console.log(msg);    //控制台输出
        }
    });

    making = null
    making = setInterval("getprocess()", 100);

    // alert("完成！")
    // location.reload()
    // location.href = "./generate-7.html"
}

var p0 = 0
function getprocess() {
    $.ajax({
        // url: "./rec/list/rec_process.txt",
        url: "http://10.214.242.10:1997/test/rec_pg",
        success: function (msg) {
            console.log(msg);    //控制台输出
            msg = msg.responseText
            var process = document.getElementById("reking")
            // html = "<div class=\"hid\">" +
            //     "   </div>" +
            //     "   <div class = \"doing\">" +
            //     "       <p class=\"do1\">"+msg+"%</p>"
            //
            //
            // if(msg==="0"){
            //     html += "       <p class=\"do2\">准备中···</p>" +
            //         "   </div>"
            // }
            // else{
            //     html += "       <p class=\"do2\">音乐推荐中···</p>" +
            //     "   </div>"
            // }

            html = "<div class=\"hid\">" +
                "</div>"

            var p1 = 0

            if (parseInt(msg) > 30) {
                p1 = 1;
            }

            var p2 = 0

            if (parseInt(msg) > 70) {
                p2 = 1;
            }

            if (msg === "75") {
                p0 += 0.3
                msg = parseInt(msg) + parseInt(p0)
                msg = parseInt(msg)
                if (msg >= 96) {
                    msg = 96
                }
            }

            html += "<div class = \"doing\">" +
                "<div class=\"do1 text-center\">" +
                "       <p1>音乐推荐中，请稍候……</p1>" +
                "       <p2>已完成" + msg + "%</p2>" +
                "   </div>" +
                "   </br>" +
                "   </br>" +
                "   <div class=\"process\">" +
                "       <div id=\"ongoing\" style = 'width: " + msg + "%'>" +
                "       </div>" +
                "   </div>" +
                "   <div class=\"do2\">" +
                "       <div class=\"step col-md-4\">" +
                "           <img src=\"./img/icon/0-1.png\" id=\"i0\" class=\"icon-0\">" +
                "           <p>视频分析</p>" +
                "       </div>" +
                "       <div class=\"step col-md-4\">" +
                "           <img src=\"./img/icon/1-" + p1 + ".png\" id=\"i1\" class=\"icon-0\">" +
                "           <p>视觉推荐</p>" +
                "       </div>" +
                "       <div class=\"step col-md-4\">" +
                "           <img src=\"./img/icon/2-" + p2 + ".png\" id=\"i2\" class=\"icon-0\">" +
                "           <p>情感推荐</p>" +
                "       </div>" +
                "   </div>" +
                "</div>"
            process.innerHTML = html

            // var bar = document.getElementsByClassName("process")
            // // alert(bar.style.width)
            // bar.innerHTML = "<div id=\"ongoing\" style='width: "+msg+"%'>"+
            //                 "</div>"



            if (msg === "100") {
                clearInterval(making);
                making = setTimeout("done()", 100);

            }
            // console.log(html)
        },
        error: function (msg) {
            console.log(msg);    //控制台输出
        }
    });
}

function done() {
    alert("音乐推荐已完成！")
    location.href = "./generate-6.html"

}

function choosestyle(id) {
    sessionStorage.setItem("style", id)

    styles = document.getElementById("g5up")
    styles.innerHTML = "<img src=\"./img/index/style/china-0.png\" id=\"china\" class=\"style-0\" onclick=\"choosestyle(this.id)\">" +
        "<img src=\"./img/index/style/pop-0.png\" id=\"pop\" class=\"style-0\" onclick=\"choosestyle(this.id)\">" +
        "<img src=\"./img/index/style/country-0.png\" id=\"country\" class=\"style-0\" onclick=\"choosestyle(this.id)\">" +
        "<img src=\"./img/index/style/jazz-0.png\" id=\"jazz\" class=\"style-0\" onclick=\"choosestyle(this.id)\">"

    choice = document.getElementById(id)
    choice.src = "./img/index/style/" + id + "-1.png"
    choice.className = "style-1"

    s = sessionStorage.getItem("style")
    console.log(s)
}

function rectest() {
    // var demo = String(sessionStorage.getItem("demo"))
    // var loading = "<div class=\"hid\"></div><div class = \"doing\"><p id= \"percent\" class=\"do1\">6%</p><p class=\"do2\">智能生成中···</p></div>"
    // $("body").prepend(loading)

    var demo = 'test'
    var s = String(sessionStorage.getItem("style"))
    console.log(demo, s)
    // 音乐生成
    $.ajax({
        params: { "contentType": "application/json;charset=utf-8" },
        dataType: 'json', type: 'get',
        url: "http://10.214.242.10:1997/test/rec?name=" + demo + '&style=' + s,
    }).done(function (msg) {
        // msg.setHeader("Access-Control-Allow-Origin", "*");
        console.log(msg);    //控制台输出
    });
    making = null
    making = setInterval("getprocess()", 1000);

}
