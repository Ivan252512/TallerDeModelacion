h=0.01;
x0=0;
xf=5;
x=x0:h:xf;
f=inline('sin(x.^2)','x','y');
y0=1; %Cond. inicial
sol=zeros(1,length(x));
sol=f1(f,x,y0,h)
plot(x,sol)
