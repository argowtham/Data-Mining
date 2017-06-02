library(rpart)
library(caret)

# Setting the path of the file
path = "D:/Datasets/IBM Attrition"
filename = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
ibm = read.csv(paste(path, filename, sep = "/"), header = T)

train = ibm[sample(nrow(ibm), 900),]


# # Splitting the data into train and test data
# ibmsplit = split(ibm, ibm$Attrition)
# train = rbind(ibmsplit$No[sample(nrow(ibmsplit$No), 50),], ibmsplit$Yes[sample(nrow(ibmsplit$Yes), 50),])
# 
# test data - data not availabe in the train data
test = ibm[!(row.names(ibm) %in% row.names(train)), ]

drop_feats = c("EmployeeCount", "EmployeeNumber", "EnvironmentSatisfaction" , "StandardHours", "Over18")
train = train[ , !(names(train) %in% drop_feats)]
test = test[ , !(names(test) %in% drop_feats)]

ytrain = train$Attrition
ytest = test$Attrition

# target = "Attrition"
# 
# xtrain = train[ , !(names(train) %in% target)]
# xtest = test[ , !(names(test) %in% target)]

model = rpart(train$Attrition ~  ., data = train, method ="class",parms = list(split = 'gini'))
ypred = predict(model, newdata = test, type = "class")
print(confusionMatrix(ypred, ytest))