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
	<script src="/js/ace/ace.js"></script>
    <script src="/js/ace/ext-language_tools.js"></script>
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

<?php
// 定义变量并默认设置为空值
$ssolution="";
$scontact="";
if ($_SERVER["REQUEST_METHOD"] == "POST")
{
	if(!empty(trim($_POST["ssolution"])))
		$ssolution=trim($_POST["ssolution"]);
	if(!empty(trim($_POST["scontact"])))
		$scontact=trim($_POST["scontact"]);
	
	if (empty($ssolution))
	{
		echo '<script>alert("题目、描述和答案不能为空！");</script>';
	}
	else
	{
		$savepath='./files/Contribute.dat';
		$myfile = fopen($savepath, "a");
		if($myfile)
		{
			date_default_timezone_set('PRC');//其中PRC为“中华人民共和国”
			fwrite($myfile, "Time: ".date("Y/m/d")."  ".date("H:i:sa")."\r\n");
			fwrite($myfile, "Author: ".$scontact."\r\n");
			fwrite($myfile, "Solution: \r\n".$ssolution."\r\n");
			fwrite($myfile, "-------------------------------------------------------------------------------------\r\n\r\n\r\n");
			fclose($myfile);
			$ssolution="";
			$scontact="";
			echo '<script>alert("提交成功，感谢您的贡献！");</script>';
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
			<div class="contributeHeader"><h2>贡献代码</h2><div class="contributeTips"><div><strong>Tips:</strong></div>
			<div>1. 可对已有题目贡献新的答案，也可贡献新的题目和答案；</div>
			<div>2. 可在代码注释中添加您的版权声明，也可添加您的邮箱、个人博客、GitHub地址等；</div>
			<div>3. 您贡献的代码将被网友参考，我对您的贡献表示万分感谢！</div>
			</div></div>
				<div class="contributeContent">
				<form class="form-horizontal" method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> 
  <div class="form-group">
    <div class="col-sm-12"><pre id="code" class="ace_editor" style="min-height:400px"> 
	<textarea class="ace_text-input" rows="10"><?php 
	  if(!empty($ssolution)) 
	   {echo $ssolution;} 
		  ?></textarea></pre>
    </div>
  </div>
   <div class="form-group">
    <div class="col-sm-10">
	<textarea name="ssolution" id="ssolution" placeholder="" rows="10" style="display:none;"></textarea>
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
				var obj =  document.getElementById("ssolution"); 
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
	<div id="tongji"><script src="https://s19.cnzz.com/z_stat.php?id=1262040335&web_id=1262040335" language="JavaScript"></script></div>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/js/ie10-viewport-bug-workaround.js"></script>
  
<iframe id="id_iframe" name="nm_iframe" style="display:none;"></iframe>   
</body></html>