import parsers


class Test(parsers.Parser):
    a = parsers.BooleanField()
    b = parsers.HourMinuteIntField()
    c = parsers.Field()

    class Meta:
        unique_together = ['a', 'b']

    def __str__(self):
        return f'{self.id} {self.a}'


t1 = Test(a='23', b='02:32', c='b')
t1.save()
t2 = Test(a='', b='2342', c='a')
t2.save()
for obj in Test.objects.all():
    pass
    # print(obj.a)

test_exists = Test.objects.exists(a='23', b='02:32')
print(test_exists)
