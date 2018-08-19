//自定义js
var aa=function(){
  if($(window).height()==$(document).height()){
	$(".copyright").addClass("navbar-fixed-bottom");
  }
  else{
	$(".copyright").removeClass(" navbar-fixed-bottom");
  }
}
aa();

$(function(){
 $(window).scroll(function(){
	if($(window).scrollTop()>100){
		$('a.backToTop').show();
	}
 })
$(".backToTop").goToTop();

})
	
$(function(){
	 $(window).scroll(function(){
		if($(window).scrollTop()<100){
			$('a.backToTop').hide();
		}
	 })	
})
	
function hideElement(elementID)
{
	var myele=document.getElementById(elementID);
	myele.style.display="none";
}

function showElement(elementID)
{
	var myele=document.getElementById(elementID);
	myele.style.display="block";
}
//百度自动推送
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';        
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
