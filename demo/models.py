from django.db import models

class BookNumber(models.Model):
	isbn_10 = models.CharField(max_length=10, blank=True)
	isbn_13 = models.CharField(max_length=13, blank=True)

class Book(models.Model):
	# BOOKS = (
	# 	('HB', 'Hobbit'),
	# 	('LOTR', 'Lord of the ring')
	# )
	# title = models.CharField(blank = False,
	# 						 null=True,
	# 						 unique=True,
	# 						 default='',
	# 						 choices=BOOKS)
	title = models.CharField(max_length=36, blank = False, unique=True)
	description = models.TextField(max_length=256, blank=True)
	## DecimalField -> decimal object in python
	## FloatField -> float object in DB
	price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
	published = models.DateField(blank=True, null=True, default=None)
	is_published = models.BooleanField(default=False)
	cover = models.ImageField(upload_to='covers/', blank=True)

	number = models.OneToOneField(BookNumber,
								  null=True,
								  blank=True,
								  on_delete=models.CASCADE)

	def __str__(self):
		return self.title




