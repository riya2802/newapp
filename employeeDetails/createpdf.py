from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template,render_to_string

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	print("1")
	print('template_src',template_src)
	template = get_template(template_src)
	print("2")

	html  = template.render(context_dict)
	print("3")
	result = BytesIO()
	print("4")
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	print("5")
	print("pdf",pdf)
	print("6")
	print("7")
	print("result.getvalue()",result.getvalue(), )
	if not pdf.err:
		print("8")
		return (result.getvalue())
	print("9")    
	return None