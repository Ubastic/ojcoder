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
  </head>

  <body>

<?php
$urls = array(
    'https://www.ojcoder.cn/index.php',
	'https://www.ojcoder.cn/results.php',
	'https://www.ojcoder.cn/LeetCode/index.php',
	'https://www.ojcoder.cn/LintCode/index.php',
	'https://www.ojcoder.cn/About/index.php',
	'https://www.ojcoder.cn/Contribute/index.php',
);
$api = 'http://data.zz.baidu.com/urls?site=www.ojcoder.cn&token=y6IJsvH3xrVHTmOT';
$ch = curl_init();
$options =  array(
    CURLOPT_URL => $api,
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => implode("\n", $urls),
    CURLOPT_HTTPHEADER => array('Content-Type: text/plain'),
);
curl_setopt_array($ch, $options);
$result = curl_exec($ch);
echo $result;
?>
</body></html>