from django.db import models
from django.contrib.auth.models import User


WEEKDAY_CHOICES = [
        (0, "月曜日"),
        (1, "火曜日"),
        (2, "水曜日"),
        (3, "木曜日"),
        (4, "金曜日"),
        (5, "土曜日"),
        (6, "日曜日"),
    ]


# Create your models here.
class Work(models.Model):
    """Delare work model."""
    name = models.CharField(max_length=50, verbose_name="名前")
    description = models.CharField(max_length=200, verbose_name="説明")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")
    next_execute_date = models.DateField(auto_now=True, verbose_name="次回予定日")

    # relations
    default_executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="デフォルトの担当者")

    def __str__(self) -> str:
        """Return then name of work."""
        return f"{self.name}"

    class Meta:
        """Meta work model datas."""
        verbose_name = "家事"
        verbose_name_plural = "家事"


class Schedule(models.Model):
    """Delare interval type model."""
    name = models.CharField(max_length=50, verbose_name="名前")
    description = models.CharField(max_length=200, verbose_name="説明", null=True)

    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self) -> str:
        """Return the name of the weekdays of work."""
        return f"{self.name}"

    class Meta:
        verbose_name = "実行タイプ"
        verbose_name_plural = "実行タイプ"


class WorkProcess(models.Model):
    name = models.CharField(max_length=50, verbose_name="名前")
    description = models.CharField(max_length=200, verbose_name="説明")
    procedure_number = models.IntegerField(default=1, verbose_name="プロセス番号")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")

    work = models.ForeignKey(
        Work,
        models.CASCADE,
        related_name="work_processes",
        verbose_name="家事")

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


class HashTag(models.Model):
    """Declare work type model."""
    name = models.CharField(max_length=50, verbose_name="名前")
    description = models.CharField(max_length=200, verbose_name="説明")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self) -> str:
        """Return the name of work type."""
        return f"{self.name}"

    class Meta:
        """Meta work type datas."""
        verbose_name = "ハッシュタグ"
        verbose_name_plural = "ハッシュタグ"

class WorkSchedule(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE
    )

    schedule = models.ForeignKey(
        Schedule,
        on_delete = models.CASCADE
    )

    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self) -> str:
        """Return the name of work type."""
        return f"{self.work.name}"

    class Meta:
        """Meta work type datas."""
        verbose_name = "タスクの実行"
        verbose_name_plural = "タスクの実行"


class WorkHashtag(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE
    )

    hashtag = models.ForeignKey(
        HashTag,
        on_delete=models.CASCADE
    )

    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日")
