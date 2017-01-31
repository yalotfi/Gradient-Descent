function J = computeCost(X, y, theta)
    %COMPUTECOST Compute cost for linear regression
    %   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
    %   parameter for linear regression to fit the data points in X and y

    % Initialize
    m = length(y); %number of training example
    J = 0; %init cost at 0
    
    % Add intercept column of ones to x
    X = [ones(m, 1), X(:, 1)];
    
    % Vectorized cost function (no loop needed)
    J = 1/(2*m) * sum(((X * theta) - y).^2);
end
