from django import forms
from food.models import item, special_item



class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ["item_name","item_full_desc", "item_sort_desc","category", "item_price","item_image"]


class specialItemForm(forms.ModelForm):
    class Meta:
        model = special_item
        fields = ["item_name", "item_sort_desc","category", "item_price","item_image"]
