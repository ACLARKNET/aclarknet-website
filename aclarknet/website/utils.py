def class_name_pk(self):
    """
    Concatenate class name and id
    """
    return '-'.join([self.__class__.__name__.lower(), str(self.pk)])
