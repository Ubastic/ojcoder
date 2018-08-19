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
	<script src="/js/ace/ace.js" type="text/javascript" charset="utf-8"></script>
    <script src="/js/ace/ext-language_tools.js" type="text/javascript" charset="utf-8"></script>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
<?php
$splatform="";$stitle="";$slang="";$sfilename="";
if ($_SERVER["REQUEST_METHOD"] == "GET")
{
	if(!strpos($_SERVER['REQUEST_URI'],'splatform')||!strpos($_SERVER['REQUEST_URI'],'stitle')||!strpos($_SERVER['REQUEST_URI'],'slang')||!strpos($_SERVER['REQUEST_URI'],'sfilename'))
		echo "<script>window.location.href='/Contribute';</script>";
	$splatform=trim($_GET["splatform"]);
	$stitle=trim($_GET["stitle"]);
	$slang=trim($_GET["slang"]);
	$sfilename=trim($_GET["sfilename"]);
    if (empty($splatform)||empty($stitle)||empty($slang)||empty($sfilename))
    {
        echo "<script>window.location.href='/Contribute';</script>";
    }
}
$stitle='['.$splatform.']'.$stitle.'['.$slang.' '.$sfilename.']';
?>
<?php
// 定义变量并默认设置为空值
$sdiscription="";
$scontact="";
if ($_SERVER["REQUEST_METHOD"] == "POST")
{
	if(!empty(trim($_POST["stitle"])))
		$stitle=trim($_POST["stitle"]);
	if(!empty(trim($_POST["sdiscription"])))
		$sdiscription=trim($_POST["sdiscription"]);
	if(!empty(trim($_POST["scontact"])))
		$scontact=trim($_POST["scontact"]);
	if(empty($sdiscription)||empty($stitle))
	{
		echo '<script>alert("反馈内容不能为空！");</script>';
	}
	else
	{
		$savepath='./files/Feedback.dat';
		$myfile = fopen($savepath, "a");
		if($myfile)
		{
			date_default_timezone_set('PRC');//其中PRC为“中华人民共和国”
			fwrite($myfile, "Time: ".date("Y/m/d")."  ".date("H:i:sa")."\r\n");
			fwrite($myfile, "Title: ".$stitle."\r\n");
			fwrite($myfile, "Author: ".$scontact."\r\n");
			fwrite($myfile, "Discription: \r\n".$sdiscription."\r\n");
			fwrite($myfile, "-------------------------------------------------------------------------------------\r\n\r\n\r\n");
			fclose($myfile);
			$sdiscription="";
			$scontact="";
			echo '<script>alert("提交成功，感谢您的贡献！页面将关闭...");window.opener=null;window.open("","_self");window.close();</script>';
		}else
		{
			echo '<script>alert("提交失败，请重试！");</script>';
		}
	}
}
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
            <li><a href="/LeetCode">LeetCode</a></li>
            <li><a href="/LintCode">LintCode</a></li>
			<li class="active"><a href="/Contribute">贡献代码</a></li>
			<li><a href="/About">关于</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
<!--搜索区-->
    <section>
	<div class="container">
		<div class="row">
			<div class="col-md-2"></div>
			<div class="col-md-8">
			<div class="contributeHeader"><h2>问题反馈</h2><div class="contributeTips"><div><strong>Tips:</strong></div>
			<div>1. 如果您发现答案错误或者可以改进，请在此页面反馈；</div>
			<div>2. 请在反馈内容中写明改正/改进思路，并附上修改之后的代码；</div>
			<div>3. 您贡献的代码将被网友参考，请附上您的邮箱等联系方式，方便交流。</div>
			</div></div>
				<div class="contributeContent">
				<form class="form-horizontal" method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> 
  <div class="form-group">
    
    <div class="col-sm-6">
      <input type="text" name="stitle" class="form-control" id="stitle" <?php 
	  if(empty($stitle)) 
	  {echo 'placeholder="输入题目"';}
	else {echo 'value="'.$stitle.'"';} 
		  ?> readonly>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-12"><pre id="code" class="ace_editor" style="min-height:400px"> 
	<textarea class="ace_text-input" rows="10"><?php 
	  if(!empty($ssolution)) 
	   {echo $ssolution;} 
		  ?></textarea></pre>
    </div>
  </div>
  <div class="form-group">
    
    <div class="col-sm-12">
	<textarea name="sdiscription" class="form-control" id="sdiscription" rows="10" style="display:none;"></textarea>
    </div>
  </div>
  <div class="form-group">
    
    <div class="col-sm-6">
      <input type="text" name="scontact" class="form-control" id="scontact" <?php 
	  if(empty($scontact)) 
	  {echo 'placeholder="邮箱/GitHub/QQ"';}
	else {echo 'value="'.$scontact.'"';} 
		  ?>>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-info">提交</button>
    </div>
  </div>
  <script>
            //初始化对象
            editor = ace.edit("code");
            
            //设置风格和语言（更多风格和语言，请到github上相应目录查看）
            theme = "xcode"
            language = "c_cpp"
            editor.setTheme("ace/theme/" + theme);
            editor.session.setMode("ace/mode/" + language);
            
            //字体大小
            editor.setFontSize(18);
            
            //设置只读（true时只读，用于展示代码）
            editor.setReadOnly(false); 
            
            //自动换行,设置为off关闭
            editor.setOption("wrap", "free")
            //设置默认值
			editor.setValue("/*\nTitle:\nDescription:\n*/\n\n//Write solution here"); // or session.setValue
            //启用提示菜单
            ace.require("ace/ext/language_tools");
            editor.setOptions({
				enableBasicAutocompletion: true,
				enableSnippets: true,
				enableLiveAutocompletion: true
			});
			//监听事件	
			editor.getSession().on('change', function(e) {
				var obj =  document.getElementById("sdiscription"); 
				obj.value = editor.getValue();
			});
        </script>
</form></div>
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
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/js/ie10-viewport-bug-workaround.js"></script>
  

</body></html>