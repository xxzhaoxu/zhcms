import django_redis
from django.http import HttpResponse
from zhdb.models import User, BaseInfo, News, Job, Aptitudes, Banner
from zhCMS.common.ResultUtils import success, fail, page_handler
from zhCMS.common.HttpUtils import JSONResponse
from zhCMS.common.AESUtils import encrypt_oracle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time


def hello(request):
    return JSONResponse(success("恭喜你，请求成功！"))


def login(request):
    if 'POST' == request.method:
        account = request.POST.get('account')
        pswd = request.POST.get('pswd')
        u = User.objects.get(account=account, pswd=pswd)
        # token = encrypt_oracle(str(u.id) + '_' + u.account)
        try:
            if u is not None:
                token = encrypt_oracle(str(u.id) + '_' + u.account).replace('\n', '')
                conn = django_redis.get_redis_connection()
                conn.set(u.id, str(token))
                return JSONResponse(success(u._toJSON(), token))
        except:
            return JSONResponse(fail(400, '登录失败'))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def find_all_user(request):
    if 'POST' == request.method:
        page_size = request.POST.get('pageSize')
        page_index = request.POST.get('pageIndex')
        try:
            user_list = User.objects.all()
            for u in user_list:
                u.pswd = ''

            return JSONResponse(success(user_list))
        except:
            return JSONResponse(success([]))


def find_base_info(request):
    try:
        return JSONResponse(success(BaseInfo.objects.filter(id=1)))
    except:
        return JSONResponse(success(None))


def update_base_info(request):
    if 'POST' == request.method:
        try:
            web_side_name = request.POST.get('web_side_name')
            logo_url = request.POST.get('logo_url')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            record_number = request.POST.get('record_number')
            pk = request.POST.get('id')
            baseInfo = BaseInfo.objects.get(id=pk)
            if len(web_side_name) > 3:
                baseInfo.web_side_name = web_side_name
            if len(logo_url) > 3:
                baseInfo.logo_url = logo_url
            if len(phone) > 3:
                baseInfo.phone = phone
            if len(email) > 3:
                baseInfo.email = email
            if len(record_number) > 3:
                baseInfo.record_number = record_number
            baseInfo.save()
            return JSONResponse(success(baseInfo._toJSON()))
        except:
            return JSONResponse(fail(400, '操作失败'))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def save_update_news(request):
    if 'POST' == request.method:
        import time
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        author = request.POST.get('author', '')
        create_time = time.time()
        img_url = request.POST.get('img_url', '')
        n_type = request.POST.get('n_type', '')

        pk = request.POST.get('pk')
        news = News(id=pk, title=title, content=content, author=author, create_time=create_time, img_url=img_url,
                    n_type=n_type, is_show='1')
        news.save()
        return JSONResponse(success(news._toJSON()))
    else:
        return JSONResponse(fail(500, "请求方式错误"))


def find_news(request):
    if 'POST' == request.method:
        n_type = request.POST.get('type', '1')
        return JSONResponse(success(News.objects.filter(n_type=n_type).order_by('-create_time')))
    else:
        return JSONResponse(fail(500, "请求方式错误"))


def find_news_by_id(request):
    if 'POST' == request.method:
        news = News.objects.filter(id=request.POST.get('id'))
        return JSONResponse(success(news))
    else:
        return JSONResponse(fail(500, "请求方式错误"))


def delete_news(request):
    if 'POST' == request.method:
        try:
            news = News.objects.get(id=request.POST.get('id'))
        except:
            return JSONResponse(fail(400, '参数错误'))
        if news is not None:
            news.is_show = request.POST.get('is_show', '1')
            news.save()
        return JSONResponse(success(news._toJSON()))
    else:
        return JSONResponse(fail(500, "请求方式错误"))


