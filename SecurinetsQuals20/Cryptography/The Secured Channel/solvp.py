from sympy.solvers import solve
from sympy import Symbol
from sympy import *

p=Symbol('p')
S=2**1024+31336
n=7658667062322026038449982247558761740004869156981524026836170582083896041054040325870190417072975704156748210501677817474529699134763410714206058569898628559393561314371939088661660712983662947603280590188476639425295406857391436940961662270067242446960578332648268884988326969765931295295653691509883260243479526535660482751525751040392249510776659146386445128015172986863059432004644090045463124989246912213064462529744106006633353340537798307164747936187787865898686332132141593938203766535698957683075275429743508979879596943605491190852215951238869768425523897496010303874659739389741386213401759122134521865367
print (solve(p**2-S*p+n,p))