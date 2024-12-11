
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


'ano': [2022,2020,2000,2008]
'motor':[1,2.5,1,2]
'preço':[70000,60000,20000,40000]
df = pd.DataFrame(dados)

y = df['preço']
x = df[['motor','ano']]# Seleciona as colunas 'Tempo' e 'qualidade'

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#0.2 indica que 20% vao ser usados para testes e 80% para treino
#random_state=42: Define uma semente para o gerador de números aleatórios, 
#garantindo que a divisão dos dados será a mesma a cada execução.

modelo = LinearRegression()#"cria" oque está prestes a acontecer(instancia)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
print(f"Erro Quadrático Médio: {mean_squared_error(y_test, y_pred)}")
# é comumente usado para verificar a acurácia de modelos e dá um maior peso aos maiores erros

carro = [[2007, 2.5]]
previsao = modelo.predict(carro)
print(f"O preço do seu carro é de: {previsao[0]:.2f}")