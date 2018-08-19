<?php
  header("Content-type: text/html; charset=utf-8");
  define('HOST','127.0.0.1');
  define('USERNAME','root');
  define('PASSWORD','wuxubj1992');
  //连接
  if(!$con=mysqli_connect(HOST,USERNAME,PASSWORD)){
	echo '连接失败';  
  }
  //选库
  if(!mysqli_select_db($con,'ojcoder')){
	echo '选库失败';      
  }
  //字符集
  if(!mysqli_query($con,'set names utf8')){
	echo '设置字符集失败';  
  }

?>