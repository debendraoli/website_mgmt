from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from json import loads


class Page(models.Model):
    page = models.CharField(max_length=10, primary_key=True)
    heading = models.CharField(null=True, max_length=255)
    tag_line = models.CharField(null=True, max_length=255)
    title = models.CharField(max_length=40, null=True)
    images = models.TextField(null=False, default='https://witanworld.com/wp-content/uploads/2018/04/Machine-Learning2.jpg')
    slider = models.SmallIntegerField(null=False, default=0)
    meta_tags = models.TextField(default=
                                 '['
                                 '{"key": "name", "key_name": "title", "content": ""},'
                                 '{"key": "name", "key_name": "description", "content": ""},'
                                 '{"key": "name", "key_name": "keywords", "content": ""},'
                                 '{"key": "property", "key_name": "og:title", "content": ""},'
                                 '{"key": "property", "key_name": "og:site_name", "content": ""},'
                                 '{"key": "property", "key_name": "og:url", "content": ""},'
                                 '{"key": "property", "key_name": "og:description", "content": ""},'
                                 '{"key": "property", "key_name": "og:type", "content": ""},'
                                 '{"key": "property", "key_name": "og:image", "content": ""}'
                                 ']'
                                 )
    css = models.TextField(default=
                           '['
                           '{"url":"", "media": ""}'
                           ']'
                           )
    js = models.TextField(default=
                          '[{"url":""}]'
                          )

    def parse_meta_tags(self):
        return loads(self.meta_tags)

    def split_heading(self):
        split_heading = self.heading.split(' ')
        split_length = len(split_heading)
        return {'first': split_heading[:split_length-1], 'last': split_heading[-1]}


class SiteInfo(models.Model):
    info = models.CharField(max_length=8, primary_key=True, default='core')
    about_short = models.TextField()
    about_long = models.TextField()
    address = models.TextField(default={"country": "", "city": "", "address_1": "", "address_2": ""})
    social_sites = models.TextField(default={"facebook": "", "twitter": "", "linkedin": ""})
    phones = models.TextField(default={"phone_1": "", "phone_2": ""})
    emails = models.TextField(default={"email_1": "", "email_2": ""})
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    start_day = models.CharField(max_length=8)  # start of week
    end_day = models.CharField(max_length=8)  # end of week
    platform_info = models.CharField(max_length=255, null=True)

    def process_info(self):
        social_sites, addresses, phones, emails = loads(self.social_sites), loads(self.address), loads(self.phones),\
                                                  loads(self.emails)
        return {'social_sites': social_sites, 'addresses': addresses, 'phones': phones, 'emails': emails}


class Career(models.Model):
    vacancy = models.IntegerField(default=1)
    status = models.SmallIntegerField(default=1)  # 1 = active
    level = models.SmallIntegerField()  # 1 = part time, 2 = full time
    position = models.CharField(max_length=255, default='Software developer')
    education = models.TextField()
    responsibilities = models.TextField()
    salary = models.IntegerField()  # 1 = Negotiable
    currency = models.CharField(max_length=3, default='NPR')
    date_posted = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=None)
    image = models.TextField(default='img/soft-dev.jpg')
    location = models.CharField(max_length=80, default='Kathmandu, Nepal')
    description_short = models.CharField(max_length=255, default='Excellent in something')
    description_long = models.CharField(max_length=255, default='Excellent in something')
    deadline = models.DateTimeField(null=True)
    experience = models.CharField(max_length=50, default='1 year')
    gender = models.SmallIntegerField(default=0)
    benefits = models.TextField()
    experiences_detail = models.TextField(default='2 yrs in related fields\n')

    def format_int(self):
        if self.level == 1:
            return {'time': 'part', 'text': 'Part-time'}
        else:
            return {'time': 'full', 'text': 'Full-time'}

    def format_list(self):
        return {'responsibilities': self.responsibilities.split('\n'),
                'benefits': self.benefits.split('\n'),
                'educations': self.benefits.split('\n'),
                'experiences_detail': self.experiences_detail.split('\n')}


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=20, default='service')
    description = models.TextField()
    short_description = models.TextField()
    status = models.IntegerField()
    link = models.IntegerField()
    tag = models.CharField(max_length=255, default='Our Excellent Service.')
    image = models.TextField()
    animation = models.CharField(max_length=255)
    icon = models.CharField(max_length=20)


class Platform(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    short_description = models.TextField()
    status = models.IntegerField()
    icon = models.CharField(max_length=20)


class Message(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    ip_addr = models.GenericIPAddressField()
    ua = models.TextField()
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()


class JobApplicant(models.Model):
    job_id = models.OneToOneField(Career, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    about = models.TextField()
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    resume = models.FileField()
    photo = models.ImageField()
    country = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()


class CareerQuestion(models.Model):
    career_id = models.OneToOneField(Career, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    image = models.TextField()
    status = models.IntegerField()

