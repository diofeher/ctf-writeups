import sys
import pdb
from bottle import route, run, debug, template, request, static_file, error
from bottle import default_app
import re
import math
import subprocess
import random, string
import os


dockerfile_tpl = """
FROM ubuntu:18.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
WORKDIR /tmp
COPY . .
payload
# code.py
CMD ["python3", "code.py"]
"""

page_tpl = '''
    <!doctype html>
    <html>
    <title>SSS - Super Secure Sandbox</title>
    <head>
    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/limonte-sweetalert2/7.28.5/sweetalert2.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/limonte-sweetalert2/7.28.5/sweetalert2.min.css">
    <style>
    .swal2-modal pre {
          background: #49483e;
          color: #f7f7f7;
          padding: 10px;
          font-size: 14px;
          text-align: left;
        }
    .container { margin-top: 50px; }
    .lds-ring {
      display: inline-block;
      position: relative;
      width: 64px;
      height: 64px;
    }
    #loading { display: none; }
    .lds-ring div {
      box-sizing: border-box;
      display: block;
      position: absolute;
      width: 51px;
      height: 51px;
      margin: 6px;
      border: 6px solid #696969;
      border-radius: 50%;
      animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
      border-color: #696969 transparent transparent transparent;
    }
    .lds-ring div:nth-child(1) {
      animation-delay: -0.45s;
    }
    .lds-ring div:nth-child(2) {
      animation-delay: -0.3s;
    }
    .lds-ring div:nth-child(3) {
      animation-delay: -0.15s;
    }
    @keyframes lds-ring {
      0% {
        transform: rotate(0deg);
      }
      100% {
        transform: rotate(360deg);
      }
    }
    </style>
    </head>
    <body class="bg-light">
    <center>
    <div class="container">
    <h1>Super Secure Sandbox</h1>
    <img src="https://i.imgur.com/9CjofF7.jpg" class="rounded-circle mx-auto" width="370" />
    <p><h5>Upload a new Python code to Run!</h5></p>
    <br>
    <br>
    <form method="post" enctype="multipart/form-data" action="/upload">
         <input id="the-file" type="file" name="file">
         <input value="Upload" class="btn btn-primary">
    </form>
    </div>
    <div id="loading" class="lds-ring"><div></div><div></div><div></div><div></div></div>
    </center>
    </body>
    <script>
        $(".btn.btn-primary").click( function()
           {
            var fileName = $('input[type=file]').val().replace(/.*(\\/|\\\\)/, '');
            var data = new FormData(jQuery('form')[0]);
            data.append('filename', fileName);
            jQuery.ajax({
                url: '/upload',
                data: data,
                cache: false,
                contentType: false,
                processData: false,
                method: 'POST',
                type: 'POST', // For jQuery < 1.9
                success: function(data){
                    var isError = data.includes("ERROR");
                    if (isError){
                        swal({
                          type: 'error',
                          html: '<center><img src="https://i.giphy.com/media/njYrp176NQsHS/giphy.webp" class="rounded mx-auto" width="450"/><audio autoplay><source src="https://www.myinstants.com/media/sounds/gandalf_shallnotpass.mp3" type="audio/mpeg"></audio><br/><br/><p>' + data + '</p></center>',
                        })
                    } else {
                        swal({
                          type: 'success',
                          html: data,
                        }).then(function(){
                            location.reload();
                           });
                    }
                },
                error: function(xhr, status, error) {
                        swal({
                          type: 'error',
                          html: '<center><img src="https://i.giphy.com/media/njYrp176NQsHS/giphy.webp" class="rounded mx-auto" width="450"/><audio autoplay><source src="https://www.myinstants.com/media/sounds/gandalf_shallnotpass.mp3" type="audio/mpeg"></audio><br/><br/><p>' + xhr.responseText + '</p></center>',
                        })
                }
            });
           }
        );
        $(document).ready(function () {
            $(document).ajaxStart(function () {
                $("#loading").show();
            }).ajaxStop(function () {
                $("#loading").hide();
            });
        });
    </script>
    <footer class="page-footer font-small blue fixed-bottom">
      <div class="footer-copyright text-center py-3">Created by
        <a href="https://github.com/pimps/"> pimps</a> - Powered by Docker
      </div>
    </footer>
    </html>
    '''

def run_sandbox(directory, filename):
    workdir = os.path.join("/tmp", directory)
    dockerfile_content = dockerfile_tpl % filename
    result = ""
    with open(os.path.join(workdir, "Dockerfile"), "w+") as text_file:
        text_file.write("%s" % dockerfile_content)
        print(dockerfile_content)
    try:
        p = subprocess.check_output(['docker', 'build', '-t', directory, '.'], cwd=workdir)
        result += p.decode("utf-8")
    except Exception as e:
        result += "ERROR: " + str(e)
    try:
        p = subprocess.check_output(['docker', 'run', directory], cwd=workdir)
        result += p.decode("utf-8")
    except Exception as e:
        result += "ERROR: " + str(e)
    return result


@route('/upload', method='POST')
def upload_file():
    if request.method == 'POST':
        # check if the post request has a file
        if 'file' not in request.files:
            return 'ERROR: Select a file to upload!'
        file = request.files['file']
        filename = request.POST.filename
        # check if the filename is empty
        if filename == '':
            return 'ERROR: Filename cannot be empty!'
        # Security protections ;-) the world is full of hackers!
        if "../" in filename:
            return 'ERROR: Hey Hacker... YOU SHALL NOT PASS!!'
        if file:
            rand_dir = ''.join([random.choice(string.ascii_lowercase) for n in range(10)])
            os.mkdir(os.path.join("/tmp", rand_dir))
            print('RAND DIR', rand_dir)
            try:
                print("SAVING FILE", filename)
                file.save(os.path.join("/tmp", rand_dir, filename))
                # file.save(os.path.join("/tmp", rand_dir, 'test.py'))
            except Exception as e:
                print('ERR FILENAME', e)
                sys.exit()
            result = run_sandbox(rand_dir, filename)
            return "<pre><code>%s</code></pre>" % result

@route('/', method='GET')
def index():
    return page_tpl

@error(403)
def mistake403(code):
    return 'ERROR: There is a problem in your url!'

@error(404)
def mistake404(code):
    return 'ERROR: Sorry, this page does not exist!'

@error(500)
def mistake500(code):
    return 'ERROR: OOOOOPS... something went really wrong :-/'

if __name__ == "__main__":
    run(host="0.0.0.0", port=8091, reloader=True)
else:
    application = default_app()
