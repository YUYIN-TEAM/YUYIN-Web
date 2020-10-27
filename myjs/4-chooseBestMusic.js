s = 0;
N = [];
var making = null;
var domain = "http://www.next.zju.edu.cn/yuyin";
var ip = "http://10.214.242.10:1997";
var s = String(sessionStorage.getItem("style"));
// var se = document.getElementById(s);
// se.className = "divhit-1";

function make_video_php(music_name) {
  // music_name = this.id
  // console.log(music_name)
  var d = String(sessionStorage.getItem("demo"));
  $.ajax({
    dataType: "json",
    type: "get",
    url: "php/video_make.php",
    data: { music: music_name, demo: d, style: s },
    success: function (msg) {
      console.log(msg); //控制台输出
    },
    error: function (msg, XMLHttpResponse, textStatus, errorThrown) {
      console.log(
        "1 异步调用返回失败,XMLHttpResponse.readyState:" +
          XMLHttpResponse.readyState
      );
      console.log(
        "2 异步调用返回失败,XMLHttpResponse.status:" + XMLHttpResponse.status
      );
      console.log("3 异步调用返回失败,textStatus:" + textStatus);
      console.log("4 异步调用返回失败,errorThrown:" + errorThrown);
      console.log(msg); //控制台输出
    },
  });

  making = null;
  making = setInterval("getprocess()", 100);

  // alert("完成！")
  // location.reload()
  // location.href = "./generate-7.html"
}

//qjchen-begin
function make_video(music_name) {
  // music_name = this.id
  $("video").trigger("pause");
  console.log(music_name);
  var demo = "test10";
  demo = sessionStorage.getItem("project_name");
  var s = String(sessionStorage.getItem("style"));
  var d = String(sessionStorage.getItem("demo"));
  console.log(s);
  console.log(d);
  $.ajax({
    dataType: "json",
    type: "get",
    url:
      ip +
      "/test/make?name=" +
      demo +
      "&music_name=" +
      music_name +
      "&style=" +
      s,
    // data: { music: music_name, demo: d, style: s },
    success: function (msg) {
      console.log(msg); //控制台输出
    },
    error: function (msg, XMLHttpResponse, textStatus, errorThrown) {
      console.log(
        "1 异步调用返回失败,XMLHttpResponse.readyState:" +
          XMLHttpResponse.readyState
      );
      console.log(
        "2 异步调用返回失败,XMLHttpResponse.status:" + XMLHttpResponse.status
      );
      console.log("3 异步调用返回失败,textStatus:" + textStatus);
      console.log("4 异步调用返回失败,errorThrown:" + errorThrown);
      console.log(msg); //控制台输出
    },
  });

  making = null;
  making = setInterval("getprocess()", 100);

  // alert("完成！")
  // location.reload()
  // location.href = "./generate-7.html"
}
//qjchen-end

var p0 = 0;

function getprocess() {
  var demo = "test10";
  demo = sessionStorage.getItem("project_name");
  $.ajax({
    url: ip + "/test/make_pg?name=" + demo,
    success: function (msg) {
      console.log(msg); //控制台输出
      msg = msg.responseText;
      var process = document.getElementById("making");

      html = '<div class="hid">' + "</div>";
      var p1 = 0;

      if (msg === "10") {
        p0 += 0.3;
        msg = parseInt(msg) + parseInt(p0);
        msg = parseInt(msg);
        if (msg >= 99) {
          msg = 96;
        }
      }

      if (parseInt(msg) > 30) {
        p1 = 1;
      }

      var p2 = 0;

      if (parseInt(msg) > 70) {
        p2 = 1;
      }

      html +=
        '<div class = "doing">' +
        '<div class="do1 text-center">' +
        '       <p1 id="toastview">视频合成中，请稍候……</p1>' +
        "       <p2>已完成" +
        msg +
        "%</p2>" +
        "   </div>" +
        "   </br>" +
        "   </br>" +
        '   <div class="process">' +
        '       <div id="ongoing" style = \'width: ' +
        msg +
        "%'>" +
        "       </div>" +
        "   </div>" +
        '   <div class="do2">' +
        '       <div class="step col-md-4">' +
        '           <img src="./img/icon/4-1.png" id="i0" class="icon-0">' +
        "           <p>节奏解析</p>" +
        "       </div>" +
        '       <div class="step col-md-4">' +
        '           <img src="./img/icon/5-' +
        p1 +
        '.png" id="i1" class="icon-0">' +
        "           <p>视频剪辑</p>" +
        "       </div>" +
        '       <div class="step col-md-4">' +
        '           <img src="./img/icon/6-' +
        p2 +
        '.png" id="i2" class="icon-0">' +
        "           <p>视频合成</p>" +
        "       </div>" +
        "   </div>" +
        "</div>";
      process.innerHTML = html;

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
      //     html += "       <p class=\"do2\">视频合成中···</p>" +
      //     "   </div>"
      // }
      //
      //
      // process.innerHTML = html

      if (msg === "100") {
        clearInterval(making);
        making = setTimeout("done()", 500);
      }
      // console.log(html)
    },
    error: function (msg) {
      console.log(msg); //控制台输出
    },
  });
}

