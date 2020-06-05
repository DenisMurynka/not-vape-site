from django.shortcuts import render
from django.core.mail import send_mail,EmailMultiAlternatives
import os
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from django.template.loader import get_template
#from liqpay import LiqPay
#from liqpay.liqpay import LiqPay
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
EMAIL_ADDRESS = ''
#EMAIL_ADDRESS = os.environ.get('dmurinka@gmail.com')
EMAIL_PASSWORD = ''

# Create your views here.
def landing(request):
    return render(request,'landing/landing.html',locals())


def sent_mail(request):
    TO = 'dmurinka@gmail.com'
    SUBJECT = "Testing sending using gmail"
    # TEXT ='http://google.com'
    # #TEXT = "<html><head></head><body><a href='http://mywebsite.com'>myWebsite</a></body></html>"
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # BODY = '\r\n'.join(['To: %s' % TO,
    #                     'From: %s' % EMAIL_ADDRESS,
    #                     'Subject: %s' % SUBJECT,
    #                     '', TEXT])
    # server.sendmail(EMAIL_ADDRESS, [TO], BODY)

    BODY = """

  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">
    table{
        background-color: #AAD373;
        empty-cells:hide;
    }
    td.cell{
        background-color: white;
    }
  </style>



<table style="border: blue 1px solid;">

<tbody>
<tr>
<td class="cell">Cell 1.1</td>
<td class="cell">Cell 1.2</td>
</tr>

  <p>
    <a href="http://htmlbook.ru/example/knob.html">Абсолютная ссылка</a>
  </p>
  <h1>
    <a href="{% url 'checked' %}"> {{unsubcribe}} </a>
  </h1>
<tr>
<td class="cell">Cell 2.1</td>
<td class="cell"></td>
</tr>

</tbody>
</table>


"""#need to adjust msg body,because of VALUE sasha,and go finally use bootstrap? how do you do

    # Create message container - the correct MIME type is multipart/alternative
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = EMAIL_ADDRESS
    MESSAGE.preamble = """
    Your mail reader does not support the report format.
    Please visit us <a href="http://www...""" #rand sites

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com', 587)

    password = EMAIL_PASSWORD
    server.starttls()
    server.login(EMAIL_ADDRESS, password)
    server.sendmail(EMAIL_ADDRESS, [TO], MESSAGE.as_string())
    server.quit()
    return render(request, "temp.html", {})


def checked(request):
    return render(request, "newsletters/unsubcribe.html", {})#omg sasha TAKE A LOOK PLEASE AT THIS хтмл
