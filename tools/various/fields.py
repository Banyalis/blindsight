from django.db import models
import json

class CustomList(list):
    def __str__(self):
        return json.dumps(self)
    def __unicode__(self):
        return self.__str__()
class CustomDict(dict):
    def __str__(self):
        return json.dumps(self)
    def __unicode__(self):
        return self.__str__()

class CustomListField(models.TextField):
    #__metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, default=[], *args, **kwargs):
        super(CustomListField, self).__init__(default=default, *args, **kwargs)

    def from_db_value(self, value, *args, **kwargs):
        return self.to_python(value)

    def to_python(self, value):
        #print "to_python"
        if not value: value = []

        if isinstance(value, basestring):
            value = json.loads(value)
        if isinstance(value, list):
            return CustomList(value)
        if isinstance(value, dict):
            return CustomDict(value)

        return value

    def get_prep_value(self, value):
        #print "get_prep_value"
        if value is None: return value

        res = unicode(json.dumps(value))
        return res

    def value_to_string(self, obj):
        if isinstance(obj, basestring):
            return obj
        val = self._get_val_from_obj(obj)
        return '' if val is None else val.isoformat()

class CustomIntPointField(models.CharField):
    #__metaclass__ = models.SubfieldBase
    description = "Stores a integer point (x,y)"

    def __init__(self,  max_length=64, default='{"x":0,"y":0}', null=True ,blank = True, **kwargs):
        super(CustomIntPointField, self).__init__(max_length=max_length,default=default, null=null, blank=blank, **kwargs)

    def to_python(self, value):
        #print "to_python: ", value
        if not value: value = []

        if isinstance(value, dict):
            return value

        return json.loads(value)

    def get_prep_value(self, value):
        #print "get_prep_value"
        if value is None: return value
        if isinstance(value, dict):
            value = {
                'x' : value.get('x', 0),
                'y' : value.get('y', 0),
            }

        print unicode(json.dumps(value))
        return unicode(json.dumps(value))

    def value_to_string(self, obj):
        val = self._get_val_from_obj(obj)
        return '' if val is None else val.isoformat()



class CustomOrderField(models.PositiveSmallIntegerField):
    description = "Stores a auto incremented order"

    def __init__(self, blank = True, default = 0, db_index = True, **kwargs):
        super(CustomOrderField, self).__init__(blank=blank,default=default, db_index=db_index, **kwargs)

    def pre_save(self, instance, add):
        val = getattr(instance, self.name, None)
        if not val:
            cl = instance.__class__

            try:    order = cl.objects.order_by('-'+self.name)[0].order+1
            except: order = 1
            setattr(instance, self.name, order)

        return super(CustomOrderField, self).pre_save(instance, add)
