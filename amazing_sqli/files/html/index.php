<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Log In / Sign Up</title>
<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/css/bootstrap.min.css'>
<link rel='stylesheet' href='https://unicons.iconscout.com/release/v2.1.9/css/unicons.css'>
<link rel="stylesheet" href="./style.css">
</head>
<body>
<div class="section">
  <div class="container">
    <div class="row full-height justify-content-center">
      <div class="col-12 text-center align-self-center py-5">
        <div class="section pb-5 pt-5 pt-sm-2 text-center">
          <h6 class="mb-0 pb-3"><span>Log In </span><span>Sign Up</span></h6>
          <input class="checkbox" type="checkbox" id="reg-log" name="reg-log" />
          <label for="reg-log"></label>
          <div class="card-3d-wrap mx-auto">
            <div class="card-3d-wrapper">
              <div class="card-front">
                <div class="center-wrap">
                  <div class="section text-center">
                    <h4 class="mb-4 pb-3">Log In</h4>
                    <div class="form-group">
                      <input type="email" name="logemail" class="form-style" placeholder="Your Email" id="logemail" autocomplete="off">
                      <i class="input-icon uil uil-at"></i></div>
                    <div class="form-group mt-2">
                      <input type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass" autocomplete="off">
                      <i class="input-icon uil uil-lock-alt"></i></div>
                    <a href="#" class="btn mt-4" onClick="location='board.html'">submit</a>
                    <p class="mb-0 mt-4 text-center"><a href="#0" class="link">Forgot your password?</a></p>
                  </div>
                </div>
              </div>
              <div class="card-back">
                <div class="center-wrap">
                  <div class="section text-center">
                    <h4 class="mb-4 pb-3">Sign Up</h4>
                    <div class="form-group">
                      <input type="text" name="logname" class="form-style" placeholder="Your Full Name" id="logname" autocomplete="off">
                      <i class="input-icon uil uil-user"></i></div>
                    <div class="form-group mt-2">
                      <input type="email" name="logemail" class="form-style" placeholder="Your Email" id="logemail" autocomplete="off">
                      <i class="input-icon uil uil-at"></i></div>
                    <div class="form-group mt-2">
                      <input type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass" autocomplete="off">
                      <i class="input-icon uil uil-lock-alt"></i></div>
                    <a href="#" class="btn mt-4" onClick="location='board.html'">submit</a></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- partial -->
<script src="./script.js"></script>
<pre>
<?php 

$conn = mysqli_connect('127.0.0.1','root','root','cometosql') or die('数据库连接失败');

$conn->set_charset('utf8');

$name = $_POST['logname'];

$email = $_POST['logemail'];

$pass = $_POST['logpass'];


if(!empty($name)){

	$sql = "INSERT INTO users(user,pass,email)

	VALUES ('{$name}' ,'{$pass}','{$email}')";

	mysqli_query($conn,$sql) or die(mysqli_error($conn));

	echo("注册成功！");
}

else{
	$sql="SELECT * FROM users where email='{$email}' and pass='{$pass}'";

	$result=$conn->query($sql);

	$row = mysqli_num_rows($result);
}

if($row == 1){

echo $row['user']."登陆成功!";
}

else{
echo"登录失败，请重新登录！";

}?>
</pre>
</body>
</html>
