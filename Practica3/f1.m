function y=f1(f,x,y0,h)
y(1)=y0;
for i=1:(length(x)-1)
y(i+1)=h*feval(f,x(i),y(i))+y(i);
end
end