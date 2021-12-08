from django.forms import (
    Form,
    CharField,
    IntegerField,
  
    FloatField,
)


class VisitForm(Form):

    student = CharField()
    math = IntegerField()
    english = IntegerField()
    science=IntegerField()
    #average=FloatField()
    
class VisitorNameForm(Form):
    visitor_name= CharField()


    