from django.shortcuts import render
from docx2pdf import convert

#convert("word_to_pdf_app/files/Project Template.docx")

# convert("word_to_pdf_app/files/")

# Create your views here.
def home(request):
     convert("word_to_pdf_app/files/mycrm_report.docx", "word_to_pdf_app/files/output.pdf")
     # return render(request,'home.html')
