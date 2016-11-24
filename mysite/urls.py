# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include, url
from django.contrib import admin

from game.views import index
from rank.views import rankList, ranks

from rest_framework import routers
from quickstart import views
from rank import views

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'api/rank', ensure_csrf_cookie(views.RankViewSet))
router.register(r'rank', views.RankViewSet)

#from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
#class RankSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Rank
#        fields = ('usernam', 'email', 'first_name', 'last_name')


# ViewSets define the view behavior.
#class RankViewSet(viewsets.ModelViewSet):
#    queryset = Rank.objects.all()
#    serializer_class = RankSerializer

#router = routers.DefaultRouter()
#router.register(r'rank', RankViewSet)

urlpatterns = [
    #url(r'^$', index),
    url(r'^rank/', rankList),
    url(r'^ranks/', ranks),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
