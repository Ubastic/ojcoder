<?php
require_once('../functions/connect.php');
function fupdate($platform,$id,$num,$slang,$con)
{
	$sql = 'UPDATE problems SET '.$slang.'='.$num.' WHERE platform="'.$platform.'" AND number='.$id;
	$query=mysqli_query($con,$sql);
	if(!$query)
	{
		die('无法更新数据: ' . mysqli_error($con));
	}
	else
		echo $sql.'</br>';
}

function getID($str)
{
	$token = strtok($str, "-");
	if ($token !== false)
	{
		return intval($token);
	}
	else
		return 0;
}

function runUpdate($splat,$dir0,$id,$con)
{
	if(is_dir($dir0))
	{
		if ($dh = opendir($dir0))
		{
			$num_cpp = 0;
			$num_java = 0;
			$num_python = 0;
			while (($file = readdir($dh)) !== false)
			{
				if($file !=='.' && $file !=='..')
				{
					if(strpos($file,'cpp',2))
						$num_cpp = $num_cpp + 1;
					if(strpos($file,'java',2))
						$num_java = $num_java + 1;
					if(strpos($file,'py',2))
						$num_python = $num_python + 1;
				}
					
			}
			//if($num_cpp !== 0)
				fupdate($splat,$id,$num_cpp,'cpp',$con);
			//if($num_java !== 0)
				fupdate($splat,$id,$num_java,'java',$con);
			//if($num_python !== 0)
				fupdate($splat,$id,$num_python,'python',$con);
			closedir($dh);
		}
	}
}
?>

<?php
	$dir0='./';
	// 打开目录，然后读取其内容
	if (is_dir($dir0)){
		if ($dh0 = opendir($dir0)){
			while (($dir1 = readdir($dh0)) !== false){
				if(is_dir($dir1) && $dir1 !=='.' && $dir1 !=='..')
				{
					$id = getID($dir1);
					runUpdate("LintCode",$dir0.$dir1,$id,$con);
				}
			}
			closedir($dh0);
		}
	}
?>
