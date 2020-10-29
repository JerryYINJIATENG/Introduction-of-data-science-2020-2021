#coding: utf-8
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
#定义模型结构
cancer_model = BayesianModel([
    ('PT', 'HO'), #('party', 'hangover'),
    ('HO', 'SA'),#'hangover', 'smell-alcohol'),
    ('HO', 'HA'), #('hangover', 'headache'),
    ('BT', 'HA'),#'brain-tumor', 'headache'),
    ('BT', 'PX') #('brain-tumor', 'pos-xray'),
])
for e in cancer_model.edges():
    print(e)

#添加概率
cpd_party = TabularCPD(variable='PT',
                       variable_card=2,
                       values=[[0.8], [0.2]])
cpd_braintumor = TabularCPD(variable='BT',
                            variable_card=2,
                            values=[[0.999], [0.001]])
cpd_hangover = TabularCPD(variable='HO',
                          variable_card=2,
                          values=[[1.000, 0.300], [0.000, 0.700]],
                          evidence=['PT'],
                          evidence_card=[2])
cpd_smellalcohol = TabularCPD(variable='SA',
                          variable_card=2,
                          values=[[0.900, 0.200], [0.100, 0.800]],
                          evidence=['HO'],
                          evidence_card=[2])
cpd_posxray = TabularCPD(variable='PX',
                          variable_card=2,
                          values=[[0.990, 0.020], [0.010, 0.980]],
                          evidence=['BT'],
                          evidence_card=[2])
cpd_headache = TabularCPD(variable='HA',
                        variable_card=2,
                        values=[[0.980, 0.100, 0.300, 0.010], [0.020, 0.900, 0.700, 0.990] ],
                        evidence=['HO', 'BT'],
                        evidence_card=[2, 2])

cancer_model.add_cpds(cpd_party, cpd_braintumor, cpd_hangover, cpd_smellalcohol, cpd_posxray, cpd_headache)
for cp in cancer_model.get_cpds():
    print(cp)

#进行预测HA发生的概率
from pgmpy.inference import VariableElimination
cancer_infer = VariableElimination(cancer_model)
q = cancer_infer.query(variables=['HA'])
print(q)
#诊断在某些证据下的概率
#from pgmpy.inference import VariableElimination
cancer_infer = VariableElimination(cancer_model)
q = cancer_infer.query(variables=['BT'], evidence={'PX': 1})
print(q)







