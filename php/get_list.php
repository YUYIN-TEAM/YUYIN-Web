<?php


//$a = system('python ../rec/main_coding.py',$ret);
//$a = system('python ../rec/main_coding.py 2>error.txt',$ret);
$cmd = 'python ../rec/get_list.py';
$a = system($cmd,$ret);
//$cmd = exec('python ../rec/main_oding.py');
//$array = explode(',',$cmd);
//foreach ($array as $value){
//    echo $value."</br>";
//}

//echo "    <script>
//                alert('视频生成完成！');
//                location.href='../generate-8.html';
//          </script>";

echo $ret

//echo $ret

?>