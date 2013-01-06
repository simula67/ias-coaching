# Create your views here.
from django.http import HttpResponse
from iasstudy_search.models import *
from django.template.loader import get_template
from django.template import Context, Template

class Quote:
	def __init__(self):
		self.name = ""
		self.quotation = ""
		self.posion = ""
		self.field = ""


def downloadable(request):
	allQuotes = []
	allPersonalities = Personality.objects.all()
	for person in allPersonalities:
		quotations = person.quotations.all()
		for quotation in quotations:
			quote = Quote()
			quote.name = person.name
			quote.quotation = quotation.text
			quote.position = quotation.position.name
			quote.field = quotation.position.field.name
			allQuotes.append(quote)
	testTemplate = get_template("table_search.html")
	html = testTemplate.render(Context( {'allQuotes': allQuotes} ))
	return HttpResponse(html)

