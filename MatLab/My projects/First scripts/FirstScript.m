1 + 1

% This is a comment

notas=2.8+0.5*randn(100,1) % This is a simulation of the notes in the subject stadistics
life=-70*log(rand(100,1))

% Medidas de tendencia central.

mediaN=mean(notas) % This the mean of the notes
medianaN=median(notas) % This is a median
modaN=mode(notas) % This is the mode of the notes
mediaRecortadaN=trimmean(notas,10) % This is a trim mean

modaV=mode(life)
mediaV=mean(life)
mediarecortadaV=trimmean(life,10)
medianV=median(life)

%----------------------------------------------------------%
% Medidas de variabilidad o disperción.

variaza=var(notas) % La variaza
desva.Tipica=std(notas)
