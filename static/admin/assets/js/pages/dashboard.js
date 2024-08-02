

var colors = ["#3073F1", "#0acf97"];
var dataColors = document.querySelector("#crm-project-statistics").dataset.colors;

if (dataColors) {
    colors = dataColors.split(",");
}

var options = {
    chart: {
        height: 350,
        type: 'bar',
        toolbar: {
            show: false
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            endingShape: 'rounded',
            columnWidth: '25%',
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 1,
        colors: ['transparent']
    },
    colors: colors,
    series: [{
        name: 'پروژه ها',
        data: [56, 38, 85, 72, 28, 69, 55, 52, 69]
    }, {
        name: 'ساعات کاری',
        data: [176, 185, 256, 240, 187, 205, 191, 114, 194]
    }],
    xaxis: {
        categories: ['اسفند', 'بهمن', 'دی', 'آذر', 'آبان', 'مهر', 'شهریور', 'مرداد', 'تیر'],
    },
    legend: {
        offsetY: 0,
        fontFamily: "IRANSansX"
    },
    fill: {
        opacity: 1

    },
    grid: {
        row: {
            colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
            opacity: 0.2
        },
        borderColor: '#9ca3af20',
        padding: {
            bottom: 5,
        }
    }
}

var chart = new ApexCharts(
    document.querySelector("#crm-project-statistics"),
    options
);

chart.render();



//
var colors = ["#3073F1", "#0acf97"];
var dataColors = document.querySelector("#monthly-target").dataset.colors;

if (dataColors) {
    colors = dataColors.split(",");
}

var options = {
    chart: {
        type: 'donut',
        height: 270,
        offsetY: -10
    },
    legend: {
        show: false
    },
    stroke: {
        colors: ['transparent']
    },
    series: [82, 37],
    labels: ["اتمام یافته", " معلق"],
    colors: colors,
    responsive: [{
        breakpoint: 480,
        options: {
            chart: {
                width: 300
            },
            legend: {
                position: 'bottom'
            }
        }
    }]
}

var chart = new ApexCharts(
    document.querySelector("#monthly-target"),
    options
);

chart.render();


//
var colors = ["#3073F1", "#0acf97", "#fa5c7c", "#ffbc00"];
var dataColors = document.querySelector("#project-overview-chart").dataset.colors;
if (dataColors) {
    colors = dataColors.split(",");
}
var options = {
    chart: {
        height: 350,
        type: 'radialBar'
    },
    colors: colors,
    series: [85, 70, 80, 65],
    labels: ['طراح محصول', 'توسعه دهنده وب', 'طراح آیکون', 'طراح'],
    plotOptions: {
        radialBar: {
            track: {
                margin: 5,
            }
        }
    }
}

var chart = new ApexCharts(
    document.querySelector("#project-overview-chart"),
    options
);

chart.render();