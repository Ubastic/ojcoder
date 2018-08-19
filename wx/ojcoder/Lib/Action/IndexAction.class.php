<?php
function SearchByTitle($str) {
  $sql='select * from problems where title like "%'.$str.'%" and (cpp or java or python) order by number';
  return $sql;
}

function SearchByPlatform($str) {
  $sql='select * from problems where platform like "%'.$str.'%" and (cpp or java or python) order by number';
  return $sql;
}

function SearchByNum($num) {
  $sql='select * from problems where number='.$num.' and (cpp or java or python) order by number';
  return $sql;
}

function sqlsearch($str){
	$sql='select * from problems where title=""';
	$str=trim($str);
	if(!empty($str))
	{
		if(is_numeric($str))
		{
			$sql=SearchByNum($str);
		}
		else if(strtolower($str)=='leetcode' || strtolower($str)=='lintcode')
		{
			$sql=SearchByPlatform($str);
		}
		else
		{
			$sql=SearchByTitle($str);
		}
	}
	return $sql;
}

function strToNum($str){
		$arr1=['零'=>'', '一'=>1, '二'=>2, '三'=>3, '四'=>4, '五'=>5, '六'=>6, '七'=>7, '八'=>8, '九'=>9];
		$arr2=['亿'=>100000000,'千万'=>10000000,'百万'=>1000000,'十万'=>100000,'万'=>10000,'千'=>1000,'百'=>100,'十'=>10];
		preg_match_all('/(零|一|二|三|四|五|六|七|八|九|十|百|千|万|亿)+/i',$str,$result);
		if(empty($result[0][0])) return $str;
		else $tmp=$result[0][0];
		$tmp=str_replace(array_keys($arr1), array_values($arr1), $tmp);
		foreach ($arr2 as $k => $v) {
			if(strlen($tmp)==1) $tmpArr[1]=$tmp;
			else if(strpos($tmp, $k)!==false){
				$tmpArr[$v]=getFromStr('',$k,$tmp);
				$tmp=getFromStr($k,'',$tmp);
				if(strlen($tmp)==1) $tmpArr[1]=$tmp;
			}
		}
		if(is_array($tmpArr)){
			$num=0;
			foreach ($tmpArr as $k => $v) {
				if(empty($v)) $v=1;
				$num+=$k*$v;
			}
		}

		if(!empty($num)) return str_replace($result[0][0], $num, $str);else return $str;
	}

function getFromStr($start,$end,$str)
{
    if(!empty($start)) $str=substr($str,strpos($str,$start)+strlen($start) ,strlen($str)-strlen($start)-strpos($str,$start));
    if(!empty($end)) $str=substr($str,0,strpos($str,$end));
    return $str;
}
?>

<?php
class IndexAction extends Action {

	public function __construct(){
		
	}
	
