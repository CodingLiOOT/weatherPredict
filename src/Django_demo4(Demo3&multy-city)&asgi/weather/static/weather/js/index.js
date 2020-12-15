var Tmax=[];
var Tmin=[];

function isNumber(value) {         //验证是否为数字
    var patrn = /^(-)?\d+(\.\d+)?$/;
    if (patrn.exec(value) == null || value == "") {
        return false
    } else {
        return true
    }
}

function issign(value){
    value = value.replace(/\s+/g, ""); //关键是这一句，把value中的空格全replace成空字符串
    if(value.length <= 0) {
        return true;
    }
    var regEn = /[`!@#$%^&*()_+<>?:"{},.\/;'[\]]/im,
        regCn = /[·！#￥（——）：；“”‘、，|《。》？、【】[\]]/im;
    if(regEn.test(value) || regCn.test(value)) {
        return true;
    }


    return false;
}

function getCity() {
    var string;
    string=document.getElementById("text").value;

    if (isNumber(string)||issign(string)||string=="") {
        alert('请输入有效城市名');
    }else {
        var info = document.getElementsByClassName('info');
        info[0].innerHTML=string;
    }
}

function init() {
    var info = document.getElementsByClassName('info');
    var date=new Date();
    var year=date.getFullYear();
    var month=date.getMonth()+1;
    var day=date.getDate();
    info[1].innerHTML=year+"-"+month+"-"+day;
    var weekday;
    switch (date.getDay()) {
        case 0:
            weekday="星期日";
            break;
        case 1:
            weekday="星期一";
            break;
        case 2:
            weekday="星期二";
            break;
        case 3:
            weekday="星期三";
            break;
        case 4:
            weekday="星期四";
            break;
        case 5:
            weekday="星期五";
            break;
        case 6:
            weekday="星期六";
            break;
    }
    info[2].innerHTML=weekday;

    var future_info=document.getElementsByClassName("future_info");
    var now = new Date();
    var nowTime = now.getTime() ;
    var oneDayTime = 24*60*60*1000 ;
    var j=0;    //临时标记
    var week=new Array(7);
    for(var i = 0 ; i < 7 ; i++) {
        //显示周一
        var ShowTime = nowTime + (i + 1) * oneDayTime;
        //初始化日期时间
        var myDate = new Date(ShowTime);
        var year = myDate.getFullYear();
        var month = myDate.getMonth() + 1;
        var date = myDate.getDate();
        future_info[j].innerHTML=year + "-" + month + "-" + date;
        future_info[++j].innerHTML="星期" + "日一二三四五六".charAt(myDate.getDay());
        week[i]='星期' + '日一二三四五六'.charAt(myDate.getDay());
        j+=2;
    }
    return week;
}

function getTmaxData() {
    Tmax=[31, 32, 30, 33, 34, 36, 32];
    return Tmax;
}

function getTminData() {
    Tmin=[25, 28, 22, 28, 26, 27, 23];
    var future_info=document.getElementsByClassName("future_info");
    var j=2;    //临时标记
    for(var i = 0 ; i < 7 ; i++) {
        future_info[j].innerHTML=Tmin[i]+"-"+Tmax[i]+"℃";
        j+=3;
    }
    return Tmin;
}