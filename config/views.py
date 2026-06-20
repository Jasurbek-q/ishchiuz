from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import check_password
from .forms import FoydalanuvchiForm, LoginForm
from .models import Ishchi, Foydalanuvchi


# ==========================================
# ISHCHILAR (o'zgarmadi)
# ==========================================

def home(request):
    # Kirmagan bo'lsa login sahifasiga
    if not request.session.get('foydalanuvchi_id'):
        return redirect('kirish')

    soha = request.GET.get('soha', '')
    ishchilar = Ishchi.objects.all().order_by('-created_at')
    if soha:
        ishchilar = ishchilar.filter(sohasi__icontains=soha)
    return render(request, 'ishchilar/list.html', {'ishchilar': ishchilar, 'soha': soha})


def detail(request, pk):
    if not request.session.get('foydalanuvchi_id'):
        return redirect('kirish')

    ishchi = get_object_or_404(Ishchi, pk=pk)
    return render(request, 'ishchilar/detail.html', {'ishchi': ishchi})


def create(request):
    if not request.session.get('foydalanuvchi_id'):
        return redirect('kirish')

    if request.method == 'POST':
        Ishchi.objects.create(
            name        = request.POST.get('name'),
            surname     = request.POST.get('surname'),
            age         = request.POST.get('age'),
            sohasi      = request.POST.get('sohasi'),
            description = request.POST.get('description'),
            rasm        = request.FILES.get('rasm'),
        )
        return redirect('home')
    return render(request, 'ishchilar/create.html')


# ==========================================
# FOYDALANUVCHILAR — RO'YXATDAN O'TISH / KIRISH
# ==========================================




def kirish(request):
    if request.session.get('foydalanuvchi_id'):
        return redirect('home')

    xato = None

    if request.method == 'POST':
        forma = LoginForm(request.POST)
        if forma.is_valid():
            email     = forma.cleaned_data['email']
            password  = forma.cleaned_data['password']
            eslab_qol = forma.cleaned_data.get('eslab_qol')

            try:
                foydalanuvchi = Foydalanuvchi.objects.get(email=email)

                if check_password(password, foydalanuvchi.password):
                    request.session['foydalanuvchi_id']  = foydalanuvchi.id
                    request.session['foydalanuvchi_ism'] = foydalanuvchi.name

                    if eslab_qol:
                        request.session.set_expiry(60 * 60 * 24 * 30)  # 30 kun
                    else:
                        request.session.set_expiry(0)  # brauzer yopilsa tugaydi

                    return redirect('home')
                else:
                    xato = "Parol noto'g'ri!"

            except Foydalanuvchi.DoesNotExist:
                xato = "Bu email ro'yxatdan o'tmagan!"
    else:
        forma = LoginForm()

    return render(request, 'ishchilar/kirish.html', {'forma': forma, 'xato': xato})


def chiqish(request):
    request.session.flush()
    return redirect('kirish')


def foydalanuvchi_list(request):
    if not request.session.get('foydalanuvchi_id'):
        return redirect('kirish')
    foydalanuvchilar = Foydalanuvchi.objects.all().order_by('-id')
    return render(request, 'foydalanuvchilar_list.html', {'foydalanuvchilar': foydalanuvchilar})


def foydalanuvchi_create(request):
    if request.method == 'POST':
        form = FoydalanuvchiForm(request.POST)
        if form.is_valid():
            foydalanuvchi = form.save(commit=False)
            foydalanuvchi.set_password(form.cleaned_data['password'])
            foydalanuvchi.save()

            # Yaratgandan keyin darhol session ochish
            request.session['foydalanuvchi_id']  = foydalanuvchi.id
            request.session['foydalanuvchi_ism'] = foydalanuvchi.name
            request.session.set_expiry(60 * 60 * 24 * 30)

            return redirect('home')
    else:
        form = FoydalanuvchiForm()
    return render(request, 'ishchilar/forms.html', {'form': form})


def foydalanuvchi_detail(request, pk):
    if not request.session.get('foydalanuvchi_id'):
        return redirect('kirish')

    foydalanuvchi = get_object_or_404(Foydalanuvchi, pk=pk)
    return render(request, 'ishchilar/foydalanuvchi_detail.html', {'foydalanuvchi': foydalanuvchi})