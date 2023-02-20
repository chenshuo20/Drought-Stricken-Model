from scipy.integrate import odeint
import math
import numpy as np
import matplotlib.pyplot as plt
from model import *
from util import *
'''
odes dx_i/dt=r_i*x_i-beta_i*x_i(x_i+alpha_ij*x_j) j!=i
r(h(t))

'''


#represent the interact by others
#-beta*x_i*(x_i+alpha_ij*x_j),j != i
def config_parser():
    import configargparse
    parser=configargparse.ArgumentParser()
    parser.add_argument('--species_number',type=int,
                        help='The number of the species, we provide 3 and 5 now. To add more choice, you can add functions in the model.')
    
    #paraments
    parser.add_argument('--beta',type=float,default=0.01,
                        help='parament beta.')
    
    return parser

if __name__=='__main__':
    #parser=config_parser()
    #args=parser.parser_args()
    
    #solve equation
    noise=make_noise(0,20,10000)
    alpha,a,b,c,x_0,p,q,lam=make_para(3)
    t=np.linspace(0,96,9601)
    solve=odeint(equations_3,x_0,t,args=(alpha,a,b,c,p,q,noise))
    
    #draw the graph
    #plt.plot(t,r[0]*)
    plt.plot(t,solve[:,0],color='r',label='x1')
    plt.plot(t,solve[:,1],color='g',label='x2')
    plt.plot(t,solve[:,2],color='b',label='x3')
    #plt.plot(t,solve[:,3],color='c',label='x4')
    #plt.plot(t,solve[:,4],color='k',label='x5')
    plt.plot(t,solve[:,0]+solve[:,1]+solve[:,2],color='y',label='y')
    h_record=np.array(h_record)
    
    plt.plot(t_record,h_record/100,color='k')
    plt.xlabel('t')
    plt.grid()
    
    '''draw the r-h graph
    h=np.linspace(0,100,1000)
    r1=r_function1(p[0],q[0],h,a)
    r2=r_function1(p[1],q[1],h,a)
    r3=r_function1(p[2],q[2],h,a)
    plt.plot(h,r1,color='r',label='r1')
    plt.plot(h,r2,color='b',label='r2')
    plt.plot(h,r3,color='g',label='r3')
    plt.xlabel('h')
    plt.grid()
    '''
    

    plt.savefig("test.png")
    
    #calculate biodiversity
    B=0
    for i in range(3):
        for j in range(3):
            B+=distance1(i,j,p,q,alpha,lam)
    print(B)
