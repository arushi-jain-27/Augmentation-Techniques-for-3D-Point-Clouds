function [mat] = matrix(out)
m = size(out);
m = m(1);
mat = zeros(3,m);
for i = 1 : m
    out1 = split(out{i});
    for j = 1 : 3
        mat(j,i) = str2double(out1(j));
    end
end
    

