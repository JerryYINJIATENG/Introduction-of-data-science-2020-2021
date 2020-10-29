import pandas as pd
from pgmpy.estimators import HillClimbSearch, ExhaustiveSearch
from pgmpy.estimators import BDeuScore, BicScore, K2Score
##结构学习
data = pd.read_csv('data.csv', encoding='gb18030')
df = pd.DataFrame(data)
bic = BicScore(df)
k2 = K2Score(df)
hc = HillClimbSearch(df, scoring_method=bic)
#hc = ExhaustiveSearch(df, k2)
model = hc.estimate()
for ee in model.edges():
    print(ee)



##参数学习
from pgmpy.models import BayesianModel
mod = BayesianModel(model.edges())
mod.fit(df)
for cpd in mod.get_cpds():
    print(cpd)

#print(mod.local_independencies('HA'))

##模型推理
from pgmpy.inference import VariableElimination, BeliefPropagation
cancer_infer = VariableElimination(mod)
q = cancer_infer.query(variables=['HA'])
print(q)

#cancer_infer = BeliefPropagation(mod)
#q = cancer_infer.query(variables=['HA'])
#print(q)




