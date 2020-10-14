
function postData() {
    // var formData = new FormData();
    var demo = "test10";
    // var project_name = Math.random().toString(36).substr(2);
    sessionStorage.setItem("project_name", project_name);
    project_name = sessionStorage.getItem("project_name")
    console.log(project_name);
    var formData = new FormData(document.getElementById("upload_file"));
    console.log(formData);
    var url = [
      "http://10.214.242.10:9880/upload?upload_project_name=",
      project_name,
      "&upload_type=web",
    ].join("");
    console.log(url);
    $.ajax({
      url: url /*接口域名地址*/,
      type: "post",
      data: formData,
      contentType: false,
      processData: false,
      success: function (res) {
        console.log("before", res);
        res = res.replace(
          "http://10.214.242.10:9881/YUYIN1004/data/input_video",
          "http://10.214.242.10:1998/data/input_video/" + project_name
        );
        console.log("after", res);
        sessionStorage.setItem("upload_video_url", res);
        window.location.href = "generate-3.html";
        // alert(res);
        // if (res.data["code"] == "succ") {
        //   alert("成功");
        // } else if (res.data["code"] == "err") {
        //   alert("失败");
        // } else {
        //   console.log(res);
        // }
      },
    });
  }

$("body").on("change", "#upload-3", function () {
  var files = $($(this))[0].files;
  names = [];
  for (i = 0; i < files.length; i++) {
    var formData = new FormData();
    // var name = $($(this)).val();
    formData.append("file", files[i]);
    // formData.append("name", name);
    $.ajax({
      url: "php/upload.php",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      dataType: "text",
      success: function (res) {
        // names.push(res.split("/").pop())
        // alert(res+'上传成功');
        // console.log(res);
        location.href = "generate-3.html";
      },
      error: function (res) {
        alert(res + "上传错误");
        console.log(res);
      },
    });
  }
  alert("上传成功！");
});

function choosedemo(id) {
  var o = String(sessionStorage.getItem("demo"));
  // console.log(o)
  var oid = "demo" + o;
  var oe = document.getElementById(oid);
  oe.className = "demo-0";

  var ne = document.getElementById(id);
  ne.className = "demo-1";

  var str = String(id);

  sessionStorage.setItem("demo", str.charAt(str.length - 1));

  // alert("done! "+str)
}

function getlist() {
  var upload_video_url = sessionStorage.getItem("upload_video_url");
  var project_name = sessionStorage.getItem("project_name");
  console.log(upload_video_url, project_name);
  var loaded_video =
    '<video class="itv" controls><source src="' +
    upload_video_url +
    '" type="video/mp4" /></video>';
  $("#itv1").append(loaded_video);
  //   $.ajax({
  //     dataType: "json",
  //     type: "get",
  //     url: "php/get_list.php",
  //     data: {},
  //     success: function (msg) {
  //       console.log(msg); //控制台输出
  //       show();
  //     },
  //     error: function (msg) {
  //       console.log(msg); //控制台输出
  //     },
  //   });
}

function show() {
  $.ajax({
    url: "./rec/list/upload.txt",
    success: function (msg) {
      console.log(msg); //控制台输出
      var list = document.getElementById("selected");
      names = msg.split(",");
      names.pop();
      var i;
      html = "";
      var len;
      len = names.length;
      if (len > 7) {
        len = 7;
      }
      for (i = 0; i < len; i++) {
        html +=
          '<div class="it">' +
          '<video class="itv" controls>' +
          '<source src="' +
          names[i] +
          '" type="video/mp4">' +
          "</video>" +
          "</div>";
      }

      for (i = len; i < 7; i++) {
        html += '<div class="it">' + "</div>";
      }

      html +=
        '<div class="items-1">' +
        '<input class="upload" type="file" multiple id="upload-3">' +
        '<img src="img/plus.png">\n' +
        "</div>";

      list.innerHTML = html;
      console.log(html);
    },
    error: function (msg) {
      console.log(msg); //控制台输出
    },
  });
}

sessionStorage.setItem("demo", "1");
getlist();
