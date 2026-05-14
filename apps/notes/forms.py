from django import forms
from .models import Note, Tag


class NoteForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Note
        fields = ['text', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

            tags_str = self.cleaned_data.get("tags", "")
            tags_list = [t.strip() for t in tags_str.split(",") if t.strip()]

            instance.tags.clear()

            for tag_name in tags_list:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        return instance