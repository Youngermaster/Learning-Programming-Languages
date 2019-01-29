for j = 1:1000
    u = rand(j,1)
    pause(0.1)
    hist(u)
end

u = rand(10000,1);
hist(u)