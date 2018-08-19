<!DOCTYPE html>
<html lang="zh-CN"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
      <meta name="description" content="OJCoder是一个OJ平台答案查询的网站，你可以在这里查询LeetCode、LintCode、华为OJ等常用OJ平台题目的答案！">
	<meta name="keywords" content="OJ平台,LeetCode,LintCode,答案查询,华为OJ,hihoCoder,算法,数据结构,C++,Java,Python">
    <meta name="author" content="OJCoder">
    <link rel="icon" href="/images/favicon.ico">
    <title>OJ答案查询</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="/css/maizi.css" />
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/css/starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="/js/ie-emulation-modes-warning.js"></script>
	<script src="/js/jquery.min.js"></script>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
	<?php
	if(isset($_SERVER['HTTP_REFERER'])){
		$url = $_SERVER['HTTP_REFERER'];
		$parts = parse_url($url);
		if($parts['host'] == 'wx.ojcoder.cn'){
			echo '<style type="text/css">';
			echo '.navbar{display:none;}';
			echo '.copyright{display:none;}';
			echo 'body{padding-top:0;padding-bottom:20px;}';
			echo '</style>';
		}
	}
	?>
  </head>

  <body>
<?php
require_once('../functions/connect.php');
require_once('../functions/fun.search.php');
$skeywords='LeetCode';
?>
<!--顶部导航栏-->
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/" style="color:#eee;">OJ答案查询</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="/">首页搜索</a></li>
            <li class="active"><a href="/LeetCode">LeetCode</a></li>
            <li><a href="/LintCode">LintCode</a></li>
			<li><a href="/Contribute">贡献代码</a></li>
			<li><a href="/About">关于</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


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
			<h2>LeetCode所有答案</h2>
				<table class="table table-responsive table-hover table-bordered">
					
				<?php 
	$sql=sqlsearch($skeywords);
	$query=mysqli_query($con,$sql);
	$num=mysqli_num_rows($query);
	$flag=0;
	if(!($query && $num))
		echo '<h3 style="text-align:center;">服务器繁忙，请稍后再试!</h3>';
	while($query && $num){
	  while($row=mysqli_fetch_array($query)){  
		  if($flag==0)
		  {
			echo '<div style="font-style: italic">All <strong>'.$num.'</strong> items for LeetCode</div>';
			echo '<tr><th>OJ平台</th><th>编号</th><th>题目</th><th>编程语言</th></tr>';
			$flag=1;				
		  }
		  if($row['platform']=="LeetCode")
			  $outlink="https://leetcode.com/problems/";
		  else if($row['platform']=="LintCode")
			  $outlink="http://www.lintcode.com/zh-cn/problem/";
		  echo '<tr><td><a href="'.$outlink.$row['slink'].'" target='.'"_black">'.$row['platform'].'</a></td>';
		  echo '<td>#'.$row['number'].'</td>';
		  echo '<td><a href="/'.$row['platform'].'/'.$row['number'].'-'.$row['slink'].'">'.$row['title'].'</a></td><td>';
		  $pstr='<a href="/'.$row['platform'].'/'.$row['number'].'-'.$row['slink'].'/index.php?slang=';
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

<!-- 尾部 -->
 <section class="copyright">
	<div class="container">
		<div class="row">
			<div class="col-md-2"></div>
			<div class="col-md-8">
			<footer>
			<img id="weixin_minicode" style="position:absolute;bottom:66px;right:38%;display:none;" src="/images/weixinCoder.jpg" alt="扫码关注微信公众号" class="img-thumbnail" width="120" height="120">
			<p>
			<a href="/">首页</a> | 
			<a href="/About">关于</a> | 
			<a style="cursor:pointer" onmouseover="showElement('weixin_minicode')" onmouseout="hideElement('weixin_minicode')">公众号</a> | 
			<a href="/Support">赞助</a> |
			<a href="mailto:ojcoder@163.com">与我联系</a>
			</p>
	<p>Copyright © 2017 OJCoder | 鄂ICP备16017973号</p>
</footer>
			</div>
			<div class="col-md-2"></div>
		</div>
	</div>
</section>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
	<script src="/js/gotoTop.js"></script>
	<script src="/js/common.js"></script>
    <script src="/js/bootstrap.min.js"></script>
	<div id="tongji"><script src="https://s19.cnzz.com/z_stat.php?id=1262040335&web_id=1262040335" language="JavaScript"></script></div>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/js/ie10-viewport-bug-workaround.js"></script>

</body></html>