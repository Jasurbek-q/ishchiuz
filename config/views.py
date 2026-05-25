from django.shortcuts import render, get_object_or_404, redirect
from .models import Ishchi

def home(request):
    soha = request.GET.get('soha', '')
    ishchilar = Ishchi.objects.all().order_by('-created_at')
    if soha:
        ishchilar = ishchilar.filter(sohasi__icontains=soha)
    return render(request, 'ishchilar/list.html', {'ishchilar': ishchilar, 'soha': soha})

def detail(request, pk):
    ishchi = get_object_or_404(Ishchi, pk=pk)
    return render(request, 'ishchilar/detail.html', {'ishchi': ishchi})

def create(request):
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