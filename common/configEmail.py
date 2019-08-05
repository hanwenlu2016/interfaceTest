import os
import getpathInfo
from common.Log import logger
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')  # 获取测试报告路径
logger = logger


class SendEmail:

    @staticmethod
    def send(fromaddrs, passwords, addressees,subject,smtplibs):

        #发送内容
        content = ' 测试已完成！！ 报告已邮件发送！！ '
        textApart = MIMEText(content)

        # imageFile = 'mis .jpg'
        # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
        # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

        # pdfFile = '算法设计与分析基础第3版PDF.pdf'
        # pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        # pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
        #
        zipFile = mail_path
        zipApart = MIMEApplication(open(zipFile, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename='测试报告！')

        m = MIMEMultipart()
        m.attach(textApart)
        #m.attach(imageApart)
        #m.attach(pdfApart)
        m.attach(zipApart)
        m['Subject'] = subject

        try:
            server = smtplib.SMTP(smtplibs)
            server.login(fromaddrs, passwords)  # 登录
            server.sendmail(fromaddrs, addressees, m.as_string())
            print('success')
            logger.info('发送邮件成功！')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:', e)  # 打印错误
            logger.info('发送邮件失败 {}'.format(e))
