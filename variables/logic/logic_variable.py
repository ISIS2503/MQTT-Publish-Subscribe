from ..models import Variable

def get_variables():
    queryset = Variable.objects.all()
    return (queryset)

def create_variable(form):
    measurement = form.save()
    measurement.save()
    return ()

def get_variable_by_name(name):
    try:
        variable = Variable.objects.get(name=name)
    except:
        variable = None
    return (variable)

def create_variable_object(name):
    variable = Variable()
    variable.name=name
    variable.save()
    return (variable)
