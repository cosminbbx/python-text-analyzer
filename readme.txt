Name: Text analyzer
Difficulty: C
ID:20

Scrieți un script care primește la intrare un fișier text și returnează următoarele informații:
numărul de cuvinte, numărul de propoziții, numărul de numere de telefoane CNP-uri găsite în
text, numărul de numere de telefoane (se considera ca un telefon începe cu 07...) găsit în
text, precum și o statistica pe fiecare litera (case insensitive) care sa contina de cate ori apare
și în ce procent din numărul total de litere din text. Pentru CNP-uri și Telefoane se vor calcula
valorile unice (dacă un număr de telefon sau CNP apare de mai multe ori e calculat o singura
data) și se vor și afișa pe ecran (vedeți secțiunea OUTPUT pentru un exemplu).

INPUT: text_analyzer.py <fisier.txt>

OUTPUT:
Cuvinte = 100
Propozitii = 10
CNP(uri) = 2 [1020320123456,1020320123456]
Telefoane = 3 [0740123456, 0740123457, 0740123458],
Litere:
A = 10 (10%)
B = 2 (2%)
.....