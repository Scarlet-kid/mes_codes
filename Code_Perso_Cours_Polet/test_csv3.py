from collections import OrderedDict

un = OrderedDict()
un["arabe"] = 1
un["latin"] = 'I'

unbis = OrderedDict()
unbis["latin"] = 'I'
unbis["arabe"] = 1

uno = {}
uno["arabe"] = 1
uno["latin"] = 'I'

unobis = {}
unobis["latin"] = 'I'
unobis["arabe"] = 1

print(un, unbis)
print(uno, unobis)

print("uno == unobis?", uno==unobis)
print("un == unbis?", un==unbis)
