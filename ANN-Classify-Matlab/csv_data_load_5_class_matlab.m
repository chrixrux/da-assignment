clear all, close all, clc


%With the file 'grade_ave.mat* in the same foler, run:
load('grade_ave.mat')

input = gradeave(:, 1:35);
d_o = gradeave(:, 37);

%The file ha the classes stored as 1-5 values. Matlab needs the data to be 
%a certain way to be able to understand that there are 5 classes. We turn,
%say, a 5 into [0,0,0,0,1], so the 5th neneuron is suppose to be trigged on
%and all the other zeroes.

target = zeros(length(d_o), 5);

for i = 1:length(d_o)
    if (d_o(i) == 1) %0-9, FAIL
        target(i,1) = 1;
        target(i,2) = 0;
        target(i,3) = 0;
        target(i,4) = 0;
        target(i,5) = 0;
    elseif d_o(i) == 2 %10-11 E/Sufficient
        target(i,1) = 0;
        target(i,2) = 1;
        target(i,3) = 0;
        target(i,4) = 0;
        target(i,5) = 0;
    elseif d_o(i) == 3 %12-13 D/Satisf.
        target(i,1) = 0;
        target(i,2) = 0;
        target(i,3) = 1;
        target(i,4) = 0;
        target(i,5) = 0;
    elseif d_o(i) == 4 %14-15 C/Good
        target(i,1) = 0;
        target(i,2) = 0;
        target(i,3) = 0;
        target(i,4) = 1;
        target(i,5) = 0;
    elseif d_o(i) == 5  %A&B/Excellent&verygood
        target(i,1) = 0;
        target(i,2) = 0;
        target(i,3) = 0;
        target(i,4) = 0;
        target(i,5) = 1;
    else
        disp('Error!')
        disp(d_o(i));
    end
end
