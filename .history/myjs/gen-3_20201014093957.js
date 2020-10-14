$('body').on('change','#upload-3',function(){
    var files = $($(this))[0].files;
    names = [];
    for (i=0;i<files.length;i++)
    {
        var formData = new FormData();
        // var name = $($(this)).val();
        formData.append("file", files[i]);
        console.log('uploading...')
        // formData.append("name", name);
        // $.ajax({
        //     url: 'php/upload.php',
        //     type: 'POST',
        //     data: formData,
        //     processData: false,
        //     contentType: false,
        //     dataType: 'text',
        //     success:function (res) {
        //         // names.push(res.split("/").pop())
        //         // alert(res+'上传成功');
        //         // console.log(res);
        //         location.href = "generate-3.html"
        //     }
        //     ,error:function (res) {
        //         alert(res+'上传错误');
        //         console.log(res);
        //     }
        // });
    }
    alert("上传成功！")
})

function choosedemo(id) {
    var o = String(sessionStorage.getItem("demo"))
    // console.log(o)
    var oid = "demo"+o
    var oe = document.getElementById(oid)
    oe.className = "demo-0"

    var ne = document.getElementById(id)
    ne.className = "demo-1"

    var str = String(id)

    sessionStorage.setItem("demo", str.charAt(str.length-1))

    // alert("done! "+str)
}

function getlist() {
    $.ajax({
        dataType: 'json', type: 'get',
        url: "php/get_list.php",
        data:{},
        success: function(msg){
            console.log(msg);    //控制台输出
            show()
        },
        error: function (msg) {
            console.log(msg);    //控制台输出
        }
    });
}

function show(){
    $.ajax({
        url: "./rec/list/upload.txt",
        success: function(msg){
            console.log(msg);    //控制台输出
            var list = document.getElementById("selected")
            names = msg.split(",")
            names.pop()
            var i;
            html = ""
            var len;
            len = names.length;
            if(len>7){
                len = 7
            }
            for(i=0;i<len;i++){
                html+="<div class=\"it\">" +
                    "<video class=\"itv\" controls>" +
                    "<source src=\""+names[i]+"\" type=\"video/mp4\">" +
                    "</video>" +
                    "</div>"
            }

            for(i=len;i<7;i++){
                html+="<div class=\"it\">" +
                    "</div>"
            }


            html+="<div class=\"items-1\">" +
                "<input class=\"upload\" type=\"file\" multiple id=\"upload-3\">" +
                "<img src=\"img/plus.png\">\n" +
                "</div>"

            list.innerHTML = html
            console.log(html)
        },
        error: function (msg) {
            console.log(msg);    //控制台输出
        }
    });
}

sessionStorage.setItem("demo", "1")
getlist()
