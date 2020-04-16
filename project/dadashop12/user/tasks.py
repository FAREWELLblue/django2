from django.core.mail import send_mail
from django.conf import settings
from dadashop12.celery import app

@app.task
def sent_active_email_async(email_address,v_url):
    #发激活邮件
    subject='达达商城激活邮件'#题目
    html_message='''
    <p>尊敬的用户您好</p>
    <p>请点击此链接激活您的账户(三天内有效):</p>
    <p><a href='%s' target='_blank'>点击激活</a></p>
    '''%(v_url)
    send_mail(subject,'',html_message=html_message,recipient_list=[email_address],
              from_email=settings.EMAIL_HOST_USER)
