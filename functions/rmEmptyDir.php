<?php 
/** 删除所有空目录 
* @param String $path 目录路径 
*/ 
function rm_empty_dir($path){ 
  if(is_dir($path) && ($handle = opendir($path))!==false){ 
    while(($file=readdir($handle))!==false){// 遍历文件夹 
      if($file!='.' && $file!='..'){ 
        $curfile = $path.$file;// 当前目录 
        if(is_dir($curfile)){// 目录 
            rmdir($curfile.'/cpp');// 删除空目录 
			rmdir($curfile.'/java');// 删除空目录 
			rmdir($curfile.'/python');// 删除空目录 
     
        } 
      } 
    } 
    closedir($handle); 
  } 
} 
$folder = './'; 
rm_empty_dir($folder); 
?> 