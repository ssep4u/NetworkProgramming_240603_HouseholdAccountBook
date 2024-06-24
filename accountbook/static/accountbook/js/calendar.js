const monthlyDiv = document.getElementById("monthly");
const calendarTds = monthlyDiv.getElementsByTagName("td");
const calendarH1 = document.getElementsByClassName("calendar-current-month")[0];
const calendarTable = document.getElementsByClassName("calendar")[0];
const calendarTableTbody = calendarTable.getElementsByTagName("tbody")[0];
const dailyDiv = document.getElementById("daily");

let currentTime = new Date();

//calendar-current-month 제목: 2024년 5월
const setCalendarTitle = () => {
    let year = currentTime.getFullYear();
    let month = currentTime.getMonth() + 1;

    calendarH1.innerText = `${year}년 ${month}월`;
}

//이전 달/이후 달
const changeMonth = (diff) => {
    currentTime.setMonth(currentTime.getMonth() + diff);
    setCalendarTitle();
    setCalendar();
    setCalendarAccountBook();
}

// currentTime 달력 그리자
const setCalendar = () => {
    const year = currentTime.getFullYear();
    const month = currentTime.getMonth() + 1;

    //첫날의 요일 찾자
    const firstTime = new Date(year, month - 1, 1);
    const firstDay = firstTime.getDay();    //0: 일, 1: 월, ... 6: 토
    //마지막날의 날짜 찾자
    const lastTime = new Date(year, month, 0);
    const lastDate = lastTime.getDate();

    let calendarDatesString = "";
    calendarDatesString += "            <tr>\n";
    //월초 여백: 0~첫째날 요일 전까지 빈 <td>
    for (let i = 0; i < firstDay; i++) {
        calendarDatesString += "               <td></td>\n";
    }
    //날짜 채우기: 1~마지막날 날짜까지
    for (let i = 1; i <= lastDate; i++) {
        calendarDatesString += `               <td>${i}</td>\n`;
        if ((firstDay - 1 + i) % 7 == 6) {  //첫째날 전 요일 + 첫째날을 7롤 나눈 나머지가 토요일이면 </tr>
            calendarDatesString += "            </tr>\n";
        }
    }
    //월말 여백: 마지막날 다음날 요일~토요일까지 빈 <td>
    let lastDay = (firstDay - 1 + lastDate) % 7;
    for (let i = lastDay + 1; i <= 6; i++) {
        calendarDatesString += "               <td></td>\n";
    }

    calendarTableTbody.innerHTML = calendarDatesString;
}

// calendar에 가계부 있는 날짜 표시하자
const setCalendarAccountBook = () => {
    // accountbookDates 하나씩 꺼내어, currentTime의 year, currentTime의 month가 같다면, 해당 일에 add account_book class
    HTMLCollection.prototype.forEach = Array.prototype.forEach;

    accountbookDates.forEach((date) => {
        date = date.split("."); //"2024.5.26" -> ["2024", "5", "26"]
        let year = Number(date[0]);
        let month = Number(date[1]);
        let ddate = Number(date[2]);
        if (currentTime.getFullYear() === year
            && currentTime.getMonth() + 1 === month) {
            calendarTds.forEach((calendarTd) => {
                if (ddate === Number(calendarTd.innerText)) {
                    calendarTd.classList.add("has-account-book");
                }
            });
        }
    });
}

//daily 영역에 그날 가계부 표시하자
const showDailyAccountBookList = (data) => {
    dailyDiv.innerHTML = data;
}

setCalendarTitle();
setCalendar();
setCalendarAccountBook();