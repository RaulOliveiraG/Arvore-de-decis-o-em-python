
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


'tamanho': [22,9,19,16]
'tempo':[2,40,10,15]
'qualidade':[3,5,8,10]
df = pd.DataFrame(dados)

y = df['qualidade']
x = df[['tempo','tamanho']]# Seleciona as colunas 'Tempo' e 'qualidade'

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#0.2 indica que 20% vao ser usados para testes e 80% para treino
#random_state=42: Define uma semente para o gerador de números aleatórios, 
#garantindo que a divisão dos dados será a mesma a cada execução.

modelo = LinearRegression()#"cria" oque está prestes a acontecer(instancia)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
print(f"Erro Quadrático Médio: {mean_squared_error(y_test, y_pred)}")
# é comumente usado para verificar a acurácia de modelos e dá um maior peso aos maiores erros

pika = [[4, 20]]
previsao = modelo.predict(pika)
print(f"A qualidade da tua pika é: {previsao[0]:.2f}")