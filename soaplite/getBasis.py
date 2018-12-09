import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.linalg import *

w = np.zeros(100);
x = np.zeros(100);
w[0] = 7.34634490505672E-4;
w[1] = 0.001709392653518105;
w[2] = 0.002683925371553482;
w[3] = 0.003655961201326375;
w[4] = 0.00462445006342212;
w[5] = 0.00558842800386552;
w[6] = 0.00654694845084532;
w[7] = 0.007499073255464712;
w[8] = 0.008443871469668971;
w[9] = 0.00938041965369446;
w[10] = 0.01030780257486897;
w[11] = 0.01122511402318598;
w[12] = 0.012131457662979497;
w[13] = 0.0130259478929715423;
w[14] = 0.0139077107037187727;
w[15] = 0.014775884527441302;
w[16] = 0.015629621077546003;
w[17] = 0.01646808617614521;
w[18] = 0.017290460568323582;
w[19] = 0.018095940722128117;
w[20] = 0.018883739613374905;
w[21] = 0.019653087494435306;
w[22] = 0.020403232646209433;
w[23] = 0.021133442112527642;
w[24] = 0.02184300241624739;
w[25] = 0.022531220256336273;
w[26] = 0.023197423185254122;
w[27] = 0.023840960265968206;
w[28] = 0.02446120270795705;
w[29] = 0.02505754448157959;
w[30] = 0.02562940291020812;
w[31] = 0.02617621923954568;
w[32] = 0.026697459183570963;
w[33] = 0.02719261344657688;
w[34] = 0.027661198220792388;
w[35] = 0.028102755659101173;
w[36] = 0.028516854322395098;
w[37] = 0.028903089601125203;
w[38] = 0.029261084110638277;
w[39] = 0.02959048805991264;
w[40] = 0.029890979593332831;
w[41] = 0.03016226510516914;
w[42] = 0.03040407952645482;
w[43] = 0.03061618658398045;
w[44] = 0.03079837903115259;
w[45] = 0.030950478850490988;
w[46] = 0.031072337427566517;
w[47] = 0.031163835696209907;
w[48] = 0.03122488425484936;
w[49] = 0.03125542345386336;
w[50] = 0.031255423453863357;
w[51] = 0.03122488425484936;
w[52] = 0.0311638356962099068;
w[53] = 0.031072337427566517;
w[54] = 0.030950478850490988;
w[55] = 0.03079837903115259;
w[56] = 0.030616186583980449;
w[57] = 0.03040407952645482;
w[58] = 0.0301622651051691449;
w[59] = 0.02989097959333283;
w[60] = 0.029590488059912643;
w[61] = 0.029261084110638277;
w[62] = 0.028903089601125203;
w[63] = 0.0285168543223951;
w[64] = 0.02810275565910117;
w[65] = 0.02766119822079239;
w[66] = 0.02719261344657688;
w[67] = 0.02669745918357096;
w[68] = 0.02617621923954568;
w[69] = 0.025629402910208116;
w[70] = 0.02505754448157959;
w[71] = 0.024461202707957053;
w[72] = 0.02384096026596821;
w[73] = 0.023197423185254122;
w[74] = 0.0225312202563362727;
w[75] = 0.021843002416247386;
w[76] = 0.02113344211252764;
w[77] = 0.020403232646209433;
w[78] = 0.019653087494435306;
w[79] = 0.0188837396133749046;
w[80] = 0.018095940722128117;
w[81] = 0.017290460568323582;
w[82] = 0.016468086176145213;
w[83] = 0.015629621077546003;
w[84] = 0.0147758845274413;
w[85] = 0.013907710703718773;
w[86] = 0.01302594789297154;
w[87] = 0.0121314576629795;
w[88] = 0.01122511402318598;
w[89] = 0.01030780257486897;
w[90] = 0.00938041965369446;
w[91] = 0.008443871469668971;
w[92] = 0.007499073255464712;
w[93] = 0.00654694845084532;
w[94] = 0.005588428003865515;
w[95] = 0.00462445006342212;
w[96] = 0.003655961201326375;
w[97] = 0.002683925371553482;
w[98] = 0.001709392653518105;
w[99] = 7.3463449050567E-4;
x[0] = -0.999713726773441234;
x[1] = -0.998491950639595818;
x[2] = -0.996295134733125149;
x[3] = -0.99312493703744346;
x[4] = -0.98898439524299175;
x[5] = -0.98387754070605702;
x[6] = -0.97780935848691829;
x[7] = -0.97078577576370633;
x[8] = -0.962813654255815527;
x[9] = -0.95390078292549174;
x[10] = -0.94405587013625598;
x[11] = -0.933288535043079546;
x[12] = -0.921609298145333953;
x[13] = -0.90902957098252969;
x[14] = -0.895561644970726987;
x[15] = -0.881218679385018416;
x[16] = -0.86601468849716462;
x[17] = -0.849964527879591284;
x[18] = -0.833083879888400824;
x[19] = -0.815389238339176254;
x[20] = -0.79689789239031448;
x[21] = -0.77762790964949548;
x[22] = -0.757598118519707176;
x[23] = -0.736828089802020706;
x[24] = -0.715338117573056447;
x[25] = -0.69314919935580197;
x[26] = -0.670283015603141016;
x[27] = -0.64676190851412928;
x[28] = -0.622608860203707772;
x[29] = -0.59784747024717872;
x[30] = -0.57250193262138119;
x[31] = -0.546597012065094168;
x[32] = -0.520158019881763057;
x[33] = -0.493210789208190934;
x[34] = -0.465781649773358042;
x[35] = -0.437897402172031513;
x[36] = -0.409585291678301543;
x[37] = -0.380872981624629957;
x[38] = -0.351788526372421721;
x[39] = -0.322360343900529152;
x[40] = -0.292617188038471965;
x[41] = -0.26258812037150348;
x[42] = -0.23230248184497397;
x[43] = -0.201789864095735997;
x[44] = -0.171080080538603275;
x[45] = -0.140203137236113973;
x[46] = -0.109189203580061115;
x[47] = -0.0780685828134366367;
x[48] = -0.046871682421591632;
x[49] = -0.015628984421543083;
x[50] = 0.0156289844215430829;
x[51] = 0.046871682421591632;
x[52] = 0.078068582813436637;
x[53] = 0.109189203580061115;
x[54] = 0.140203137236113973;
x[55] = 0.171080080538603275;
x[56] = 0.201789864095735997;
x[57] = 0.23230248184497397;
x[58] = 0.262588120371503479;
x[59] = 0.292617188038471965;
x[60] = 0.322360343900529152;
x[61] = 0.351788526372421721;
x[62] = 0.380872981624629957;
x[63] = 0.409585291678301543;
x[64] = 0.437897402172031513;
x[65] = 0.465781649773358042;
x[66] = 0.49321078920819093;
x[67] = 0.520158019881763057;
x[68] = 0.546597012065094168;
x[69] = 0.572501932621381191;
x[70] = 0.59784747024717872;
x[71] = 0.622608860203707772;
x[72] = 0.64676190851412928;
x[73] = 0.670283015603141016;
x[74] = 0.693149199355801966;
x[75] = 0.715338117573056447;
x[76] = 0.736828089802020706;
x[77] = 0.75759811851970718;
x[78] = 0.77762790964949548;
x[79] = 0.79689789239031448;
x[80] = 0.81538923833917625;
x[81] = 0.833083879888400824;
x[82] = 0.849964527879591284;
x[83] = 0.866014688497164623;
x[84] = 0.881218679385018416;
x[85] = 0.89556164497072699;
x[86] = 0.90902957098252969;
x[87] = 0.921609298145333953;
x[88] = 0.933288535043079546;
x[89] = 0.94405587013625598;
x[90] = 0.953900782925491743;
x[91] = 0.96281365425581553;
x[92] = 0.970785775763706332;
x[93] = 0.977809358486918289;
x[94] = 0.983877540706057016;
x[95] = 0.98898439524299175;
x[96] = 0.99312493703744346;
x[97] = 0.99629513473312515;
x[98] = 0.998491950639595818;
x[99] = 0.99971372677344123;

