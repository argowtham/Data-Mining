
## Building a decision tree model
# Loading the required libraries
library(caret)
library(rpart)
library(rpart.plot)

set.seed(123)

# Loading the data
path = "D:/Datasets/IBM Attrition"
filename = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
ibm = read.csv(paste(path, filename, sep = "/"), header = T)

drop_feats = c("EmployeeCount", "EnvironmentSatisfaction" , "StandardHours", "Over18")
ibm = ibm[ , !(names(ibm) %in% drop_feats)]

# Dimensions of the data set
n = nrow(ibm)
d = ncol(ibm)

# Splitting the train and test data
# Making an 80-20 split for test and train

# # Method 1 - Random Sampling
# traindata = ibm[sample(n, 0.8*n),]

# Method 2 - Down Sampling
# Splitting the data into train and test data
ibmsplit = split(ibm, ibm$Attrition)
ntrue = nrow(ibmsplit$Yes)   # Number of examples from positive class - Attrition = "Yes"
nfalse = nrow(ibmsplit$No)  # Number of examples from negative class - Attrition = "No"
traindata = rbind(ibmsplit$No[sample(nrow(ibmsplit$No), 150),], ibmsplit$Yes[sample(nrow(ibmsplit$Yes), 144),])

# test data - data not availabe in the train data
test = ibm[ !(row.names(ibm) %in% row.names(train)), ]

# Developing the decision tree model based on the training data
model = rpart(traindata$Attrition~., data = traindata, parms = list(split = 'information'), method = "class")
prunedmodel = prune(model, cp = 0.03)
rpart.plot(prunedmodel)
# printcp(model)
# printcp(prunedmodel)

ypred = predict(prunedmodel, newdata = test, type = "class")
ytest = test$Attrition
cf = confusionMatrix(ytest, ypred)
# print(cf)
# print(roc(as.numeric(ytest), as.numeric(ypred)))
# plot(roc(as.numeric(ytest), as.numeric(ypred)))