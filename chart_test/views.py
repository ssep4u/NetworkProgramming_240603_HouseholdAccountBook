import json

from django.shortcuts import render


def show_chart(request):
    # open(파일경로, 모드(r=읽기, w=쓰기, a=내용추가, b=바이너리파일, x=파일생성), 인코딩)
    with open('data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 데이터 분해하기
    name = [item['name'] for item in json_data]
    price = [item['price'] for item in json_data]
    ctgColor = [item['ctgColor'] for item in json_data]

    context = {
        'name': name,
        'price': price,
        'ctgColor': ctgColor
    }
    return render(request, 'chart_test/chart_view.html', context=context)
