from django.forms.models import ModelForm

from walkthedog.dashboard.models import Order


class ClientOrderFrom(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClientOrderFrom, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ('location', 'date', 'start_of_walk', 'end_of_walk', 'name', 'breed', 'size', 'price',
                  'additional_option', 'coordinates')

    def save(self, commit=True):
        instance = super(ClientOrderFrom, self).save(commit=False)
        instance.user = self.user

        if commit:
            instance.save()
        return instance
