from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms_post import views
from django.contrib.auth.views import logout
from django.contrib.auth.views import login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio, name="Página inicio"),
    url(r'^logout', logout),
    url(r'^login', login),
    url(r'^edit/(.+)', views.pagina, name="Editar página"), # Ver abajo
    url(r'^edit', views.error_edit, name="/edit/ sin nada más"),
    url(r'^accounts/profile/', views.login_exito, name="Login hecho"),
    url(r'(.+)', views.pagina, name="Página"),
)

# Ya implementé la edición (para la práctica 15.8) dentro
# de la función página (views.pagina)
#
# Lo reutilizo para la edición desde /edit/<name>
