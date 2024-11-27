def store_username_and_delete(instance, **kwargs):
    instance.user = instance.user.first_name + instance.user.last_name
    instance.save(update_fields=['user'])