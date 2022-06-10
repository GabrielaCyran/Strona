from django.urls import URLPattern, path
from .import views 

urlpatterns= [
path('rejestracja',views.rejestracja,name="rejestracja"),
path('', views.index, name="index"),
path ('logowanie/',views.logowanie,name="logowanie"),
path('index/',views.index,name="index"),
path('baza/', views.baza,name="baza"),
path('wylogowanie/',views.wylogowanie, name="wylogowanie"),
path('forum/',views.Forum.as_view(), name="forum"),
path('koło/',views.kolo, name="koło"),
path('gruba/',views.gruba, name="gruba"),
path('drobna/',views.drobna, name="drobna"),
path('galeria/',views.galeria, name="galeria"),
path('profil/<email>/', views.profil, name='profil'),
path('post-szczegoly/<int:pk>',views.PostSzczegoly.as_view(), name="post-szczegoly"),
path('dodaj-post/', views.DodajPostView.as_view(), name="dodaj-post"),
path('post/<int:pk>/dodaj-komentarz/', views.DodajKomentarzView.as_view(), name='dodaj-komentarz')
]
