# coding:gbk
import socket  # ���� socket ģ��

s = socket.socket()  # ���� socket ����
host = socket.gethostname()  # ��ȡ����������
port = 12345  # ���ö˿�
s.bind((host, port))  # �󶨶˿�

s.listen(5)  # �ȴ��ͻ�������
while True:
    c, addr = s.accept()  # �����ͻ�������
    print '���ӵ�ַ��', addr
    c.send('��ӭ���ʲ���̳̣�')
    c.close()  # �ر�����