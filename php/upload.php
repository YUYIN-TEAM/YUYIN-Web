<?php
    header('Content-type:text/json;charset=utf-8');

    $F = $_FILES['file'];
    $fname = $F['name'];
    $des_path = "../upload/".$fname;

    $res = move_uploaded_file($F["tmp_name"],$des_path);
    echo $des_path;




//    $a = system('python ../analyze/ana.py');
//    echo "<script>alert('分析完成！')";
//    echo "location.href='../generate-3.html';";
//    echo "</script>";
?>