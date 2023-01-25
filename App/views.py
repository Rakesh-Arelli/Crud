from django.shortcuts import render
from App.models import Passinger
from App.forms import Pas


def pas(request):
    if request.method == 'POST':
        fm = Pas(request.POST)
        if fm.is_valid():
            print('persons:', fm.cleaned_data['prs'])
            print('cost:', fm.cleaned_data['cost'])
            print('total:', fm.cleaned_data['totals'])
            p_no = fm.cleaned_data['sNo']
            p_nm = fm.cleaned_data['name']
            p_em = fm.cleaned_data['mailId']
            p_pas1 = fm.cleaned_data['password']
            p_img = fm.cleaned_data['photo']

            p_dt = fm.cleaned_data['dot']

            p_per = fm.cleaned_data['persons']

            p_tc = fm.cleaned_data['cost']

            reg = Passinger(sNo=p_no, name=p_nm, mailId=p_em, password=p_pas1, photo=p_img, dot=p_dt, persons=p_per,
                            cost=p_tc)
            reg.save()


    else:
        fm = Pas()
    return render(request, 'cur.html', {'data': fm})


def base(request):
    return render(request, "base.html")


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')