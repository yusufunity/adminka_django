from django.db import models


class News(models.Model):
	
	title=models.CharField(max_length=150,verbose_name='Nomi')
	content=models.TextField(blank=True,verbose_name='Kontent')
	create_at=models.DateTimeField(auto_now_add=True,verbose_name='Tuzilgan vaqti')
	update_at=models.DateTimeField(auto_now=True,verbose_name='Ozgargan vaqti')
	photo=models.ImageField(upload_to='img/%Y/%m/%d/',verbose_name='rasm',blank=True)
	is_published=models.BooleanField(default=True,verbose_name='Publikabad')

	def __str__(self):
		return self.title
	## --Meta tegi va verbose_name= ozgartirish
	class Meta:
		verbose_name='Yanglik'
		## koplikda nom berish
		verbose_name_plural='Yangiliklar'
		## ordering- filter
		ordering=['-create_at']
