function register(){

var name = document.getElementById("userId").value;
var password = document.getElementById("userPassword").value;
var password_again=document.getElementById("userPassword-again").value;
if(password != password_again){
    alert("两次密码输入不一致");
    document.getElementById("userPassword").value="";
    document.getElementById("userPassword-again").value="";
}else{

    //alert("register success");
    var xmlhttp = new XMLHttpRequest();
    //alert("creat xmlrequest")
        xmlhttp.open("get","register?name="+name+"&pw="+password,true);
        xmlhttp.onreadystatechange=function(){

            if(xmlhttp.readyState==4&&xmlhttp.status==200){
                //alert("statuc changed success");
                var txt =xmlhttp.responseText;
                alert("注册成功！你的ID是："+txt);
                window.location="/login/";
                //跳转到登陆页面
            }


        }

        xmlhttp.send(null);
        //alert("send success");
}

}