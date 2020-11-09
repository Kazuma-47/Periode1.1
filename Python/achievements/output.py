Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 6/4
1.5
>>> 6//4
1
>>> afronden
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    afronden
NameError: name 'afronden' is not defined
>>> print('Mijn naam is Joao')
Mijn naam is Joao
>>> naam 'Joao'
SyntaxError: invalid syntax
>>> naam "Joao"
SyntaxError: invalid syntax
>>> naam= 'Joao'
>>> print(naam)
Joao
>>> print(naam.upper())
JOAO
>>> print(naam[0:2])
Jo
>>> print(naam[2:3])
a
>>> print(naam[0:1])
J
>>> print(naam(::-1)
      
SyntaxError: invalid syntax
>>> print(naam[::-1])
oaoJ
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Joao ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd= leeftijd -1
>>> leeftijd
17
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 1 jaar wordt je 18
>>> rom random import randint
SyntaxError: invalid syntax
>>> from random import randint
>>> randint(0,1000)
922
>>> randint(0,1000)
817
>>> randint(0,1000)
41
>>> randint(0,10)
3
>>> randint(0,3)
0
>>> randint(0,3)
0
>>> randint(0,3)
3
>>> randint(0,3)
3
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
979
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 979
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 12:38:49.425908
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> nederlands
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    nederlands
NameError: name 'nederlands' is not defined
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 