import numpy as np
import math
k=1
beta=0.01
h_record=[]
t_record=[]
count=np.zeros(10000)



def make_para(n):
    np.random.seed(10)
    alpha=np.random.randn(n,n)
    # alpha=np.array([[0.1,0.1,0.1],
    #                  [0.1,0.1,0.1],
    #                  [0.1,0.1,0.1]])
    for i in range(n):
         alpha[i][i]=1
    #alpha=abs(alpha)
    #print(alpha)
    #alpha=1
    
    a=np.random.uniform(90,110)# a [90,110]
    b=2*np.pi/12#set T=12, then omega=b=2*pi/T
    c=np.random.uniform(-30,50) # c [90,110]
    #p=np.random.uniform(0,2,size=n)
    #q=np.random.uniform(0,10,size=n)
    
    #p=np.array([30,10,60,60,80])
    p=np.array([30,10,60])
    #p=np.array([30])
    #q=np.array([1,0.2,1.5,0.5,1.2])/12
    q=np.array([1,0.2,1.5])/12
    #q=np.array([1.5])/12
    q=q*2
    #m=np.random.uniform(0,1,size=n)+p #use in the model 2
    x_0=0.2*q/beta
    #x_0[2]=0.5*q[2]/beta
    lam=0.1
    return alpha,a,b,c,x_0,p,q,lam

def relu(x):
    return max(0,x)

def r_function1(p,q,h,a):
    return q*(1/(1+math.e**((p-h))/(100*a))-1/2)

def r_function2(p,q,m,h):
    if h>=p and h<=m:
        return q
    else:
        return 0

# the noise of the rain funtion, use the guassion noise

def make_noise(mu,sigma,step):
    return np.random.normal(mu,sigma,step)

# r(h(t))=q(1/(1+exp(-(h-p))-1/2), represent the self growth
def self_grow(x,t,a,b,c,p,q,noise):
    global k
    if int(t)%12==0 and count[int(t)]==0:
        k=np.random.uniform(0.4,1.2)
        count[int(t)]=1
        #print(k)
    h=relu((a*np.sin(b*t)+c)+noise[int(10*t)])*k
    h_record.append(h)
    t_record.append(t)
    return relu(r_function1(p,q,h,a))*x

#B=|1-\alpha_ij|+|1-\alpha_ji|+\lambda*f(p1,q1,p2,q2)
#and f use the 2 norm

def distance1(i,j,p,q,alpha,lam):
    return abs(1-alpha[i][j])+abs(1-alpha[j][i])+lam*(((p[i]-p[j])**2+(q[i]-q[j])**2)**(1/2))

def distance2(i,j,p,q,m,alpha,lam):
    return abs(1-alpha[i][j])+abs(1-alpha[j][i])+lam*(((p[i]-p[j])**2+(q[i]-q[j])**2+(m[i]-m[j])**2)**(1/2)) 

    