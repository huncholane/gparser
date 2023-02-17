import parsers


class Test(parsers.Parser):
    a = parsers.BooleanField()
    b = parsers.HourMinuteIntField()

    def __str__(self):
        return f'{self.id} {self.a}'


t1 = Test(a='23', b='02:32')
t1.save()
t2 = Test(a='', b='2342')
t2.save()
for obj in Test.objects.all():
    print(obj.a)
