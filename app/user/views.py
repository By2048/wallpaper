from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.core.mail import send_mail

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm
from .models import UserProfile


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        next = request.GET.get('next', '')
        return render(request, 'user/register.html', context={'register_form': register_form, 'next': next})

    def post(self, request):
        next = request.POST.get('next', '')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Subject here',
                'Here is the message.',
                'user_admin@email.com',
                [form.email],
                fail_silently=False,
            )
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            register_form = RegisterForm()
            return render(request, 'user/register.html', context={'register_form': register_form})


# # 发送邮箱验证码的view:
# class SendEmailCodeView(LoginRequiredMixin, View):
#     def get(self, request):
#         # 取出需要发送的邮件
#         email = request.GET.get("email", "")
#
#         # 不能是已注册的邮箱
#         if UserProfile.objects.filter(email=email):
#             return HttpResponse(
#                 '{"email":"邮箱已经存在"}',
#                 content_type='application/json')
#         send_register_eamil(email, "update_email")
#         return HttpResponse(
#             '{"status":"success"}',
#             content_type='application/json')
#
#
# # 用户上传图片的view:用于修改头像
# class UploadImageView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def post(self, request):
#         # 这时候用户上传的文件就已经被保存到imageform了 ，为modelform添加instance值直接保存
#         image_form = UploadImageForm(
#             request.POST, request.FILES, instance=request.user)
#         if image_form.is_valid():
#             image_form.save()
#             # # 取出cleaned data中的值,一个dict
#             # image = image_form.cleaned_data['image']
#             # request.user.image = image
#             # request.user.save()
#             return HttpResponse(
#                 '{"status":"success"}',
#                 content_type='application/json')
#         else:
#             return HttpResponse(
#                 '{"status":"fail"}',
#                 content_type='application/json')
#
#
# class UserInfoView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def get(self, request):
#         return render(request, "usercenter-info.html", {
#
#         })
#
#     def post(self, request):
#         # 不像用户咨询是一个新的。需要指明instance。不然无法修改，而是新增用户
#         user_info_form = UserInfoForm(request.POST, instance=request.user)
#         if user_info_form.is_valid():
#             user_info_form.save()
#             return HttpResponse(
#                 '{"status":"success"}',
#                 content_type='application/json')
#         else:
#             # 通过json的dumps方法把字典转换为json字符串
#             return HttpResponse(
#                 json.dumps(
#                     user_info_form.errors),
#                 content_type='application/json')
#
#
# # 修改邮箱的view:
# class UpdateEmailView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def post(self, request):
#         email = request.POST.get("email", "")
#         code = request.POST.get("code", "")
#
#         existed_records = EmailVerifyRecord.objects.filter(
#             email=email, code=code, send_type='update_email')
#         if existed_records:
#             user = request.user
#             user.email = email
#             user.save()
#             return HttpResponse(
#                 '{"status":"success"}',
#                 content_type='application/json')
#         else:
#             return HttpResponse(
#                 '{"email":"验证码无效"}',
#                 content_type='application/json')
#
#
# # 个人中心页我的课程
#
# class MyCourseView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def get(self, request):
#         user_courses = UserCourse.objects.filter(user=request.user)
#         return render(request, "usercenter-mycourse.html", {
#             "user_courses": user_courses,
#         })
#
#
# # 我收藏的机构
#
# class MyFavOrgView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def get(self, request):
#         org_list = []
#         fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
#         # 上面的fav_orgs只是存放了id。我们还需要通过id找到机构对象
#         for fav_org in fav_orgs:
#             # 取出fav_id也就是机构的id。
#             org_id = fav_org.fav_id
#             # 获取这个机构对象
#             org = CourseOrg.objects.get(id=org_id)
#             org_list.append(org)
#         return render(request, "usercenter-fav-org.html", {
#             "org_list": org_list,
#         })
#
#
# # 我收藏的授课讲师
#
# class MyFavTeacherView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def get(self, request):
#         teacher_list = []
#         fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
#         # 上面的fav_orgs只是存放了id。我们还需要通过id找到机构对象
#         for fav_teacher in fav_teachers:
#             # 取出fav_id也就是机构的id。
#             teacher_id = fav_teacher.fav_id
#             # 获取这个机构对象
#             teacher = Teacher.objects.get(id=teacher_id)
#             teacher_list.append(teacher)
#         return render(request, "usercenter-fav-teacher.html", {
#             "teacher_list": teacher_list,
#         })
#
#
# # 我收藏的课程
#
# class MyFavCourseView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def get(self, request):
#         course_list = []
#         fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
#         # 上面的fav_orgs只是存放了id。我们还需要通过id找到机构对象
#         for fav_course in fav_courses:
#             # 取出fav_id也就是机构的id。
#             course_id = fav_course.fav_id
#             # 获取这个机构对象
#             course = Course.objects.get(id=course_id)
#             course_list.append(course)
#         return render(request, "usercenter-fav-course.html", {
#             "course_list": course_list,
#         })
#
#
# # 我的消息
# class MyMessageView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#
#     def get(self, request):
#         all_message = UserMessage.objects.filter(user=request.user.id)
#
#         # 用户进入个人中心消息页面，清空未读消息记录
#         all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
#         for unread_message in all_unread_messages:
#             unread_message.has_read = True
#             unread_message.save()
#         # 对课程机构进行分页
#         # 尝试获取前台get请求传递过来的page参数
#         # 如果是不合法的配置参数默认返回第一页
#         try:
#             page = request.GET.get('page', 1)
#         except PageNotAnInteger:
#             page = 1
#         # 这里指从allorg中取五个出来，每页显示5个
#         p = Paginator(all_message, 4)
#         messages = p.page(page)
#         return render(request, "usercenter-message.html", {
#             "messages": messages,
#         })
#
#