def add_job(request):
    if 'POST' == request.method:
        import time
        job_name = request.POST.get('job_name')
        job_desc = request.POST.get('job_desc')
        professional = request.POST.get('professional')
        education_level = request.POST.get('education_level')
        work_address = request.POST.get('work_address')
        people_number = request.POST.get('people_number')
        work_age = request.POST.get('work_age')
        gender = request.POST.get('gender')
        people_age = request.POST.get('people_age')
        salary = request.POST.get('salary')
        work_range = request.POST.get('work_range')
        contact = request.POST.get('contact')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        valid_time = request.POST.get('valid_time')
        job = Job(job_name=job_name,
                  job_desc=job_desc,
                  professional=professional,
                  education_level=education_level,
                  work_address=work_address,
                  people_number=people_number,
                  people_age=people_age,
                  work_age=work_age,
                  gender=gender,
                  salary=salary,
                  work_range=work_range,
                  contact=contact,
                  phone=phone,
                  email=email,
                  address=address,
                  valid_time=valid_time,
                  update_time=time.time(),
                  create_time=time.time(),
                  is_show='1',
                  )
        job.save()
        return JSONResponse(success(job._toJSON()))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def update_job(request):
    if 'POST' == request.method:
        job_name = request.POST.get('job_name', '')
        job_desc = request.POST.get('job_desc', '')
        professional = request.POST.get('professional', '')
        education_level = request.POST.get('education_level', '')
        work_address = request.POST.get('work_address', '')
        people_number = request.POST.get('people_number', '')
        work_age = request.POST.get('work_age', '')
        gender = request.POST.get('gender', '')
        people_age = request.POST.get('people_age', '')
        salary = request.POST.get('salary', '')
        work_range = request.POST.get('work_range', '')
        contact = request.POST.get('contact', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        valid_time = request.POST.get('valid_time', '')
        pk = request.POST.get('id', '')
        is_show = request.POST.get('is_show', '')
        import time

        try:
            job = Job.objects.get(id=pk)
            if '' is not job_name:
                job.job_name = job_name
            if '' is not professional:
                job.professional = professional
            if '' is not job_desc:
                job.job_desc = job_desc
            if '' is not education_level:
                job.education_level = education_level
            if '' is not work_address:
                job.work_address = work_address
            if '' is not people_number:
                job.people_number = people_number
            if '' is not people_age:
                job.people_age = people_age
            if '' is not work_age:
                job.work_age = work_age
            if '' is not gender:
                job.gender = gender
            if '' is not salary:
                job.salary = salary
            if '' is not work_range:
                job.work_range = work_range
            if '' is not contact:
                job.contact = contact
            if '' is not phone:
                job.phone = phone
            if '' is not email:
                job.email = email
            if '' is not address:
                job.address = address
            if '' is not valid_time:
                job.valid_time = int(valid_time)
            if '' is not is_show:
                job.is_show = is_show
            job.update_time = time.time()
        except:
            return JSONResponse(fail(400, '参数错误'))
        job.save()
        return JSONResponse(success(job._toJSON()))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def find_jobs(request):
    if 'POST' == request.method:
        page_size = request.POST.get('pageSize', 3)
        page_index = request.POST.get('pageIndex', 1)
        job_list = Job.objects.all()
        count = Job.objects.count()
        paginator = Paginator(job_list, page_size)
        try:
            job_list = paginator.page(int(page_index))
        except:
            job_list = []
        return JSONResponse(page_handler(count, paginator.num_pages, int(page_index), job_list))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def find_jobs_by_id(request):
    if 'POST' == request.method:
        pk = request.POST.get('id')
        return JSONResponse(success(Job.objects.filter(id=pk)))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


'''
保存资质
'''


def save_aptitudes(request):
    if 'POST' == request.method:
        name = request.POST.get('name', '')
        if '' != name:
            if Aptitudes.objects.filter(name=name).__len__() == 0:
                aptitudes = Aptitudes(name=name, create_time=time.time())
                aptitudes.save()
                return JSONResponse(success(aptitudes._toJSON()))
            else:
                return JSONResponse(fail(400, '保存失败'))
        else:
            return JSONResponse(fail(400, '参数错误'))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


'''
查询所有资质
'''


def find_aptitudes(request):
    if 'POST' == request.method:
        try:
            return JSONResponse(success(Aptitudes.objects.all()))
        except:
            return JSONResponse(success([]))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def save_update_banner(request):
    if 'POST' == request.method:
        pk = request.POST.get('id')
        urls = request.POST.get('urls')
        name = request.POST.get('name')
        create_time = request.POST.get('create_time', time.time())
        banner = Banner(id=pk, name=name, urls=urls, create_time=create_time)
        banner.save()
        return JSONResponse(success(banner._toJSON()))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def find_banner(request):
    if 'GET' == request.method:
        pk = request.GET['id']
        banner = Banner.objects.get(id=pk)
        return JSONResponse(success(banner._toJSON()))
    else:
        return JSONResponse(fail(500, '请求方式错误'))


def find_all_banner(request):
    if 'POST' == request.method:
        return JSONResponse(success(Banner.objects.all()))
    else:
        return JSONResponse(fail(500, '请求方式错误'))
