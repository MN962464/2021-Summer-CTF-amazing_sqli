<html>
<head>
<title>come to find tips</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" href="css/style.css" type="text/css" media="all">
</head>
<body>
<div class="banner">
  <div class="agileinfo-dot">
    <h1>一句话形容MMT</h1>
    <div class="w3layoutscontaineragileits">
      <h2>请留言</h2>
      <form method="get">
        <input type="text" name="inject">
        <div class="aitssendbuttonw3ls">
          <input type="submit" value="提交">
        </div>
      </form>
    </div>
  </div>
</div>
<pre>
<?php
function waf1($inject) {
    preg_match("/select|update|delete|drop|insert|where|\./i",$inject) && die('察觉到你尝试攻击,请停止sql注入');
}

function waf2($inject) {
    strstr($inject, "set") && strstr($inject, "prepare") && die('察觉到你尝试攻击,请停止sql注入');
}

if(isset($_GET['inject'])) {
    $id = $_GET['inject'];
    waf1($id);
    waf2($id);
    $mysqli = new mysqli("127.0.0.1","root","root","cometosql");
    //多条sql语句
    $sql = "select * from `come_on` where id = '$id';";

    $res = $mysqli->multi_query($sql);

    if ($res){//使用multi_query()执行一条或多条sql语句
      do{
        if ($rs = $mysqli->store_result()){
          while ($row = $rs->fetch_row()){
            var_dump($row);
            echo "<br>";
          }
          $rs->Close(); 
          if ($mysqli->more_results()){ 
            echo "<hr>";
          }
        }
      }while($mysqli->next_result()); 
    } else {
      echo "error ".$mysqli->errno." : ".$mysqli->error;
    }
    $mysqli->close(); 
}


?>
</pre>

</body>

</html>
