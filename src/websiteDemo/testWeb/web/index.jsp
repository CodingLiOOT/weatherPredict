<%--
  Created by IntelliJ IDEA.
  User: zhou
  Date: 2020/7/1
  Time: 16:59
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<html>
<head lang="en">
    <meta charset="UTF-">
    <title>天气预报</title>
    <meta name="author" content="zzh" />
    <link rel="stylesheet" href="css/weather.css"/>

</head>
<body>
<header>
    <h1>气温预报</h1>
    <div id="weather_search">
        <span><input id="text" type="text" placeholder="请输入您要查询的城市" /></span>
        <span><input id="btn" type="button" value=" 查询气温" /></span>
    </div>
</header>
<section>
    <div id="today_container">
        <div>
            <img src="images/weather_icon/temp.jpg" alt="今日气温" width="60" height="60"/>
        </div>
        <div>
            <div class="main_info"><span class="info">城市</span>|<span class="info">202X-XX-XX</span>|<span class="info">星期X</span> </div>
        </div>
    </div>
    <div id="future_container">
        <div class="future_box">
            <span class="future_info">202X-XX-XX</span>
            <span class="future_info">星期X</span>
            <span class="future_info">12-16℃</span>
        </div>
        <div class="future_box">
            <span class="future_info">202X-XX-XX</span>
            <span class="future_info">星期X</span>
            <span class="future_info">12-16℃</span>
        </div>
        <div class="future_box">
            <span class="future_info">202X-XX-XX</span>
            <span class="future_info">星期X</span>
            <span class="future_info">12-16℃</span>
        </div>
        <div class="future_box">
            <span class="future_info">202X-XX-XX</span>
            <span class="future_info">星期X</span>
            <span class="future_info">12-16℃</span>
        </div>
        <div class="future_box">
            <span class="future_info">202X-XX-XX</span>
            <span class="future_info">星期X</span>
            <span class="future_info">12-16℃</span>
        </div>
        <div class="future_box">
            <span class="future_info">202X-XX-XX</span>
            <span class="future_info">星期X</span>
            <span class="future_info">12-16℃</span>
        </div>
        <div class="future_box">
            <span class="future_info">202X-XX-XX</span>
            <span class="future_info">星期X</span>
            <span class="future_info">12-16℃</span>
        </div>

    </div>
</section>
<footer>
    <div>All Rights Reserved.</div>
</footer>
<script src="js/index.js"></script>
</body>
</html>