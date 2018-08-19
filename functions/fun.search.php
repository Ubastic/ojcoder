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
?>