import os
import uuid

class UploadToPathAndRename:
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[-1]
        uuid_str = uuid.uuid4().hex[:16]
        app_label = instance._meta.app_label.lower()
        class_name = instance.__class__.__name__.lower()
        return f"{app_label}/{class_name}/{self.field_name}/{uuid_str}{ext}"

    def deconstruct(self):
        return (
            f"{self.__class__.__module__}.{self.__class__.__name__}",
            [self.field_name],
            {},
        )



SPONSOR_LEVEL_CHOICES = {
    'silver': 'Silver',
    'bronze': 'Bronze',
    'gold': 'Gold',
    'platinum': 'Platinum',
    'diamond': 'Diamond'
}