from bottle import Bottle, run, request
from spider import job_51job
app = Bottle()


@app.post('/login')
def login():
    print(request.method)
    return "success!"


@app.post('/hello')
def hello():
    print(request.method)
    if request.POST:
        data = request.POST.decode()
        print()
        job_51job.spider_job(data['company'])
        return "success!"
    else:
        return "方法错误"
run(app, host='localhost', port=8443)