from scipy.special import *
from scipy.linalg import *
from scipy.optimize import *

#--------------------------------------------------
def myGamma(l,x):
    return gamma(l)*gammaincc(l,x)
#--------------------------------------------------
def intAllMat(l,a):
    m = np.zeros((a.shape[0],a.shape[0]))
    m[:,:] = a
    m = m + m.transpose()
    return 0.5*gamma(l + 3.0/2.0)*m**(-l-3.0/2.0)
#--------------------------------------------------
def intAllSqr(l,a):
    return 0.5*gamma(l + 3.0/2.0)*(2*a)**(-l-3.0/2.0)
#--------------------------------------------------
def intPartSqr(l,a,x):
    return x**(2*l - 1)/2./(2*a)**2*(2*a*x**2)**(0.5 - l)*(gamma(l + 3.0/2.0) - myGamma(l + 3.0/2.0,2*a*x**2))
#--------------------------------------------------
def minimizeMe(alpha,l,x):
    return np.abs(intPartSqr(l,alpha,x)/intAllSqr(l,alpha) - .99)
#--------------------------------------------------
def findAlpha(l,a, alphaSpace):
    alphas = np.zeros(a.shape[0])
    for i,j in enumerate(a):
      initG = alphaSpace[np.argmin(minimizeMe(alphaSpace,l,j))]
      alphas[i] = fmin(minimizeMe, x0=initG, args=(l,j), disp=False)
    return alphas
