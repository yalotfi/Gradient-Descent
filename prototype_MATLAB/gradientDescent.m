function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
    %GRADIENTDESCENT Performs gradient descent to learn theta
    %   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
    %   taking num_iters gradient steps with learning rate alpha

    % Initialize parameters
    m = length(y); % number of training examples
    J_history = zeros(num_iters, 1); %Keep track of each gradient step for plotting

    for iter = 1:num_iters
        % Compute partial derivative of given theta each step until convergence
        theta = theta - (alpha/m) * (X' * (X * theta - y));

        % Save the cost J in every iteration    
        J_history(iter) = computeCost(X, y, theta);
    end
end
