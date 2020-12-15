var Tmax=[];
var Tmin=[];
var week;
var myChart;

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
    var j=0;    //临时计数标记
    week=new Array(7);
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


    for(var i=0;i<7;i++){
        Tmax[i]=weather[i].tmax;
        Tmin[i]=weather[i].tmin;
    }


    //Tmax=[32, 30, 31, 25, 30, 31, 33];
    //Tmin=[23, 22, 22, 22, 21, 23, 22];

    var future_info=document.getElementsByClassName("future_info");
    var j=2;    //临时计数标记
    for(var i = 0 ; i < 7 ; i++) {
        future_info[j].innerHTML=Tmin[i]+"-"+Tmax[i]+"℃";
        j+=3;
    }
}

function drawChart() {
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
            myChart = ec.init(document.getElementById('chart'));
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
}

function getCity() {
    var string;
    string=document.getElementById("text").value;

    if (isNumber(string)||issign(string)||string=="") {
        alert('请输入有效城市名');
    }else {
        var info = document.getElementsByClassName('info');
        info[0].innerHTML=string;


        //Tmax=[2,2,2,3,2,2,2];
        //Tmin=[1,1,1,1,1,1,1];

        var future_info=document.getElementsByClassName("future_info");
        var j=2;    //临时计数标记
        for(var i = 0 ; i < 7 ; i++) {
            future_info[j].innerHTML=Tmin[i]+"-"+Tmax[i]+"℃";
            j+=3;
        }
        myChart.setOption({
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
        })
    }
}