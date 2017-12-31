$.fn.echarts_graph = function( indata ) {

    var _this = $(this);
    // // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echart'));

    //var myChart = indata.myChart;
    var rawdata = indata.rawdata;

    var hours = ['2007', '2008', '2009', '2010', '2011', '2012', '2013',
        '2014', '2015', '2016', '2017'];
    var days = ['Rong Jin', 'Heng Huang', 'Xiaoou Tang', 'Dacheng Tao', 
        'Jiawei Han 0001', 'Qiang Yang 0001', 'Jieping Ye', 'Zhi-Hua Zhou', 'Feiping Nie', 'Shuicheng Yan'];

    var data = [[0, 0, 6], [0, 1, 8], [0, 2, 8], [0, 3, 6], [0, 4, 6], 
        [0, 5, 7], [0, 6, 7], [0, 7, 5], [0, 8, 6], [0, 9, 3], [0, 10, 4], [1, 0, 0], [1, 1, 3], [1, 2, 1], [1, 3, 3], [1, 4, 11], [1, 5, 6], [1, 6, 11], [1, 7, 6], [1, 8, 8], [1, 9, 10], [1, 10, 13], [2, 0, 13], [2, 1, 7], [2, 2, 3], [2, 3, 4], [2, 4, 6], [2, 5, 4], [2, 6, 4], [2, 7, 7], [2, 8, 11], [2, 9, 10], [2, 10, 4], [3, 0, 0], [3, 1, 1], [3, 2, 2], [3, 3, 2], [3, 4, 1], [3, 5, 3], [3, 6, 7], [3, 7, 7], [3, 8, 11], [3, 9, 18], [3, 10, 24], [4, 0, 4], [4, 1, 5], [4, 2, 6], [4, 3, 4], [4, 4, 11], [4, 5, 7], [4, 6, 8], [4, 7, 4], [4, 8, 12], [4, 9, 10], [4, 10, 6], [5, 0, 10], [5, 1, 14], [5, 2, 7], [5, 3, 5], [5, 4, 11], [5, 5, 5], [5, 6, 5], [5, 7, 4], [5, 8, 6], [5, 9, 8], [5, 10, 7], [6, 0, 6], [6, 1, 7], [6, 2, 12], [6, 3, 5], [6, 4, 9], [6, 5, 11], [6, 6, 7], [6, 7, 6], [6, 8, 9], [6, 9, 9], [6, 10, 4], [7, 0, 3], [7, 1, 4], [7, 2, 6], [7, 3, 7], [7, 4, 6], [7, 5, 5], [7, 6, 6], [7, 7, 9], [7, 8, 8], [7, 9, 14], [7, 10, 17], [8, 0, 2], [8, 1, 1], [8, 2, 1], [8, 3, 2], [8, 4, 9], [8, 5, 4], [8, 6, 11], [8, 7, 7], [8, 8, 8], [8, 9, 14], [8, 10, 30], [9, 0, 3], [9, 1, 7], [9, 2, 9], [9, 3, 11], [9, 4, 6], [9, 5, 9], [9, 6, 10], [9, 7, 13], [9, 8, 8], [9, 9, 8], [9, 10, 17]];

    option = {
       tooltip: {
            position: 'top'
        },
        title: [],
        singleAxis: [],
        series: []
    };

    echarts.util.each(days, function (day, idx) {
       option.title.push({
            textBaseline: 'middle',
            top: (idx + 0.5) * 10 + '%',
            text: day
        });
        option.singleAxis.push({
            left: 150,
            type: 'category',
            boundaryGap: false,
            data: hours,
            top: (idx * 10 + 5) + '%',
            height: (10 - 10) + '%',
            axisLabel: {
                interval: 2
            }
        });
        option.series.push({
            singleAxisIndex: idx,
            coordinateSystem: 'singleAxis',
            type: 'scatter',
            data: [],
            symbolSize: function (dataItem) {
                console.log(idx);
                console.log(dataItem);
                return dataItem[1] * 3;
            }
        });
    });

    echarts.util.each(data, function (dataItem) {
        option.series[dataItem[0]].data.push([dataItem[1], dataItem[2]]);
    });

    myChart.setOption(option);

    return this;
};