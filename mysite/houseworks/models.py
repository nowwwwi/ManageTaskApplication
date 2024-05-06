from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WorkType(models.Model):
    """"""
    name = models.CharField(max_length=50, verbose_name="名前")
    description = models.CharField(max_length=200, verbose_name="説明")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        """"""
        verbose_name = "家事分類"
        verbose_name_plural = "家事分類"


class Work(models.Model):
    name = models.CharField(max_length=50, verbose_name="名前")
    description = models.CharField(max_length=200, verbose_name="説明")
    is_regular = models.BooleanField(default=True, verbose_name="定期実行の有無")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")

    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE, verbose_name="家事分類")

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "家事"
        verbose_name_plural = "家事"


class WeekDaysOfWork(models.Model):
    """"""
    work = models.ForeignKey(Work, models.CASCADE, verbose_name="家事")
    weekday = models.CharField(max_length=1, verbose_name="曜日")

    def __str__(self) -> str:
        """Return the name of the weekdays of work."""
        return f"execute at {self.weekday}."

    class Meta:
        verbose_name = "実行日"
        verbose_name_plural = "実行日"


class WorkProcess(models.Model):
    name = models.CharField(max_length=50, verbose_name="名前")
    description = models.CharField(max_length=200, verbose_name="説明")
    procedure_number = models.IntegerField(default=1, verbose_name="プロセス番号")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")

    work = models.ForeignKey(Work, models.CASCADE, verbose_name="家事")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "家事プロセス"
        verbose_name_plural = "家事プロセス"


class History(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="ユーザー")
    work = models.ForeignKey(Work, models.CASCADE, verbose_name="家事")


    def __str__(self):
        return f"{self.user} did {self.work} at {self.pub_date}."
    
    class Meta:
        verbose_name = "実行履歴"
        verbose_name_plural = "実行履歴"