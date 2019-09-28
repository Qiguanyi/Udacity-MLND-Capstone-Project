# Udacity_MLND_Capstone_Project
Udacity_MLND_Capstone_Project

Support vector machine (SVM) is one of the most widely used machine learning methods. Linear support vector machine can solve linear classification problems, kernel support vector machine is mainly for nonlinear classification problems. In this report, we apply support vector machine to multi-factor stock selection, focusing on the following issues:

  1.	Firstly, model selection. Is there any improvement in the performance of support vector machines compared with linear regression models? Does the nonlinear classifier such as polynomial kernel, Sigmoid kernel and Gaussian kernel support vector machine, have advantages in classification performance compared with the linear classifier represented by linear support vector machine? Is there any difference between the predictive ability of support vector regression and support vector classifier?
  2.	Secondly, parameter optimization. SVM depends much more on parameters than generalized linear models. The SVM contains two important parameters: the penalty coefficient C and gamma (γ) value. In the context of the problem of combining multiple factors, what is the most reasonable value of parameters? Which indicators should be used to determine the optimal parameters?
  3.	Finally, portfolio construction. After measuring the performance of different support vector machine models, how to use the prediction results of the model to construct a strategy combination for back-test? What are the similarities and differences of stock selection effect of each model in CSI 300, CSI 500 and all A-share pools?

# Data Set
A-share constituent stocks, excluding. The ST shares, stocks suspended in the next trading day of each cross-section period and the stocks listed within 3 months were excluded.

# Key Files
The main functions are in following files:
  1. CustomizedFunctions.py: Customized Defination of Functions
  2. database_api.py: ectracting data from SQL database.

The final results of different models are in following html files:
  1. Linear model.html
  2. SVM_linear kernel.html
  3. SVM_poly_3.html
  4. SVM_poly_7.html
  5. SVM_sigmoid.html
  6. SVM_Gaussian.html
