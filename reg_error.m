path = 'C:\Users\Akhi\Desktop\priyanka\experiment\random\stratified\intersubject'
files=dir(fullfile(path, '*.asc'))
l = size(files)
error = []
for i=1:l(1)
    disp(files(i).name)
    out1  = textread(fullfile(path,files(i).name),'%s', 'delimiter', '\n');
    mat1 = matrix(out1)
       for j=i:l(1)
           disp(files(j).name)
           out2  = textread(fullfile(path,files(j).name),'%s', 'delimiter', '\n');
           mat2 = matrix(out2) 
           [TR,TT,ER] = icp(mat1,mat2,10)
           str_err = strcat(files(i).name,"&",files(j).name,":",num2str(ER(1)))
           error = [error,str_err]
       end
       
end