	public function index(){
		//获得参数 signature nonce token timestamp echostr
		$nonce     = $_GET['nonce'];
		$token     = 'ojcoder';
		$timestamp = $_GET['timestamp'];
		$echostr   = $_GET['echostr'];
		$signature = $_GET['signature'];
		//形成数组，然后按字典序排序
		$array = array();
		$array = array($nonce, $timestamp, $token);
		sort($array);
		//拼接成字符串,sha1加密 ，然后与signature进行校验
		$str = sha1( implode( $array ) );
		if( $str  == $signature && $echostr ){
			//第一次接入weixin api接口的时候
			echo  $echostr;
			exit;
		}else{
			$this->reponseMsg();
		}
	}
	// 接收事件推送并回复
	public function reponseMsg(){
		//1.获取到微信推送过来post数据（xml格式）
		$postArr = $GLOBALS['HTTP_RAW_POST_DATA'];
		//2.处理消息类型，并设置回复类型和内容
		/*<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[FromUser]]></FromUserName>
<CreateTime>123456789</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[subscribe]]></Event>
</xml>*/
		$postObj = simplexml_load_string( $postArr );
		//$postObj->ToUserName = '';
		//$postObj->FromUserName = '';
		//$postObj->CreateTime = '';
		//$postObj->MsgType = '';
		//$postObj->Event = '';
		//判断该数据包是否是订阅的事件推送
		if( strtolower( $postObj->MsgType) == 'event'){
			//如果是关注 subscribe 事件
			if( strtolower($postObj->Event == 'subscribe') ){
				//回复用户消息(纯文本格式)	
				$toUser   = $postObj->FromUserName;
				$fromUser = $postObj->ToUserName;
				$time     = time();
				$msgType  =  'text';
				$content  = '欢迎关注OJCoder微信公众号，本公众号提供LeetCode、LintCode 等各大OJ平台答案查询服务，可以通过发送题目编号或标题或关键词进行答案查询；本公众号还会不定期推送各大IT/互联网公司历年笔试题目及答案解析。';
				$template = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<Content><![CDATA[%s]]></Content>
							</xml>";
				$info     = sprintf($template, $toUser, $fromUser, $time, $msgType, $content);
				echo $info;
			}
		}
		
		header("Content-type: text/html; charset=utf-8");
		define('HOST','127.0.0.1');
		define('USERNAME','root');
		define('PASSWORD','wuxubj1992');
		//连接
		$flag=true;
		if(!$con=mysqli_connect(HOST,USERNAME,PASSWORD)){
			$flag=false;
		}
		//选库
		if(!mysqli_select_db($con,'ojcoder')){
			$flag=false;     
		}
		//字符集
		if(!mysqli_query($con,'set names utf8')){
			$flag=false;
		}

/* 文本消息	
$template = "<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[%s]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>";*/	
		//文本消息回复
		if( strtolower($postObj->MsgType) == 'text'){
			$skeywords= trim($postObj->Content);
			$sql=sqlsearch($skeywords);
			$query=mysqli_query($con,$sql);
			$num=mysqli_num_rows($query);
			if($flag && $query && $num)
			{
				$toUser = $postObj->FromUserName;
				$fromUser = $postObj->ToUserName;
				$arr = array(
					array(
						'title'=>'OJCoder - OJ平台答案查询',
						'description'=>'"'.$skeywords.'"的搜索结果',
						'picUrl'=>'https://wx.ojcoder.cn/images/bg1.png',
						'url'=>'https://wx.ojcoder.cn/results.php?keywords='.$skeywords,
					),				
				);
				$template = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<ArticleCount>".count($arr)."</ArticleCount>
							<Articles>";
				foreach($arr as $k=>$v){
					$template .="<item>
								<Title><![CDATA[".$v['title']."]]></Title> 
								<Description><![CDATA[".$v['description']."]]></Description>
								<PicUrl><![CDATA[".$v['picUrl']."]]></PicUrl>
								<Url><![CDATA[".$v['url']."]]></Url>
								</item>";
				}
				
				$template .="</Articles>
							</xml> ";
				echo sprintf($template, $toUser, $fromUser, time(), 'news');
			}else{
				$template = "<xml>
						<ToUserName><![CDATA[%s]]></ToUserName>
						<FromUserName><![CDATA[%s]]></FromUserName>
						<CreateTime>%s</CreateTime>
						<MsgType><![CDATA[%s]]></MsgType>
						<Content><![CDATA[%s]]></Content>
						</xml>";
				$content = '没有关于 "'.$skeywords.'" 的搜索结果，欢迎<a href="https://www.ojcoder.cn/Contribute/">贡献代码。</a>';
				$fromUser = $postObj->ToUserName;
				$toUser   = $postObj->FromUserName; 
				$time     = time();
				$msgType  = 'text';
				echo sprintf($template, $toUser, $fromUser, $time, $msgType, $content);
			}
		}else if(strtolower($postObj->MsgType) == 'voice'){//语音消息回复
			/*<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>1357290913</CreateTime>
<MsgType><![CDATA[voice]]></MsgType>
<MediaId><![CDATA[media_id]]></MediaId>
<Format><![CDATA[Format]]></Format>
<Recognition><![CDATA[腾讯微信团队]]></Recognition>
<MsgId>1234567890123456</MsgId>
</xml>*/
			$skeywords = $postObj->Recognition;
			$skeywords=urlencode($skeywords);//将关键字编码
			$skeywords=preg_replace("/(%7E|%60|%21|%40|%23|%24|%25|%5E|%26|%27|%2A|%28|%29|%2B|%7C|%5C|%3D|\-|_|%5B|%5D|%7D|%7B|%3B|%22|%3A|%3F|%3E|%3C|%2C|\.|%2F|%A3%BF|%A1%B7|%A1%B6|%A1%A2|%A1%A3|%A3%AC|%7D|%A1%B0|%A3%BA|%A3%BB|%A1%AE|%A1%AF|%A1%B1|%A3%FC|%A3%BD|%A1%AA|%A3%A9|%A3%A8|%A1%AD|%A3%A4|%A1%A4|%A3%A1|%E3%80%82|%EF%BC%81|%EF%BC%8C|%EF%BC%9B|%EF%BC%9F|%EF%BC%9A|%E3%80%81|%E2%80%A6%E2%80%A6|%E2%80%9D|%E2%80%9C|%E2%80%98|%E2%80%99)+/",'',$skeywords);
			$skeywords=urldecode($skeywords);//将过滤后的关键字解码
			if(is_numeric(strToNum($skeywords)))
				$skeywords=strToNum($skeywords);
			$sql=sqlsearch($skeywords);
			$query=mysqli_query($con,$sql);
			$num=mysqli_num_rows($query);
			if($flag && $query && $num)
		    //if($flag)
			{
				$toUser = $postObj->FromUserName;
				$fromUser = $postObj->ToUserName;
				$arr = array(
					array(
						'title'=>'OJCoder - OJ平台答案查询',
						'description'=>'"'.$skeywords.'"的搜索结果',
						'picUrl'=>'https://wx.ojcoder.cn/images/bg1.png',
						'url'=>'https://wx.ojcoder.cn/results.php?keywords='.$skeywords,
					),				
				);
				$template = "<xml>
							<ToUserName><![CDATA[%s]]></ToUserName>
							<FromUserName><![CDATA[%s]]></FromUserName>
							<CreateTime>%s</CreateTime>
							<MsgType><![CDATA[%s]]></MsgType>
							<ArticleCount>".count($arr)."</ArticleCount>
							<Articles>";
				foreach($arr as $k=>$v){
					$template .="<item>
								<Title><![CDATA[".$v['title']."]]></Title> 
								<Description><![CDATA[".$v['description']."]]></Description>
								<PicUrl><![CDATA[".$v['picUrl']."]]></PicUrl>
								<Url><![CDATA[".$v['url']."]]></Url>
								</item>";
				}
				
				$template .="</Articles>
							</xml> ";
				echo sprintf($template, $toUser, $fromUser, time(), 'news');
			}else{
				$template = "<xml>
						<ToUserName><![CDATA[%s]]></ToUserName>
						<FromUserName><![CDATA[%s]]></FromUserName>
						<CreateTime>%s</CreateTime>
						<MsgType><![CDATA[%s]]></MsgType>
						<Content><![CDATA[%s]]></Content>
						</xml>";
				$content = '没有关于 "'.$skeywords.'" 的搜索结果。语音搜索依赖微信的语音识别功能，当语音识别不准确时，您可以尝试发送文本消息进行搜索。';
				$fromUser = $postObj->ToUserName;
				$toUser   = $postObj->FromUserName; 
				$time     = time();
				$msgType  = 'text';
				echo sprintf($template, $toUser, $fromUser, $time, $msgType, $content);
			}
		
		}
	}//reponseMsg end
	
	
}//class end
?>