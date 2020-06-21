# -*- coding: utf-8 -*-

import matematikModule

matematikModule.carp(2, 3)
matematikModule.topla(3,2)



import matematikModule as mm  # as ile modülü yeniden adlandırıp kullanıyoruz

mm.carp(2, 4)
mm.topla(6, 9)

print(mm.customer["firstName"])



from matematikModule import topla # from modülden belirtilen bi yeri çıkarmaya yarar

topla(5,6)

from matematikModule import customer

print(customer["firstName"])

