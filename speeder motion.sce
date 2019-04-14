clear 

xs0 = 0.0
xp0 = 0.0
vs0 = 36
vp0 = 0.0
rtp = 0.0

dt = 0.01
xs(1) = xs0
vp(1) = vp0
xp(1) = xp0
time (1)= 0.0
i = 1

while  (xs(i) > xp(i) | i < 2)
    xs(i+1) = xs(i) + vs0*dt // posição do ladrão
    
    ap      =  7 // aceleração do policial em m/s^2
    vp(i+1) = vp(i) + ap*dt // velocidade do policial
    xp(i+1) = xp(i) + vp(i+1)*dt // posição do policial
   
    time(i+1) = time(i) + dt // tempo de perseguição
    i = i + 1
end

plot(time,xs, 'g')
plot(time,xp, 'r')

disp(xp(i))
disp(time(i))
