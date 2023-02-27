from django.forms import (
    DateInput,
    DateTimeInput,
    ModelForm,
    Textarea,
    TextInput,
    TimeInput,
)

from .models import Articles


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "anons", "full_text", "date"]

        widgets = {
            "title": TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок"}
            ),
            "anons": TextInput(attrs={"class": "form-control", "placeholder": "Анонс"}),
            "full_text": Textarea(
                attrs={"class": "form-control", "placeholder": "Основной текст"}
            ),
            "date": DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Дата и время публикации",
                }
            ),
        }
