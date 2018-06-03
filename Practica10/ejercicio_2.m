%Metodos de diferencias finitas 
% Con condiciones de frontera tipo Robin    

%Definir los vectores y el valor de las particiones
h=0.01;
a=0;
b=0.5;
x=a:h:b;
n=length(x);

A=zeros(n-1,n-1);
for i=2:n-2
    for j=1:n-1
        if i==j
            A(i,j-1)=1;
            A(i,j)=-2;
            A(i,j+1)=1;
        end
    end
end
A(1,1)=-2;
A(1,2)=1;
A(n-1,n-2)=1;
A(n-1,n-1)=-2;


%Crear vector de f

func=zeros(n-1,1);
func(1,1)=-cos(pi*x(2))*pi^2 -1;
for i=3:n-1
    func(i,1)=-cos(pi*x(i))*pi^2;
end
func(n-1,1)=-cos(pi*x(n))*pi^2 +(h*pi);

f=func*h^2;


%La matriz soluci�n!
u= f

