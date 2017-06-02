# Setting the path of the file
path = "D:/Datasets/IBM Attrition"
filename = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
ibm = read.csv(paste(path, filename, sep = "/"), header = T)

set.seed(123)

# Loading the required packages
library(randomForest)
library(pROC)

# Splitting the train and test data
# Making an 80-20 split for test and train

# # Method 1 - Random Sampling
# traindata = ibm[sample(n, 0.8*n),]

# Method 2 - Down Sampling
# Splitting the data into train and test data
ibmsplit = split(ibm, ibm$Attrition)
ntrue = nrow(ibmsplit$Yes)   # Number of examples from positive class - Attrition = "Yes"
nfalse = nrow(ibmsplit$No)  # Number of examples from negative class - Attrition = "No"
train = rbind(ibmsplit$No[sample(nrow(ibmsplit$No), 150),], ibmsplit$Yes[sample(nrow(ibmsplit$Yes), 144),])

# test data - data not availabe in the train data
test = ibm[!(row.names(ibm) %in% row.names(train)), ]

ytrain = train$Attrition
ytest = test$Attrition

drop_feats = c("Attrition", "EmployeeCount", "EmployeeNumber", "EnvironmentSatisfaction" , "StandardHours", "Over18")

xtrain = train[ , !(names(train) %in% drop_feats)]
xtest = test[ , !(names(test) %in% drop_feats)]

# tuneRF(xtrain, ytrain)

# Building the model
model = randomForest(xtrain, y = ytrain, classwt = c(1, 1.25), nodesize = 15, mtry = 3)
#print(model)

ypred = predict(model, newdata = test, type = "response")
cf = confusionMatrix(ytest, ypred)
#print(cf)
aucroc = roc(as.numeric(ytest), as.numeric(ypred))

# varImpPlot(model)
