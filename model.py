from util import *

def equations_5(x,t,alpha,a,b,c,p,q,noise):
    x1,x2,x3,x4,x5=x
    #R=r*np.maximum((a*np.sin(b*x)+c))
    #dxdt=R*x-(beta*x)*np.dot(alpha,x.T)
    dxdt=[self_grow(x1,t,a,b,c,p[0],q[0],noise)-beta*x1*(alpha[0][0]*x1+alpha[0][1]*x2+alpha[0][2]*x3+alpha[0][3]*x4+alpha[0][4]*x5),
          self_grow(x2,t,a,b,c,p[1],q[1],noise)-beta*x2*(alpha[1][0]*x1+alpha[1][1]*x2+alpha[1][2]*x3+alpha[1][3]*x4+alpha[1][4]*x5),
          self_grow(x3,t,a,b,c,p[2],q[2],noise)-beta*x3*(alpha[2][0]*x1+alpha[2][1]*x2+alpha[2][2]*x3+alpha[2][3]*x4+alpha[2][4]*x5),
          self_grow(x4,t,a,b,c,p[3],q[3],noise)-beta*x4*(alpha[3][0]*x1+alpha[3][1]*x2+alpha[3][2]*x3+alpha[3][3]*x4+alpha[3][4]*x5),
          self_grow(x5,t,a,b,c,p[4],q[4],noise)-beta*x5*(alpha[4][0]*x1+alpha[4][1]*x2+alpha[4][2]*x3+alpha[4][3]*x4+alpha[4][4]*x5),
          ]
    return dxdt

def equations_3(x,t,alpha,a,b,c,p,q,noise):
    x1,x2,x3=x
    dxdt=[self_grow(x1,t,a,b,c,p[0],q[0],noise)-beta*x1*(alpha[0][0]*x1+alpha[0][1]*x2+alpha[0][2]*x3),
          self_grow(x2,t,a,b,c,p[1],q[1],noise)-beta*x2*(alpha[1][0]*x1+alpha[1][1]*x2+alpha[1][2]*x3), 
          self_grow(x3,t,a,b,c,p[2],q[2],noise)-beta*x3*(alpha[2][0]*x1+alpha[2][1]*x2+alpha[2][2]*x3),
        ]
    return dxdt

def equations_1(x,t,alpha,a,b,c,p,q,noise):
    x1=x
    dxdt=self_grow(x1,t,a,b,c,p[0],q[0],noise)-beta*x1*x1
    return dxdt