#--------------------------------------------------
def getOrthNorm(X):
    x = sqrtm(pinv(X))
    return x
#--------------------------------------------------
def getBasisFuncSing(rcut, n):
    a = np.linspace(1,rcut,n)
    alphasFull = np.array([])
    betas = np.array([])
    betasFull = np.array([])
    alphaSpace = np.array([])
    val = 0.00001
    for i in range(1100):
        val = val*1.015
        alphaSpace = np.append(alphaSpace, val)
    for l in range(0,1):
       alphas = findAlpha(l,a, alphaSpace)
       betas = getOrthNorm(intAllMat(l,alphas))
       alphasFull = np.append(alphasFull, alphas)
       betasFull  = np.append(betasFull , betas)
    return  alphasFull, betasFull
#---------------------------------------------------
def getGns(rCut,nMax,functionList=[]):
  alphas, betas = getBasisFuncSing(rCut, nMax)
  rCutVeryHard= rCut+5.0;
##  functionList = [lambda x: np.exp(-x*x), lambda x: np.exp(-2*x*x)]
#  x = np.linspace(0.01,10,100)
  if not functionList:
    # print(rCut,nMax)

    # print("alphas", alphas)
    # print("betas", betas)
    basisFunctions = []
    for i in range(nMax):
      basisFunctions.append(lambda x, i=i: np.exp(-alphas[i]*x*x))

    functionList = basisFunctions
  else:
      if nMax != len(functionList):
          print("nMax Doesn't match number of functions!")
          exit(1)

  mat = np.zeros([nMax,nMax]);
  gss = np.zeros([nMax,len(x)]);
#  print("nMax",nMax)
  rx = 0.5*rCutVeryHard*(x + 1);

  y = np.zeros([nMax,len(rx)]);
  for i in range(0,nMax):
    y[i,:] = functionList[i](rx);

  for i in range(0,nMax):
    for j in range(0,nMax):
      mat[i,j] = rCutVeryHard*0.5*np.sum(w*rx*rx*y[i,:]*y[j,:]);

#  print("M:",mat)
  invMat = sqrtm(pinv(mat));
#  print("invmat",invMat)
#  print("inv:", invMat)
  for n in range(0,nMax):
    for a in range(0,nMax):
      gss[n,:] = gss[n,:] + invMat[n,a]*y[a,:]

  for i in range(nMax):
    plt.plot(x,gss[i])


  return nMax,rx,gss
#---------------------------------------------------
##def getGTOs(rCut,nMax):
##  rCutVeryHard= rCut*2.0; # This is only for numerical reasons
##  alphas, betas = getBasisFuncSing(2.0000, nMax)
##  betas = betas.reshape([nMax,nMax])
##
##  nMax = len(functionList);
##  mat = np.zeros([nMax,nMax]);
##  gss = np.zeros([nMax,len(x)]);
##
##  rx = 0.5*rCutVeryHard*(x + 1);
##
##  y = np.zeros([nMax,len(rx)]);
##  for i in range(0,nMax):
##    y[i,:] = functionList[i](rx);
##
##  for i in range(0,nMax):
##    for j in range(0,nMax):
##      mat[i,j] = rCutVeryHard*0.5*np.sum(w*rx*rx*y[i,:]*y[j,:]);

##  print("M:",mat)
##  invMat = sqrtm(inv(mat));
##  print("inv:", invMat)
##  for n in range(0,nMax):
##    for a in range(0,nMax):
##      gss[n,:] = gss[n,:] + invMat[n,a]*y[a,:]
##
##  return nMax,rx,gss
#------Out of Stack Memory-------------------------------------------
###def getGTOs(rCut,nMax):
##  np.set_printoptions(precision=32)
##  sys.setrecursionlimit(100000)
###  alphas, betas = getBasisFuncSing(rCut, nMax)
###  print("alphas", alphas)
###  betas = betas.reshape([nMax,nMax])
###  basisFunctions = []
###  for i in range(nMax):
###    basisFunctions.append(lambda x: np.exp(-alphas[i]*x*x))
###  nMax,rx,gss = getGns(rCut, basisFunctions)
###  return nMax,rx,gss

if __name__=="__main__":
    nMax,rx,gss=getGns(2.0,10)
    plt.show()

## example nMax, rx, gss = getGns([np.exp, np.sin, ...., np.cos])
