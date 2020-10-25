<?php
$d = $_GET["demo"];
$s = $_GET["style"];
//echo $d;
//$a = system('python ../rec/main_coding.py',$ret);
//$a = system('python ../rec/main_coding.py 2>error.txt',$ret);

//$cmd = exec('python ../rec/main_oding.py');
//$array = explode(',',$cmd);
//foreach ($array as $value){
//    echo $value."</br>";
//}
//ignore_user_abort(true); // 后台运行
//set_time_limit(0); // 取消脚本运行时间的超时上限
$cmd = 'python ../rec/main_coding.py '.$d." ".$s;
$a = system($cmd,$ret);

//echo "    <script>
//                alert('音乐推荐完成！');
//                location.href='../4-chooseBestMusic.html';
//          </script>";

echo $ret

?>