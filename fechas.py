import datetime

print('#--datetime')

currentDate = datetime.date.today()
print('currentDate:')
print(currentDate)
print(datetime.datetime.now())

print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

print('\nstrftime()')
print(currentDate.strftime('%d %b, %Y'))


print('\ndir(datetime.date)')
print(dir(datetime.date))
#['__add__', '__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__',
#'__sizeof__', '__str__', '__sub__', '__subclasshook__', 'ctime', 'day', 'fromordinal', 'fromtimestamp', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'timetuple', 'today', 'toordinal', 'weekday', 'year']

hoy = datetime.date.today()

print(hoy.day)
print(hoy.weekday)
print(hoy.year)
print(hoy.strftime)

from dateutil.relativedelta import relativedelta # pip install python-dateutil

print('\n#--dateutil.relativedelta')

print(hoy + relativedelta(months=+6))
# Sumar a hoy 6 anos y 40 dias
print(hoy + relativedelta(years=6, days=40))

texto_fecha = "March 7 2009 7:30pm EST"
formatting = "%B %d %Y %I:%M%p "
texto_fecha = texto_fecha[:-3]
print(texto_fecha)
fecha_anterior = datetime.datetime.strptime(texto_fecha,formatting)

print(fecha_anterior + datetime.timedelta(hours=12))


import time
print('\n#--time')

print(time.time())

tiempo = time.time()
print(time.localtime(tiempo))



