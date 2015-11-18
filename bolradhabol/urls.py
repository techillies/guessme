from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'guessme.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'words.views.guessme', name="guessme"),
                       url(r'^getnextword/$', 'words.views.getnextword', name="getnextword"),
                       url(r'^addwords/$', 'words.views.add_words', name="add_words"),

                       )