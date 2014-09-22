%%
clear;
clc;
close all;
%%
[count, exchange] = textread('./pattern.txt', '%n%s');
type = unique(exchange);

m = length(count);
n = length(type);
eachcount = zeros(m,n);
ymax = max(count);
figure;
%hold all;
for i = 1:n
    idx = (strcmp(exchange, type(i))==1);
    eachcount(:,i) = count .* idx; % col-vector
    subplot(2, ceil(n/2), i);
    plot(eachcount(:,i), 'color', rand(1,3));%generate random color 
    %plot(eachcount(:,i), 'color',[1-i/n, i/n, 1-i/n]);% deterministic 
    %hold on;
    title(type(i),'interpreter', 'none');
    xlabel('t');
    ylabel('count');  
    ylim([0, ymax]);
end

%subplot(2, ceil((n+1)/2), i+1);
figure;
bar(eachcount); % control color with colormap and FaceVertexCData
legend(type,'interpreter', 'none');% display the underscore("_") 
title('Exchange sequence');
xlabel('t');
ylabel('count');


% figure;
% bar(eachcount')
% set(gca, 'XTickLabel',type)


%%
%x = 1:size(count);
%gscatter(x, count, exchange);
% figure
% hold all
% for i = 1:size(type)
%     idx = (strcmp(exchange, type(i))==1);
%     plot(x, count .* idx)
%     
% end    
% legend('show')