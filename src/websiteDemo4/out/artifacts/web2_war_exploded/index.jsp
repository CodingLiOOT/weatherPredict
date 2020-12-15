<%--
  Created by IntelliJ IDEA.
  User: zhou
  Date: 2020/7/1
  Time: 16:59
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>天气预报</title>
    <meta name="author" content="zzh" />
    <link rel="stylesheet" href="css/weather.css">
    <script src="js/index.js"></script>

</head>
<body>
<header>
    <h1>气温预报</h1>
    <div id="weather_search">
        <span><input id="text" type="text" placeholder="请输入您要查询的城市" /></span>
        <span><input id="btn" type="button" onclick="getCity()" value=" 查询气温" /></span>
    </div>
</header>
<section>
    <div id="today_container">
        <div>
            <img src="images/weather_icon/temp.jpg" alt="今日气温" width="60" height="60"/>
        </div>
        <div>
            <div class="main_info"><span class="info">北京</span>|<span class="info">202X-XX-XX</span>|<span class="info">星期X</span> </div>
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

    <script>
        var week=init();    //初始化函数，获取时间
        var Tmax=getTmaxData();
        var Tmin=getTminData();
    </script>

    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="chart" style="background-color: #C6C6C6;height: 300px;width:900px;"></div>
    <script src="http://echarts.baidu.com/build/dist/echarts.js"></script>
    <script type="text/javascript">

        //var week=["Day1","Day2","Day3","Day4","Day5","Day6","Day7"];

        // 路径配置
        require.config({
            paths: {
                echarts: 'http://echarts.baidu.com/build/dist'
            }
        });

        //使用
        require(
            [
                'echarts',
                'echarts/chart/bar', // 使用柱状图就加载bar模块，按需加载
                'echarts/chart/line'
            ],
            function(ec){
                // 基于准备好的dom，初始化echarts图表
                var myChart = ec.init(document.getElementById('chart'));
                // 过渡---------------------
                myChart.showLoading({
                    text: '正在努力的读取数据中...',    //loading话术
                });
                myChart.hideLoading();
                option = {
                    title : {
                        text: '未来一周气温变化',
                    },
                    tooltip : {
                        // trigger: 'axis'
                        trigger:'item'
                    },
                    legend: {
                        data:['最高气温','最低气温']
                    },
                    toolbox: {
                        show : true,
                        feature : {
                            mark : {show: false},
                            dataView : {show: true, readOnly: false}, //数据视图
                            magicType : {show: true, type: ['line', 'bar']}, //动态类型切换,柱状折现切换
                            restore : {show: true}, //重置
                            saveAsImage : {show: true} //保存为图片
                        }
                    },
                    calculable : false, //是否启用拖拽重计算特性，默认false
                    xAxis : [
                        {
                            type : 'category',
                            boundaryGap : false, // 坐标轴两端空白策略
                            //data : ["Day1","Day2","Day3","Day4","Day5","Day6","Day7"]
                            data : week
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value',
                            axisLabel : {
                                formatter: '{value} °C'
                            }
                        }
                    ],
                    series : [
                        {
                            name:'最高气温',
                            type:'line',
                            //data:[11, 11, 40, 13, 50, 13, 10],
                            data:Tmax,          //最高温数组
                            markPoint : {
                                data : [
                                    {type : 'max', name: '最大值'},
                                    {type : 'min', name: '最小值'}
                                ]
                            },
                            markLine : {
                                data : [
                                    {type : 'average', name: '平均值'}
                                ]
                            }
                        },
                        {
                            name:'最低气温',
                            type:'line',
                            //data:[1, -2, 2, -5, 8, 2, 0],
                            data:Tmin,          //最低温数组
                            markPoint : {
                                data : [
                                    {type : 'max', name: '最大值'},
                                    {type : 'min', name: '最小值'}
                                ]
                            },
                            markLine : {
                                data : [
                                    {type : 'average', name : '平均值'}
                                ]
                            }
                        }
                    ]
                };
                // 为echarts对象加载数据
                myChart.setOption(option);
            }
        );
        // }

    </script>
        </section>
    <footer>
        <div>
            Powered by Harry Zhou.
        </div>
    </footer>

</body>
</html>