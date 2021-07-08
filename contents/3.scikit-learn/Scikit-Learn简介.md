# Scikit-Learn简介

> 编辑日期：2021-07-08
>
> 代码验证环境：python 3.7.10 + jupyter lab
>
> 操作系统：OSX 11.4



Scikit-Learn包提供了多种机器学习算法和模型（称为estimators），用法也很简单，一般使用`fit()`训练数据，使用`predict()`预测新样本，下面是一个简单的Demo：

```python
# 导入机器学习算法：随机森林分类器
from sklearn.ensemble import RandomForestClassifier
# 实例化，配置相关模型参数
clf = RandomForestClassifier(random_state=0)
# 构造一个训练数据，2个样本，每个样本3个特征
X = [[ 1,  2,  3],  
     [11, 12, 13]]
# 样本的类别
y = [0, 1]
# 训练
clf.fit(X, y)
```

`fit()`训练函数一般有两个输入量：

* **训练样本 X：**矩阵结构，X大小一般是 **(样本数量, 样本特征数)**，矩阵中每行代表一个样本，列代表一个特征；
* **样本label y：**也成为**target value**，一般回归任务（regression）y取值为实数，分类任务（classification）y取值为整数（或者其他离散的数据集），而非监督学习任务中，y可以没有值。一般y大小是一个1维的数组，数组的索引与训练样本X的行一一对应；

![](https://enpei-md.oss-cn-hangzhou.aliyuncs.com/img20210708114542.png?x-oss-process=style/wp)



模型训练完成，就可以用来预测新的测试数据：

```python
# 预测一下测试数据的类别
>>> clf.predict(X)
array([0, 1])
# 预测一下测试数据
>>> clf.predict([[4, 5, 6], [14, 15, 16]]) 
array([0, 1])
```







参考资料：

* [Introducing Scikit-Learn](https://jakevdp.github.io/PythonDataScienceHandbook/05.02-introducing-scikit-learn.html)
* [Getting Started](https://scikit-learn.org/stable/getting_started.html)

