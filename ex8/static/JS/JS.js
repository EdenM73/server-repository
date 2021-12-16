function validate(){
  var regName = /^[a-zA-Z]+ [a-zA-Z]+$/;
  var name = document.getElementById('fn').value;
  var name = document.getElementById('ls').value;
  if(!regName.test(name)){
      alert('you need to enter your name correctlly');
      document.getElementById('name').focus();
      return false;
  }
  else{
      alert('thanks for contact me!');
      return true;
  }
}

delay=100;

timer=window.setInterval("blinkImg()",1000);


var imgId = 'fire';
var imgOnTime = 5000;
var imgOffTime = 2000;
function blink()
{
  // check for existence of objects we will use
  if (document.getElementById) {
    var ele = document.getElementById(imgId);
    if (ele && ele.style) {
      setTimeout('blinkImg()', imgOffTime);
    }
  }
}
function blinkImg()
{
  var v, t, ele = document.getElementById(imgId);
  if (ele.style.visibility == 'visible') {
    // hide it, then wait for imgOffTime
    v = 'hidden';
    t = imgOffTime;
  }
  else {
    // show it, then wait for imgOnTime
    v = 'visible';
    t = imgOnTime;
  }
  ele.style.visibility = v;
  setTimeout('blinkImg()', t);
}
