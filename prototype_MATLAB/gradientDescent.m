function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
    %GRADIENTDESCENT Performs gradient descent to learn theta
    %   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
    %   taking num_iters gradient steps with learning rate alpha

    % Initialize parameters
    m = length(y); % number of training examples
    J_history = zeros(num_iters, 1); %Keep track of each gradient step
    
    % Add intercept column of ones to x
    X = [ones(m, 1), X(:, 1)];

    for i = 1:num_iters
        % Compute partial derivative of given theta at each step
        theta = theta - (alpha/m) * (X' * (X * theta - y));

        % Save the cost J at every gradient(i) until converged 
        J_history(i) = computeCost(X, y, theta);
    end
end
