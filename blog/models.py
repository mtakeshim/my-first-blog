from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	# ユーザー名
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	# 下はブログ用
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	# 申込日
	created_date = models.DateTimeField(default=timezone.now)

	IM_choices = [
		('EI', 'EI'),
		('CI', 'CI'),
		('FAV', 'FAV'),
		('ESI', 'ESI'),
		('APCI', 'APCI'),
		('MALDI', 'MALDI'),
	]
	IK_choices = [
		('+', '+イオン'),
		('-', '-イオン'),
	]
	Intoro_choices = [
		('直接', '直接導入'),
		('GC', 'GC導入(EI/CIのみ)'),
		('LC', 'LC導入(ESI/APCIのみ)'),
	]
	res_choices = [
		('LR', '低分解能[LR]測定（通常選択）'),
		('HR', '高分解能[HR]測定（精密質量測定、MALDI選択不可）'),
	]
	mass_choices = [
		('50 ～ 800', '50 ～ 800 ( EIのみ )'),
		('800 ～ 1000', '800 ～ 1000'),
		('1000 ～ 2000', '1000 ～ 2000'),
		('2000 ～', '2000 ～'),
	]
	status_choices = [
		('未割当', '未割当'),
		('予約', '予約'),
		('終了', '終了'),
	]
	# 試料リスト用
	ionMethod = models.CharField(max_length=20,default='',choices=IM_choices)
	ionKind = models.CharField(max_length=20,default='',choices=IK_choices )
	introMethod = models.CharField(max_length=20,default='', choices=Intoro_choices)
	resolution = models.CharField(max_length=20,default='', choices=res_choices)
	mass = models.CharField(max_length=20,default='', choices=mass_choices)
	# remarks = models.CharField(max_length=200,default='')
	remarks = models.TextField()
	flgStatus = models.CharField(max_length=20, default='未割当', choices = status_choices ) 
	charge = models.CharField(max_length=20,default='')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
