from django.shortcuts import render, redirect, get_object_or_404
from .models import Registro, Sale
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, View
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy
from xhtml2pdf import pisa
from crud import utils
from django.template.loader import get_template
from django.shortcuts import render
from django.views.generic import TemplateView
import io
from reportlab.pdfgen import canvas
from django.http import FileResponse
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4


def GenPdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=A4)

    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'GLu - Diario de emociones')

    c.setFont('Helvetica', 12)
    c.drawString(30,735,'Reistro de emociones')

    c.setFont('Helvetica-Bold',12)
    c.drawString(440, 735,"Glu created by ScarlettOC")

    c.setFont('Helvetica-Bold',12)
    c.drawString(250, 690,"Revisa tu pdf en la parte de abajo para ver tus registros")
    
    c.line(460,747,560,747)

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)
 
    sales = Registro.objects.all()

    lines = []

    for sale in sales:
        lines.append(sale.nombre)
        lines.append(sale.sentimiento)
        lines.append("- - - - - - - - - - - -")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=("Glu.pdf"))

class Listar(ListView):
    model=Registro
    template_name='listar.html'
    context_object_name='listas' 

class Crear(CreateView):
    model=Registro
    template_name='crear.html'
    fields=('nombre','sentimiento','nota','image')#Permite aceso a 3 parámetros
    success_url=reverse_lazy('listar')#Al crear regresa a listar

class VistaInd(DetailView):
    model=Registro
    template_name='detalle.html'
    context_object_name='listas'


class Actualizar(UpdateView):
    model=Registro
    template_name='actualiza.html'
    context_object_name='listas'
    fields=('nombre','sentimiento','nota','image')

    def get_success_url(self):
        return reverse_lazy('detalle',kwargs={'pk':self.object.id})

class Eliminar(DeleteView):
    model=Registro
    template_name='eliminar.html'
    success_url=reverse_lazy('listar')
    
