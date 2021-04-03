from django import forms


class Newbookform(forms.Form):
     title=forms.CharField(label='Enter Title',max_length=50)
     price=forms.FloatField(label='Enter Price')
     author=forms.CharField(label='Enter Author')
     publisher=forms.CharField(label='Enter Publisher')

class SearchForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
