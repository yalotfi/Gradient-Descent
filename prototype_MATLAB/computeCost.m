function J = computeCost(X, y, theta)
    %COMPUTECOST Compute cost for linear regression
    %   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
    %   parameter for linear regression to fit the data points in X and y

    % Initialize
    m = length(y); %number of training example
    J = 0; %init cost at 0

    %cost = 0;

    for i = 1:m
        prediction = X(i, :) * theta;
        sqrErrors = (prediction - y(i)) .^ 2;
        J = J + sqrErrors;
    end
    
    % Compute total cost
    J = 1/(2*m) * J;
end
