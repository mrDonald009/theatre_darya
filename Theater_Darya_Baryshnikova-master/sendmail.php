<?php
  <?php
  use PHPMailer\PHPMailer\PHPMailer;
  use PHPMailer\PHPMailer\Exception;
  
  require 'path/to/PHPMailer/src/Exception.php';
  require 'path/to/PHPMailer/src/PHPMailer.php';
  require 'path/to/PHPMailer/src/SMTP.php';

  $mail = new PHPMailer(true);
  $mail ->CharSet = 'UTF-8';
  $mail ->setLanguage('ru','phpmailer/language/');
  $mail ->IsHTML(true);
  
  //от кого письмо
  $mail->setFrom('vishnyajudo@gmail.com', 'Театр Новочебоксарск');
  //кому отправить 
  $mail->addAddres('vishnyajudo@gmail.com', 'Театр Новочебоксарск');
  //тема письма
  $mail->Subject = 'Зажигаем детские сердца';

  //тело письма
  $body = '<h1>Встречай супер письмо! Удачного дня, Дарья!</h1>';

  if(trim(!empty($_POST['name']))){
    $body.='<p><strong>Имя:</strong> '.$_POST['name'].'</p>';
  }
  if(trim(!empty($_POST['email']))){
    $body.='<p><strong>Email:</strong> '.$_POST['email'].'</p>';
  }
  if(trim(!empty($_POST['message']))){
    $body.='<p><strong>Cообщение:</strong> '.$_POST['message'].'</p>';
  }
