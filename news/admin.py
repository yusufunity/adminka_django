from django.contrib import admin


from .models import News




class NewsAdmin(admin.ModelAdmin):
	list_display=('id','title','create_at','update_at','is_published')
	## link berish oynasi
	list_display_links=('id','title')
	##qidirish oynasi
	search_fields=('title','content')


admin.site.register(News,NewsAdmin)