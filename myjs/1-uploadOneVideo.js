var domain = "http://www.next.zju.edu.cn/yuyin"
var ip = "http://10.214.242.10:1997"
function postData() {
  // var formData = new FormData();
  var demo = "test10";
  var project_name = Math.random().toString(36).substr(2);
  sessionStorage.setItem("project_name", project_name);
  console.log(project_name);
  var formData = new FormData(document.getElementById("upload_file"));

  console.log(formData);
  var url = [
    ip + "/upload/upload?upload_project_name=",
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
        ip + "/data/data/input_video/" + project_name
      );
      console.log("after", res);
      var video_urls = {"urls": []}
      video_urls["urls"].push(res)

      sessionStorage.setItem("upload_video_url", JSON.stringify(video_urls));
      window.location.href = "2-uploadVideos.html";
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
$("body").on("change", "#upload", function () {
  var mask =
    '<div class="hid"></div><div class = "doing-small"><p class="do-small2">智能生成中···</p></div>';
  $("body").prepend(mask); 
  // qjchen begin
  postData();
  // qjchen end
  //   var files = $($(this))[0].files;
  //   names = [];
  //   console.log('uploading...')
  //   for (i = 0; i < files.length; i++) {
  //     var formData = new FormData();
  //     // var name = $($(this)).val();
  //     formData.append("file", files[i]);
  //     // formData.append("name", name);
  //     $.ajax({
  //       url: "php/upload.php",
  //       type: "POST",
  //       data: formData,
  //       processData: false,
  //       contentType: false,
  //       dataType: "text",
  //       success: function (res) {
  //         // names.push(res.split("/").pop())
  //         // alert(res+'上传成功');
  //         // console.log(res);
  //         location.href = "generate-3.html";
  //       },
  //       error: function (res) {
  //         alert(res + "上传错误");
  //         console.log(res);
  //       },
  //     });
  //   }
  //   alert("上传成功！");
});
