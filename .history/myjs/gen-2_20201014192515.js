function postData() {
    // var formData = new FormData();
    var demo = 'test10'
    var project_name = Math.random().toString(36).substr(2);
    console.log(project_name)
    var formData = new FormData(document.getElementById("upload_file"));
    console.log(formData);
    var url = [
      "http://10.214.242.10:9880/upload?upload_project_name=",
      project_name,
      "&upload_type=web"
    ].join("");
    console.log(url);
    // console.log($("#upload_project_name").val());
    // $.ajax({
    //   url: url, /*接口域名地址*/
    //   type: "post",
    //   data: formData,
    //   contentType: false,
    //   processData: false,
    //   success: function (res) {
    //     console.log('before', res);
    //     res = res.replace("http://10.214.242.10:9881/YUYIN1004/data/input_video","http://10.214.242.10:1998/data/input_video/"+ $("#upload_project_name").val())
    //     console.log('after', res)
    //     sessionStorage.setItem("upload_video_url", res)

    //     // alert(res);
    //     // if (res.data["code"] == "succ") {
    //     //   alert("成功");
    //     // } else if (res.data["code"] == "err") {
    //     //   alert("失败");
    //     // } else {
    //     //   console.log(res);
    //     // }
    //   },
    // });
  }
$("body").on("change", "#upload", function () {

    // qjchen begin
    postData()
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
