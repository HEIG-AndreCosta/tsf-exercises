# Problème 1
Une source discrète sans mémoire X émet des signaux d’amplitude x1 et x2 avec probabilités respec-
tives p1 = 0.8 et p2 = 0.2.

1. Calculer l’entropie de la source X.

H = - (0.8 * log2(0.8) + 0.2 * log2(0.2)  = 0.722

2. Quelle signification physique donnez-vous à l’entropie ?

C'est l'information moyenne envoyé

3. Admettons que la source émette 1000 symboles consécutifs, combien de bits doit-on utiliser en
moyenne si l’efficacité de codage est de 100% ?

Efficacité de codage = 100% => H = I => I = 0.722 bits par symbole

1000 * 0.721 = 722 bits

4. Quelle efficacité optimum allez-vous obtenir en pratique si vous codez les symboles consécutifs un
par un ?

I = 1

0.722 / 1 = 0.722 -> 72%

5. Existe-t-il un moyen d’améliorer l’efficacité de codage ? (Justifiez toute proposition par un calcul
ad hoc.)

Non.


# Problème 2

Un récepteur reçoit un signal à 2.4 GHz subissant une atténuation de 105dB.

1. Quelle est la distance avec l’émetteur si il n’y a pas d’obstacles ?

105db = (4*pi*r*f/c)^2 

105db = 10 log(P * 1000)
log(P*1000) = 105/10

10^(105/10) = P

P = 31.6e9

31.6e9 = (4*pi*r*f/c)^2 

f = 2.4 * 10^9
c = 300'000'000 

(sqrt(31.6e9) * c) / (4*pi*f) = r = 1.768 KM


2. Calculer la puissance reçue en dBm si on émet à 1W et que les antennes sont omnidirectionnelles.



3. De combien varie l’atténuation si on se trouve en milieu urbain (Urban area) ?
