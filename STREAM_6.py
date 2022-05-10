import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import math as M

st.title('Определение критических частот вращения ротора в соотвествии с допустимыми вибрациями')
st.subheader('Выполнили Фонов А.М. и Луговых Т.А')

st.write('_Конструкция ротора_')

z = st.number_input('Количество ступеней z', value = 9)
drs = 1085
rrs = drs/2

d_val = 540
r_val = d_val/2

d_st = 820
r_st = d_st/ 2

r_r = 410
r_r2 = r_val - 160

fig = plt.figure()

plt.plot([0,0],[0,rrs],c="g")
plt.plot([0,120],[rrs,rrs],c="g")
plt.plot([120,120],[rrs,0],c="g")
plt.plot([120,240],[r_val,r_val],c="g")
plt.plot([0,-540],[r_val,r_val],c="g")
n1 = 0
n2 = 0
k = 1

for i in range(z-1):
  if i % 2 != 0:
    plt.plot([240+n1,360+n1],[r_val,r_val],c="g")
    plt.plot([360+n1,360+n1],[0,r_r],c="g")
    plt.plot([360+n1,420+n1],[r_r,r_r],c="g")
    plt.plot([420+n1,420+n1],[r_r,0],c="g")
    n1 = n1 + 180
  else:
    plt.plot([-540-n2,-660-n2],[r_val,r_val],c="g")
    plt.plot([-660-n2,-660-n2],[0,r_r],c="g")
    plt.plot([-660-n2,-720-n2],[r_r,r_r],c="g")
    plt.plot([-720-n2,-720-n2],[r_r,0],c="g")
    n2 = n2 + 180
# Слева
plt.plot([-720-n2+180,-720-n2+180-1440],[r_val,r_val],c="g")
plt.plot([-720-n2+180-1440,-720-n2+180-1440],[r_val,0],c="g")
plt.plot([-720-n2+180-1440,-720-n2+180-1440-480],[r_r2,r_r2],c="g")
plt.plot([-720-n2+180-1440-480,-720-n2+180-1440-480],[r_r2,0],c="g")
# Справа
plt.plot([420+n1-180,420+n1-180+960],[r_val,r_val],c="g")
plt.plot([420+n1-180+960,420+n1-180+960],[r_val,0],c="g")
plt.plot([420+n1-180+960,420+n1-180+960+480],[r_r2,r_r2],c="g")
plt.plot([420+n1-180+960+480,420+n1-180+960+480],[r_r2,0],c="g")

plt.plot([-720-n2+180-1440-480-300,420+n1-180+960+480+300],[0,0],linewidth = '1',c="blue")
plt.grid()

st.pyplot(fig)



st.write('_Масса ротора_')

#Объем диска для регулирующей ступени
d = 1.1
l_1 = 0.015
dk = d-l_1
dval = 0.54
sd_reg = 0.12

Vd_reg = (M.pi/4)*(dk**2-dval**2)*sd_reg

#Объем раб.лопаток для регулирующей ступени
F_atl = 0.000244
b2_reg = 0.03
b2_atl = 0.0259
Delta = 0.003
l2_reg =l_1+Delta
betta_2=15
#'P-23-14A' тип профиля
t2_ = 0.63
b2_mod = 2.59
f2_mod = 2.44
W2_mod = 0.39
beta_inst2 = betta_2-12.5*(t2_-0.75)+20.2
z2 = ((M.pi*d)/(b2_reg*t2_))

Vlop_reg = F_atl*l2_reg*z2*(b2_reg/b2_atl)**2

#Объем бандажа для регулирующей ступени
B2 = b2_reg*M.sin(M.radians(beta_inst2))
B_band = B2+0.01 #м
delta_band = 0.005 #м
dp = d+l2_reg

Vband_reg = B_band*delta_band*M.pi*dp

#Масса диска рег.ступени
rho = 7800 #кг/м3
md_reg = (Vd_reg+Vlop_reg+Vband_reg)*rho





#Объем диска для нерегулирующей ступени
sd_nereg = 0.06
z_nereg = z-1

Vd_nereg = M.pi/4*(dk**2-dval**2)*sd_nereg*z_nereg

#Объем раб.лопаток для нерегулирующей ступени
b2_nereg = 0.05
l_21 = 0.041
l_2z = 0.105
l2_nereg = (l_21+l_2z)/2
d21=0.84
d2z=0.904
z_2z = (M.pi*d2z)/(0.65*b2_nereg)
z_21=(M.pi*d21)/(0.65*b2_nereg)
Z2_sr = (z_21+z_2z)/2

Vlop_nereg = F_atl*l2_nereg*Z2_sr*z_nereg*(b2_nereg/b2_atl)**2

#Объем бандажа для нерегулирующей ступени
B2_ = b2_nereg*M.sin(M.radians(beta_inst2))
B_band_ = B2_+0.01 #м
delta_band_ = 0.005 #м
d21=0.84
d2z=0.904
l_11=0.038
dp1 = d21+l_11
dpz = d2z+l_2z
dp_sr = (dp1+dpz)/2

Vband_nereg = B_band_*delta_band_*M.pi*dp_sr*z_nereg

#Масса диска нерег.ступени
md_nereg = (Vd_nereg+Vlop_nereg+Vband_nereg)*rho

#Масса вала
dsh_right = 0.36
dsh_left = 0.32 #меньше правого
d_otv = 0.1 #м
L2 = 0.48
L3 = 0.36
L4 = 5.16
L_summ = L2+L3+L4
m_val = M.pi/4*((dval**2-d_otv**2)*L4-(dsh_left**2-d_otv**2)*L2-(dsh_right**2-d_otv**2)*L3)*rho
# Определение первой критической частоты
L = (L3/2)+(L2/2)+L4 #м - пролет между осями подшипников
# Средняя изгибная жесткость ротора:
E_sr = 1.8e11
EI = E_sr*(3.14/64)*(dval**4-d_otv**4)


#Масса ротора
m_rot = (m_val+md_nereg+md_reg)
#первая собственная частота вращения ротора на абсолютно
#жестких опорах:
P11 = ((1*3.14)**2)/((L)**2)*((EI/(m_rot/L_summ))**0.5)
#Первая собственная частота вращения ротора как жесткого целого на
#упругих опорах:
P21 = (2/(m_rot*2.5e-9))**0.5
#первая критическая частота вращения ротора:
P1 = (1/((1/P11**2)+(1/P21**2))**0.5)/(2*3.14)
#Вторая собственная частота вращения ротора как жесткого целого на
#абсолютно жестких опорах:
P12 = 4*P11
#Вторая собственная частота вращения ротора как жесткого целого на
#упругих опорах:
P22 = (3**0.5)*(L/L_summ)*P21
#вторая критическая частота вращения ротора:
P2 = (1/((1/P12**2)+(1/P22**2))**0.5)/(2*3.14)
st.write("""Macca вала  
                m_val = %.2f  кг""" % m_val)
st.write("""Macca диска регулирующей ступени  
                md_reg = %.2f  кг""" % md_reg)
st.write("""Macca диска нерегулирующей ступени  
                md_nereg = %.2f  кг""" % md_nereg)
st.write("""Macca ротора  
                m_rot = %.2f  кг""" % m_rot)
st.write("""Первая критическая частота  
                P1 = %.2f  1/с""" % P1)
st.write("""Вторая критическая частота  
                P2 = %.2f  1/с""" % P2)



