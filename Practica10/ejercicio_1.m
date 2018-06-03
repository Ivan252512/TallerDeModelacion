% Metodos de diferencias finitas 
% Con condiciones de frontera tipo Dirichlet 

%Definir los vectores y el valor de las particiones
h=0.01;
a=0;
b=1;
x=a:h:b;
n=length(x);

A=zeros(n-2,n-2);
for i=2:n-3
    for j=1:n-2
        if i==j
            A(i,j-1)=-1;
            A(i,j)=2+h^2;
            A(i,j+1)=-1;
        end
    end
end
A(1,1)=2+h^2;
A(1,2)=-1;
A(n-2,n-3)=-1;
A(n-2,n-2)=2+h^2;


%Crear vector de soluciones)
f=zeros(n-2,1);
for i=1:n-2
    for j=1
        if i==n-2
            f(i,1)=1;
        end
    end
        
end

size(f);

%La matriz soluci�n!
u= inv(A)*f

