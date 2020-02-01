from django.conf.urls import url
from su import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^send/$', views.send, name="send"), # Cancellation/Registration mail
	# url(r'^send2/$', views.send2, name="send2"),  # Signed up mail 1-2 days before
	url(r'^contact/$', views.contact, name='contact'),#Contact
	url(r'^about/$', views.about, name='about'),#About
	#url(r'^index/$', views.index, name='index'),#Home
	url(r'^su/login/$', views.su_login, name='su_login'), #su Login
	url(r'^su/register/$',views.su_register,name='register'),
	url(r'^su/coord-inactive/(?P<cgid>[-\w]+)/$',views.su_coord_inactive,name='coord inactive'),
	url(r'^su/coord-active/(?P<cgid>[-\w]+)/$',views.su_coord_active,name='coord active'), #register coords
	url(r'^coord/login/$',views.coord_login,name='coord_login'), #coord login
	url(r'^logout/$', views.user_logout, name='logout'),  #Common logout
	url(r'^coord/register/$', views.coord_item_register, name='item_register'),  #coord register items
	url(r'^coord/upload/(?P<gmid>[-\w]+)/$', views.coord_upload, name='upload'),#upload list and all list related updates here
	url(r'^coord/view/(?P<gmid>[-\w]+)/$',views.coord_view_item,name="view registered item"),
	url(r'^invalid_ids/(?P<gmid>[-\w]+)/$', views.coord_invalid_ids, name="invalid-ids"),
	url(r'^su/item/(?P<gmid>[-\w]+)/$', views.su_iteminfo, name='items'),  #su view all items
	url(r'^su/itemlist/$', views.su_item_list, name='item_list'),  #Smms view List and all list related updates here
	url(r'^su/item/(?P<gmid>[-\w]+)/inactive/' , views.su_item_inactive, name="Coord Item Inactive") ,
	url(r'^su/item/(?P<gmid>[-\w]+)/active/' , views.su_item_active, name="Coord Item Active") ,
	#url(r'^student/login$', views.student_login, name='student_login'),  #student login
	url(r'^student/upcoming_items/$', views.student_upcoming_items, name='student_upcoming_items'),  #view upcoming items
	url(r'^student/item/(?P<gmid>[-\w]+)/$', views.student_item_register, name='student item register'),
	url(r'^student/item/(?P<gmid>[-\w]+)/cancel/$', views.student_item_cancel, name='student item cancel'),
	url(r'^student/item/(?P<gmid>[-\w]+)/register/signup/$', views.student_item_register4, name='student item register4'),  #for wear,event
 #Cancel and register for items here
	# url(r'^coord/register-students/(?P<gmid>[-\w]+)/$',views.coord_student_register,name='coord student register'),
	#url(r'^item_info/(?P<gmid>\w+)/$', views.item_info, name='item_info'),
	#adddddddddddddddd
	url(r'^export/(?P<gmid>[-\w]+)/', views.export_data, name="export"),
	url(r'^stats/(?P<gmid>[-\w]+)/$', views.su_student_table, name="stats"),
	url(r'^import/', views.import_data, name="import"),
	url(r'^coord/edit/(?P<gmid>[-\w]+)/$', views.coord_item_edit, name='item_edit'),
	url('^su/item/(?P<gmid>[-\w]+)/sendmail/' , views.su_item_sendmail, name="Item send mail1") ,
	url('^ajax/su/item/(?P<gmid>[-\w]+)/sendmail1/' , views.su_item_sendmail1, name="Item send mail1") ,
	# url('^ajax/su/item/(?P<gmid>[-\w]+)/sendmail2/' , views.su_item_sendmail2, name="Item send mail1") ,
	url(r'^export2/',views.export,name="export2"),
	#url(r'^(?P<inv>\w+)/$',views.invalid,name="invalid"),
	#url(r'^coord/upload-spot-signing/(?P<gmid>[-\w]+)/$', views.coord_upload_spot, name='upload spot signing'),
	]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
