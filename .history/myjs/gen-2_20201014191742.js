$("body").on("change", "#upload", function () {

  var files = $($(this))[0].files;
  names = [];
  console.log('uploading...')
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
