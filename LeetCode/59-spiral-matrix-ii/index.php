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
 <link href="/css/tomorrow.min.css" rel="stylesheet">

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
// 定义变量并默认设置为空值
$slang='cpp';
if ($_SERVER["REQUEST_METHOD"] == "GET")
{
    if (!empty($_GET["slang"]))
    {
        $slang = test_input($_GET["slang"]);
        // 检测名字是否只包含字母跟空格
        if ($slang!='cpp' && $slang!='java' && $slang!='python')
        {
            $slang = "cpp"; 
        }
		if($slang == 'python' )
			$slang = "py"; 
    } 
}
function test_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
	$data = strtolower($data);
    return $data;
}
$splatform="";
$snumber=0;
$token = strtok($_SERVER['REQUEST_URI'], "/");
if ($token !== false)
{
	$splatform=$token;
}
$token = strtok("/");
if ($token !== false)
{
$snumber=intval($token);
}
?>

<?php
$stitle="";
require_once('../connect.php');
$sql='select title from problems where platform="'.$splatform.'" and number='.$snumber.' and(cpp or java or python)';
	$query=mysqli_query($con,$sql);
	$num=mysqli_num_rows($query);
	if($query && $num)
	{
		$row=mysqli_fetch_array($query);
		$stitle=$row['title'];
		$stitle='['.$splatform.']#'.$snumber.'&nbsp;&nbsp;'.$stitle;
	}
	else
		$stitle="读取标题失败！";
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

<section id="codeArea">
	<div class="container">
	<div class="row">
		<div class="col-md-2"></div>
		<div class="col-md-8"><?php
			echo '<h2>'.$stitle.'</h2>';
		?>
		</div>
		<div class="col-md-2"></div>
	</div>
	
	<?php
		$dir='./';
		// 打开目录，然后读取其内容
			if ($dh = opendir($dir)){
				$num=0;
				while (($file = readdir($dh)) !== false){
					if($file!='.' && $file!='..' && strpos($file,$slang,2))
					{
						$num=$num+1;
						echo '<div class="row"><div class="col-md-2"></div><div class="col-md-8">';
						$str=$dir.$file;
						$myfile = fopen($str, "r");
						if($myfile)
						{
							$strclipid='clipboard'.$num;
							echo '<div class="solution"><span class="solutiontitle"><a href="#'.$strclipid.'" data-toggle="collapse" title="点击折叠/展开代码"> Solution'.$num.'.'.$slang.'</a></span>';
							echo '<a href="javascript:void(0);" class="btn default btn-sm active" role="button">';
							echo '<span class="btn-copy" data-clipboard-target="#'.$strclipid.'" aria-label="复制成功" title="点击复制代码">复制代码</span></a>';
							echo '<a href="/feedback/index.php?splatform='.$splatform.'&stitle='.$row['title'].'&slang='.$slang.'&sfilename=Solution '.$num.'" class="btn default btn-sm active" role="button" target="_blank">代码报错/优化</a>';
							echo '</div><div></div>';
							echo '<pre class="prettyprint linenums lang-'.$slang.'" id="'.$strclipid.'">';
							while(!feof($myfile)) {
								$slin = fgets($myfile);
								echo htmlspecialchars($slin);
							}
							fclose($myfile);
							echo '</pre>';
						}
						echo '</div><div class="col-md-2"></div></div>';
					}
				}
				closedir($dh);
			}
	?>
	</div>
</section>
<script src="/js/clipboard.min.js"></script>
<script>
//new Clipboard('.btn');
var clipboard = new Clipboard('.btn-copy');
clipboard.on('success', function(e) {
	var msg = e.trigger.getAttribute('aria-label');
	alert(msg);
    console.info('Action:', e.action);
    console.info('Text:', e.text);
    console.info('Trigger:', e.trigger);

    e.clearSelection();
});
</script>

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
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/js/ie10-viewport-bug-workaround.js"></script>
    <script src="/js/run_prettify.js"></script>
	
</body></html>