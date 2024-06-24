// <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
const chartTitleDiv = document.querySelector(".chart-title");
const myChartCanvas = document.getElementById("myChart");
let myChart;
let weeklyTableDiv = document.getElementById("weekly-table");

function formatNumberWithCommas(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

const updateWeeklyTable = (data) => {
    const sumTotalPrice = data.prices.reduce((accumulator, currentValue) => accumulator + currentValue, 0)
    const arrRatioTotalPrice = data.prices.map((price) => parseFloat((price / sumTotalPrice * 100).toFixed(1)));
    // console.log(arrRatioTotalPrice);

    weeklyTableDiv.innerHTML = "";      // 표 초기화
    const table = document.createElement("div");
    table.classList.add("table");
    for (let i = 0; i < data.prices.length; i++) {
        const row = document.createElement("div");
        row.classList.add("row");
        colString = "";
        colString += `<div class="col">
                        <div class="badge" style="background-color: ${data.bgcolors[i]};">${arrRatioTotalPrice[i]}%</div>
                    </div>`;
        colString += `<div class="col">${data.labels[i]}</div>`;
        numberString = formatNumberWithCommas(data.prices[i]);      // 세자리 마다 ,
        colString += `<div class="col">${numberString}원</div>`;
        row.innerHTML = colString;
        table.appendChild(row);
    }
    weeklyTableDiv.appendChild(table);
}
const initChart = () => {
    //맨 처음에 모든 데이터 가져오자
    const allURL = `/accountbook/all/`;
    fetch(allURL)
        .then((response) => response.json())
        .then((data) => updateChart(data, true))
        .catch((error) => console.error(`Error: ${error}`));

    // 차트 설정하기
    const config = {
        type: 'pie',
        options: {
            responsive: false,
            plugins: {
                legend: {
                    display: false,
                }
            }
        }
    }

    // 차트 생성
    myChart = new Chart(myChartCanvas, config);
}

const convertToYearMonthWeekNum = (dateString) => {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = date.getMonth() + 1; // JavaScript months are 0-based
    const day = date.getDate();

    // Calculate week of the month
    const firstDay = new Date(date.getFullYear(), date.getMonth(), 1).getDay(); // Day of the week of the 1st day of the month
    const weekNumber = Math.ceil((day + firstDay) / 7); // Calculate week number

    return `${year}년 ${month}월 ${weekNumber}주`;
}

const updateChart = (data, first = false) => {
    const weekly_category_total_price_list = data.weekly_category_total_price_list;
    const startDateString = data.start_date;
    const endDateString = data.end_date;
    const week_num = convertToYearMonthWeekNum(startDateString);


    if (first === true)
        chartTitleDiv.innerHTML = `모든 데이터<div>(${startDateString} ~ ${endDateString})</div>`;
    else
        chartTitleDiv.innerHTML = `${week_num}<div>(${startDateString} ~ ${endDateString})</div>`;

    // context의 데이터 가져오기
    data = {
        'labels': weekly_category_total_price_list.map((oneRow) => oneRow.category__name),
        'bgcolors': weekly_category_total_price_list.map((oneRow) => oneRow.category__bgcolor),
        'prices': weekly_category_total_price_list.map((oneRow) => oneRow.total_price)
    }
    myChart.data = {
        labels: data.labels,
        datasets: [{
            data: data.prices,
            backgroundColor: data.bgcolors
        }]
    };
    // myChart.options.plugins.title.text = [week_num, `(${startDateString} ~ ${endDateString})`];
    myChart.update();       //애니메이션
    // myChart.update('none');

    updateWeeklyTable(data);
}
initChart();