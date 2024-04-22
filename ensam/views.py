"""
Module views.py pour gérer les vues de l'application.
"""
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from app.models import ArticleType, Article, Niveau, Filiere, EmploisTemps, Slide, Events


def ent(request):
    """
    Redirige vers l'URL de l'ENT de l'université.
    """
    print(request)
    return HttpResponseRedirect('https://ent.univh2c.ma/uPortal/f/welcome/normal/render.uP')


def mooc_universite(request):
    """
    Redirige vers l'URL du MOOC de l'université.
    """
    print(request)
    return HttpResponseRedirect('http://www.mooc.univh2c.ma/')


def biblio(request):
    """
    Redirige vers l'URL de la bibliothèque de l'université.
    """
    print(request)
    return HttpResponseRedirect('http://bums.univcasa.ma/')


def home(request):
    """
    Redirige vers la page d'accueil.
    """
    print(request)
    return redirect('/index/')


def index(request):
    """
    Affiche la page d'accueil avec les slides,
    les événements, les communiqués
     officiels et les avis aux étudiants.
    """
    slide = Slide.objects.all()
    events = Events.objects.all().order_by('date_event')
    type_com = ArticleType.objects.get(name='Communiqes Officiels')
    com_off = Article.objects.filter(article_type_id=type_com.id).order_by('-publication_date')
    type_avis = ArticleType.objects.get(name='Avis Aux Etudiants')
    aviss = Article.objects.filter(article_type_id=type_avis.id).order_by('-publication_date')
    return render(request, 'index.html',
                  {'slide': slide, 'com_off': com_off, 'avis': aviss, 'events': events})


def afficher(request, article_id):
    """
    Affiche un article spécifique en fonction de son ID.
    """
    article = Article.objects.get(id=article_id)
    return render(request, 'afficher.html', {'article': article})


def actualites(request):
    """
    Affiche les actualités, les communiqués officiels et les avis aux étudiants paginés.
    """
    type_com = ArticleType.objects.get(name='Communiqes Officiels')
    com_off = Article.objects.filter(article_type_id=type_com.id).order_by('-publication_date')
    type_avis = ArticleType.objects.get(name='Avis Aux Etudiants')
    avises = Article.objects.filter(article_type_id=type_avis.id).order_by('-publication_date')
    paginator1 = Paginator(com_off, 3)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)
    paginator2 = Paginator(avises, 3)
    page_number2 = request.GET.get('pagee')
    page_obj2 = paginator2.get_page(page_number2)
    return render(request, 'Ecole/Actualites.html',
                  {'com_off': com_off,
                   'avis': avises,
                   'page_obj1': page_obj1,
                   'page_obj2': page_obj2})


def avis(request):
    """
    Affiche les avis aux étudiants paginés.
    """
    type_avis = ArticleType.objects.get(name='Avis Aux Etudiants')
    avisss = Article.objects.filter(article_type_id=type_avis.id)
    paginator = Paginator(avisss, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Etudiant/avis_aux_etudiants.html', {'page_obj': page_obj})


def recrutement(request):
    """
    Affiche les offres de recrutement.
    """
    type_avis = ArticleType.objects.get(name='Recrutement')
    recrutements = Article.objects.filter(article_type_id=type_avis.id)
    paginator = Paginator(recrutements, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Ecole/recrutement.html',
                  {'page_obj': page_obj})


def appel_offres(request):
    """
    Affiche les appels d'offres.
    """
    type_avis = ArticleType.objects.get(name='Appels d\'offres')
    appels_offres = Article.objects.filter(article_type_id=type_avis.id)
    paginator = Paginator(appels_offres, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Ecoles/appels_offres.html',
                  {'page_obj': page_obj})


def emplois_du_temps(request):
    """
    Affiche les emplois du temps des étudiants.
    """
    niveaux = Niveau.objects.all()
    filieres = Filiere.objects.all()
    if request.method == 'POST':
        print(request.POST)
        niveau_id = request.POST.get('niveau')
        filiere_id = request.POST.get('filiere')
        emplois = get_object_or_404(EmploisTemps, niveau_id=niveau_id, filiere_id=filiere_id)
        return redirect(emplois.fichier_url)

    return render(request, 'Etudiant/emplois_du_temps.html',
                  {'filieres': filieres, 'niveaux': niveaux})


def api(request):
    """
    Affiche la page de documentation de l'API.
    """
    return render(request, 'Formation/prepa/api.html')


def ge(request):
    """
    Affiche la page de la filière génie électrique.
    """
    return render(request, 'Formation/ing/GE.html')


def gm(request):
    """
    Affiche la page de la filière génie mécanique.
    """
    return render(request, 'Formation/ing/GM.html')


def mse(request):
    """
    Affiche la page de la filière mse.
    """
    return render(request, 'Formation/ing/MSE.html')


def iagi(request):
    """
    Affiche la page de la filière iagi.
    """
    return render(request, 'Formation/ing/IAGI.html')


def cime(request):
    """
    Affiche la page du master cime.
    """
    return render(request, 'Formation/Master/CIME.html')


def gcbcm(request):
    """
    Affiche la page du master gcbcm.
    """
    return render(request, 'Formation/Master/GCBCM.html')


def mitd(request):
    """
    Affiche la page du master mitd.
    """
    return render(request, 'Formation/Master/MITD.html')


def aise(request):
    """
        Affiche la page de la licence AISE.
        """
    return render(request, 'Formation/Licence/AISE.html')


def csaa(request):
    """
        Affiche la page de la licence csaa.
        """
    return render(request, 'Formation/Licence/CSAA.html')


def di(request):
    """
        Affiche la page de la licence di.
        """
    return render(request, 'Formation/Licence/DI.html')


def dlss(request):
    """
        Affiche la page de la licence dlss.
        """
    return render(request, 'Formation/Licence/DLSS.html')


def dwm(request):
    """
            Affiche la page de la licence dwm.
            """
    return render(request, 'Formation/Licence/DWM.html')


def gc(request):
    """
        Affiche la page de la licence gc.
        """
    return render(request, 'Formation/Licence/GC.html')


def idami(request):
    """
        Affiche la page de la licence idami.
        """
    return render(request, 'Formation/Licence/IDAMI.html')


def msi(request):
    """
            Affiche la page de la licence msi.
            """
    return render(request, 'Formation/Licence/MSI.html')


def qse(request):
    """
            Affiche la page de la licence qse.
            """
    return render(request, 'Formation/Licence/QSE.html')


def tts(request):
    """
            Affiche la page de la licence tts.
            """
    return render(request, 'Formation/Licence/TTS.html')
