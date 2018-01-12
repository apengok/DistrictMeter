
class GisRouter:
    """
    A router to control all database operations on models in the
    gis application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read gis models go to gis.
        """
        if model._meta.app_label == 'gis':
            return 'gis'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write gis models go to gis.
        """
        if model._meta.app_label == 'gis':
            return 'gis'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the gis app is involved.
        """
        if obj1._meta.app_label == 'gis' or \
           obj2._meta.app_label == 'gis':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the gis app only appears in the 'gis'
        database.
        """
        if app_label == 'gis':
            return db == 'gis'
        return None