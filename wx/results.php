<!DOCTYPE html>
<html lang="zh-CN"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
      <meta name="description" content="OJCoder是一个OJ平台答案查询的网站，你可以在这里查询LeetCode、LintCode、华为OJ等常用OJ平台题目的答案！">
	<meta name="keywords" content="OJ平台,LeetCode,LintCode,答案查询,华为OJ,hihoCoder,算法,数据结构,C++,Java,Python">
    <meta name="author" content="OJCoder">
    <link rel="icon" href="https://www.ojcoder.cn/images/favicon.ico">
    <title>OJ答案查询</title>
    <!-- Bootstrap core CSS -->
    <link href="https://www.ojcoder.cn/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://www.ojcoder.cn/css/maizi.css" />
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="https://www.ojcoder.cn/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="https://www.ojcoder.cn/css/starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="https://www.ojcoder.cn/js/ie-emulation-modes-warning.js" charset="utf-8" type="text/javascript"></script>
	<script src="https://www.ojcoder.cn/js/jquery.min.js" charset="utf-8" type="text/javascript"></script>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
<?php
ini_set('display_errors','on');
error_reporting(E_ALL);
require_once('./functions/connect.php');
require_once('./functions/fun.search.php');
$skeywords="";
if ($_SERVER["REQUEST_METHOD"] == "GET")
{
    if (!empty($_GET["keywords"]))
    {
        $skeywords = $_GET["keywords"];
    } 
}
?>

<!-- 搜索结果列表区域 -->
<section id="content">
	<div class="container">
		<div class="row">
		</div>
	</div>
</section>
<section id="list">
	<div class="container">
		<div class="row">
		<div class="col-md-2"></div>
			<div class="col-md-8">
				<table class="table table-responsive table-hover table-bordered">
					
				<?php 
	$sql=sqlsearch($skeywords);
	$query=mysqli_query($con,$sql);
	$num=mysqli_num_rows($query);
	$flag=0;
	if(!($query && $num))
		echo '<h3 style="text-align:center;">No result!</h3>';
	while($query && $num){
	  while($row=mysqli_fetch_array($query)){  
		  if($flag==0)
		  {
			echo '<div style="font-style: italic">All <strong>'.$num.'</strong> items for keywords "'.$skeywords.'"</div>';
			echo '<tr><th>OJ平台</th><th>编号</th><th>题目</th><th>编程语言</th></tr>';
			$flag=1;				
		  }
		  if($row['platform']=="LeetCode")
			  $outlink="https://leetcode.com/problems/";
		  else if($row['platform']=="LintCode")
			  $outlink="http://www.lintcode.com/zh-cn/problem/";
		  echo '<tr><td><a href="'.$outlink.$row['slink'].'" target='.'"_black">'.$row['platform'].'</a></td>';
		  echo '<td>#'.$row['number'].'</td>';
		  echo '<td><a href="https://www.ojcoder.cn/'.$row['platform'].'/'.$row['number'].'-'.$row['slink'].'">'.$row['title'].'</a></td><td>';
		  $pstr='<a href="https://www.ojcoder.cn/'.$row['platform'].'/'.$row['number'].'-'.$row['slink'].'/index.php?slang=';
		  if($row['cpp']!=0) 
			  echo $pstr.'cpp" class="btnlang">Cpp</a>';
		  if($row['java']!=0) 
			  echo $pstr.'java" class="btnlang">Java</a>';
		  if($row['python']!=0) 
			  echo $pstr.'python" class="btnlang">Python</a>';
		  echo '</td></tr>';	
		}
	  $num=$num-1;
	}
?>
				</table>
			</div>
			<div class="col-md-2"></div>
		</div>
	</div>
</section>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
	<script src="https://www.ojcoder.cn/js/gotoTop.js" charset="utf-8" type="text/javascript"></script>
	<script src="https://www.ojcoder.cn/js/common.js" charset="utf-8" type="text/javascript"></script>
    <script src="https://www.ojcoder.cn/js/bootstrap.min.js" charset="utf-8" type="text/javascript"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="https://www.ojcoder.cn/js/ie10-viewport-bug-workaround.js" charset="utf-8" type="text/javascript"></script>

</body></html>