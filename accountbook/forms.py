from django import forms

from accountbook.models import AccountBook


class AccountBookForm(forms.ModelForm):
    class Meta:
        model = AccountBook
        fields = ['type', 'price', 'category', 'time', 'contents']
        widgets = {
            'type': forms.RadioSelect(choices=AccountBook.TYPE_CHOICES),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '금액을 입력하세요.'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': '분류를 선택하세요.'}),
            'time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요.'}),
        }