function done() {
  var msg = "视频合成成功！";
  $("#toastview").text(msg);
  setTimeout(function () {
    location.href = "./5-generateResult.html";
  }, 3000);
  // alert("视频合成已完成！")
}

function split_list_string(responseText) {
  let tempList = responseText.substr(1, responseText.length - 2).split(", ");
  for (let i = 0; i < tempList.length; i++) {
    let nowstr = tempList[i];
    tempList[i] = nowstr.substr(1, nowstr.length - 2);
  }
  return tempList;
}

function musicrec(start) {
  console.log("musicrec");
  var demo = "test10";
  demo = sessionStorage.getItem("project_name");
  getMusicList(demo, start);
}

function getMusicList(demo, start) {
  document.getElementById("showVideo").src =
    "http://10.214.242.10:1998/data/input_video/" + demo + ".mp4";
  $.ajax({
    // url: "./rec/rec_music.txt",
    url: ip + "/test/rec_res?name=" + demo,
    success: function (msg) {
      console.log(msg.responseText); //控制台输出
      var songList = msg.responseText;
      var list = document.getElementById("recmus");
      console.log(songList);
      // let names = songList.split(",")
      // names.pop()
      // console.log(names)
      let N = songList;
      names = songList;
      html = "";
      start = start % names.length;
      end = start + 3;
      len = end > names.length ? names.length : end;
      s = String(sessionStorage.getItem("style"));
      console.log("style", s);
      console.log(names);
      for (var i = 1; i <= 3; i++) {
        var name = "myVideo" + i;
        addPlaySyncListener(name, songList[i - 1].start, songList[i - 1].end);
      }
      for (i = start; i < len; i++) {
        n = ip + "/data/data/music/" + s + "/" + songList[i].name;
        var musicPlayer = "myVideo" + (i + 1);
        document.getElementById(musicPlayer).src = n; // 设置播放音乐
        document.getElementById(musicPlayer).nextElementSibling.id =
          songList[i].name; //设置button id
        html +=
          '<div class="adiv">' +
          "       <video controls>" +
          '           <source src = "' +
          n +
          '" type = "audio/mpeg">' +
          "       </video>" +
          '       <div class="audio-right">' +
          '           <div class="ar1">' +
          // "               <a href=\"./php/video_make.php\"><button class=\"arbt2\" id = "+names[i]+">使用</button></a>" +
          '               <button class="arbt2" id = ' +
          names[i] +
          " onclick = make_video(this.id)>使用</button>" +
          "           </div>" +
          "       </div>" +
          "   </div>";
      }

      // for (let i = 0; i < end - names.length; i++) {
      //     n = "http://10.214.242.10:1997/music/music/" + s + "/" + names[i];
      //     html += "<div class=\"adiv\">" +
      //         "       <video controls>" +
      //         "           <source src = \"" + n + "\" type = \"audio/mpeg\">" +
      //         "       </video>" +
      //         "       <div class=\"audio-right\">" +
      //         "           <div class=\"ar1\">" +
      //         // "               <a href=\"./php/video_make.php\"><button class=\"arbt2\" id = "+names[i]+">使用</button></a>" +
      //         "               <button class=\"arbt2\" id = " + names[i] + " onclick = make_video(this.id)>使用</button>" +
      //         "           </div>" +
      //         "       </div>" +
      //         "   </div>"
      // }

      // html += "<br>" +
      //     "<a class=\"change\" onclick=\"change()\">不喜欢？点我换一批</a>"

      // list.innerHTML = html;
      // console.log(html)
    },
    error: function (msg) {
      console.log(msg); //控制台输出
    },
  });
}

function change() {
  s += 3;
  musicrec(s);
}

function pauseOtherPlayers(musicPlayer) {
  for (var i = 1; i <= 3; i++) {
    var myVideo = document.getElementById("myVideo" + i);
    console.log(musicPlayer)
    if (musicPlayer != "myVideo" + i) {
      console.log(musicPlayer, "myVideo" + i);
      myVideo.pause();
    }
  }
}

function addPlaySyncListener(musicPlayer, start, end) {
  var showVideo = document.getElementById("showVideo");
  var myVideo = document.getElementById(musicPlayer);
  myVideo.currentTime = start; //set Start Time
  console.log(musicPlayer, start, end);
  // var end = 13;
  myVideo.addEventListener("pause", function () {
    myVideo.currentTime = start;
    myVideo.pause();
    showVideo.currentTime = 0;
    showVideo.pause();
  });

  myVideo.addEventListener("play", function () {
    pauseOtherPlayers(musicPlayer);
    myVideo.play();
  });
  myVideo.addEventListener("timeupdate", function () {
    if (myVideo.currentTime > end) {
      myVideo.currentTime = start;
      myVideo.pause();
    }
    if (myVideo.paused === false && showVideo.paused === true) {
      showVideo.play();
    }
  });
}

setTimeout(musicrec(0), 2000);
setTimeout(musicrec(0), 2000);
