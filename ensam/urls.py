"""
Module urls.py pour la gestion des URLs de l'application.
"""
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .views import mooc_universite, ent, biblio,\
    index, actualites, avis, emplois_du_temps, recrutement, appel_offres, \
    afficher, home, api, ge, gm, iagi, mse, cime,\
    gcbcm, mitd, aise, csaa, tts, qse, msi, idami, gc, dwm, dlss, di

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('en/etudiant/ent/', ent, name='external_redirect'),
    path('en/ent/', ent, name='external_redirect'),
    path('en/e-learning/mooc-universite-hassan-2/', mooc_universite, name='mooc_universite'),
    path('en/bibliotheque/', biblio, name='biblio'),
    path('en/index/', index, name='index'),
    path('fr/index/', index, name='index'),
    path('en/ensam/actualites/', actualites, name='actualites'),
    path('fr/ensam/actualites/', actualites, name='actualites'),
    path('en/etudiant/avis-aux-etudiants/', avis, name='avis'),
    path('en/etudiant/recrutement/', recrutement, name='recrutement'),
    path('en/etudiant/appels-doffres/', appel_offres, name='appel_offres'),
    path('en/etudiant/emploi-du-temps/', emplois_du_temps, name='emplois_du_temps'),
    path('en/afficher/<int:article_id>/', afficher, name='afficher'),
    path('en/', home, name='home'),
    path('en/formation/prepa/', api, name='api'),
    path('en/formation/ing/ge/', ge, name='ge'),
    path('en/formation/ing/gm/', gm, name='gm'),
    path('en/formation/ing/iagi/', iagi, name='iagi'),
    path('en/formation/ing/mse/', mse, name='mse'),
    path('en/formation/master/cime/', cime, name='cime'),
    path('en/formation/master/gcbcm/', gcbcm, name='gcbcm'),
    path('en/formation/master/mitd/', mitd, name='mitd'),
    path('en/formation/licence/aise/', aise, name='aise'),
    path('en/formation/licence/csaa/', csaa, name='csaa'),
    path('en/formation/licence/di/', di, name='di'),
    path('en/formation/licence/dlss/', dlss, name='dlss'),
    path('en/formation/licence/dwm/', dwm, name='dwm'),
    path('en/formation/licence/gc/', gc, name='gc'),
    path('en/formation/licence/idami/', idami, name='idami'),
    path('en/formation/licence/msi/', msi, name='msi'),
    path('en/formation/licence/qse/', qse, name='qse'),
    path('en/formation/licence/tts/', tts, name='tts'),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

# This is only needed when using runserver.
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
