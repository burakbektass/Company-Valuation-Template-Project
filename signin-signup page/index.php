<?php
include 'db_connection.php';

session_start();

error_reporting(0);

if(isset($_SESSION["user_id"])){
  header('Location: index.php');
}

if(isset($_POST["signup"])){
  $fullname = mysqli_real_escape_string($conn,$_POST["full_name_signup"]);
  $email = mysqli_real_escape_string($conn,$_POST["email_signup"]);
  $password = mysqli_real_escape_string($conn,md5($_POST["password_signup"]));
  $cpassword = mysqli_real_escape_string($conn,md5($_POST["cpassword_signup"]));
  $check_email= mysqli_num_rows(mysqli_query($conn,"SELECT email FROM users Where email='$email'"));

  if($password !== $cpassword){
    echo "<script>alert('Password not match !'); </script>";
  }elseif ($check_email > 0) {
    echo "<script>alert('Email already in use !'); </script>";
  }else{
    $sql="INSERT INTO users (full_name,email,password) VALUES ('$fullname','$email','$password')";
    $result= mysqli_query($conn,$sql);
    if($result){
      $_POST["full_name_signup"] = "";
      $_POST["email_signup"] = "";
      $_POST["password_signup"] = "";
      $_POST["cpassword_signup"] = "";
  
      echo "<script>alert('Registration is successful.'); </script>";
    }else{
      echo "<script>alert('Registration is not successful.');</script>')"; 
    }
    header("Location:http://localhost:8501/");

  }
}
if(isset($_POST["signin"])){
  
  $email = mysqli_real_escape_string($conn,$_POST["email"]);
  $password = mysqli_real_escape_string($conn,md5($_POST["password"]));
  
  $check_email= mysqli_query($conn,"SELECT id FROM users Where email='$email' AND password='$password'");

  if(mysqli_num_rows($check_email) > 0){
    $row = mysqli_fetch_assoc($check_email);
    $_SESSION["user_id"] = $row['id'];
    header("Location:http://localhost:8501/");

  }else{
    echo "<script>alert('Login failed. Please try again!!'); </script>";
  }
  


}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script
      src="https://kit.fontawesome.com/64d58efce2.js"
      crossorigin="anonymous"
    ></script>
    <link rel="stylesheet" href="style.css" />
    <title>Sign in & Sign up Form</title>
  </head>
  <body>
    <div class="container">
      <div class="forms-container">
        <div class="signin-signup">
          <form action="" class="sign-in-form" method="POST">    <!-- SIGN IN FORM--> 
            <h2 class="title">Sign in</h2>
            <div class="input-field">
              <i class="fas fa-user"></i>
              <input type="text" placeholder="Email" name="email" value="<?php echo $_POST["email"]; ?>" required />
            </div>
            <div class="input-field">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Password" name="password" value="<?php echo $_POST["password"]; ?>" required />
            </div>
            <input type="submit" value="Login" name="signin" class="btn solid" />
          </form>
          <form action="" class="sign-up-form" method="post" >  <!-- SIGN UP FORM-->     
            <h2 class="title">Sign up</h2>
            <div class="input-field">
              <i class="fas fa-user"></i>
              <input type="text" placeholder="Full Name" name="full_name_signup" value="<?php echo $_POST["full_name_signup"]; ?>" required/>
            </div>
            <div class="input-field">
              <i class="fas fa-envelope"></i>
              <input type="email" placeholder="Email" name="email_signup" value="<?php echo $_POST["email_signup"]; ?>" required/>
            </div>
            <div class="input-field">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Password" name = "password_signup" value="<?php echo $_POST["password_signup"]; ?>" required/>
            </div>
            <div class="input-field">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Confirm Password" name = "cpassword_signup" value="<?php echo $_POST["cpassword_signup"]; ?>" required/>
            </div>
            <input type="submit" class="btn" name="signup" value="Sign up" />
          </form>
        </div>
      </div>

      <div class="panels-container">
        <div class="panel left-panel">
          <div class="content">
            <h3>Do not have account ?</h3>
            <p>
                Quickly register and start to use.
            </p>
            <button class="btn transparent" id="sign-up-btn">
              Sign up
            </button>
          </div>
          <img src="img/signin-icon.png" class="image" alt="" />
        </div>
        <div class="panel right-panel">
          <div class="content">
            <h3>Already have account ?</h3>
            <p>
                Login and start to use.
            </p>
            <button class="btn transparent" id="sign-in-btn">
              Sign in
            </button>
          </div>
          <img src="img/signup-icon.svg" class="image" alt="" />
        </div>
      </div>
    </div>

    <script src="app.js"></script>
  </body>
</html>
