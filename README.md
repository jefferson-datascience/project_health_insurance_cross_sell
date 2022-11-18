# Classificação de Clientes da Empresa Insurance All

<img src="https://github.com/jefferson-datascience/project_health_insurance_cross_sell/blob/main/images/logo.jpg" alt="logo" style="zoom: 80%" />


O objetivo deste projeto é criar um modelo de machine learning que realiza a classificação dos clientes da empresa Insurance All, de tal modo, que retorne uma lista rankeada com os clientes que possuem maior propensão de compra do novo produto que a empresa está oferencendo.

O contexto de negócio é fictício. Todavia, o planejamento, execução, desenvolvimento e implementação da solução seguem todos os passos de um projeto real.

# 1. Questão de Negócio

A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis. Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.

Assim o meu objetivo como Cientista de Dados é propor uma solução que faça com que o time de vendas consiga priorizar as pessoas com maior interesse no novo produto e assim, otimizar a campanha realizando apenas contatos aos clientes mais propensos a realizar a compra.

Além disso, nessa consultoria, eu preciso entregar um relatório contendo algumas análises e respostas às seguintes perguntas:

**1.** Principais Insights sobre os atributos mais relevantes de clientes interessados em adquirir um seguro de automóvel.

**2.** Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel? O time de vendas conseguirá contatar todos esses clientes fazendo 20.000 ligações?

**3.** E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?

**4.** Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?

## Planejamento de Solução
- **Qual é a solução para esse problema?** 
A solução para esse problema é um aprendizado de máquina que realize a classificação do clientes que tem maior propensão de compra desse produto.

- **Como vai ser o produto final?**
  1. Será fornecido um relatório com as questões as perguntas do CEO respondida.
  2. Será fornecido, para a empresa, uma planilha no GoogleSheets com um botão que realiza o rankeamento dos clientes com maior propensão de compra do novo produto, uma vez fornecido os dados para essa planilha. Assim, essa planilha otimiza o processo de prospecçaõ e aumenta a taxa de conversão de novos clientes.

# 2. Premissas de Negócio

- O valor anual do seguro veicular é de Rs 5.000.

## Atributos
|      **ATRIBUTOS**    |                                              **DESCRIÇÃO**                                           |
|-----------------------|------------------------------------------------------------------------------------------------------|
|          **id**       |                                          ID único do cliente                                         |
|      **Gender**       |                                           Gênero do cliente                                          |
|         **Age**       |                                           Idade do cliente                                           |
|  **Driving_License**  |               0 : Cliente não possui a driving license; 1: Cliente possui a driving license          |
|     **Region_Code**   |                                   Código único da região do cliente                                  |
|**Previously_Insured** |                1: Cliente já possui um seguro veicular; 0 : Cliente não tem um seguro veicular       |
|   **Vehicle_Age**     |                                            Idade do veículo                                          |
|   **Vehicle_Damage**  |           1 : Veículo já foi danificado no passado; 0 : Veículo não foi danificado no passado.       |
|   **Annual_Premium**  |                                  Quantidade que o cliente paga de plano anual.                       |
|**PolicySalesChannel** |             Código anônimo de contato com o cliente, ou seja, e-mail, telefone, fax, whats...        |
|  **Vintage_Number**   |                   Quantidade de dias em que o cliente está associado a companhia                     |
|     **Response**      | 1 : Cliente está interessado no seguro veicular; 0 : Cliente não está interessado no seguro veicular |

# 3. Estratégia de Resolução

Para resolver esse problema, nós adotamos a seguinte estratégia:

**Etapa 01 - Descrição dos Dados:** Comprensão dos atributos, analise da dimensão do dados, verificação de dados nulos e estudo da estatística descritiva dos dados numéricos e categóricos.

**Etapa 02 - Feature Engineering:** Criação do Mapa Mental para criar hipóteses e insights e reajuste de variáveis.

**Etapa 03 - Filtragem dos Dados:** Não foi necessário realizar a filtragem. Todos os dados foram utilizados.

**Etapa 04 - Análise Exploratória dos Dados:** Realização da análise univariada de cada variável sobre a variável resposta, análise multivariada para compreender melhor a influência de duas variáveis sobre a variável resposta, validação das hipóteses e resumo dessas três etapas para determinar as variáveis mais importantes para os modelos de machine learning.

**Etapa 05 - Preparação dos Dados:** Padronização e reescala de dados numéricos e encoding de dados categóricos para os modelos a serem avaliados.

**Etapa 06 - Seleção das Features:** Divisão do conjunto de dados em treino, validação e teste, seleção das variáveis mais relevante usando o modelo extratreesclassifier.

**Etapa 07 - Machine Learning Models:** Preparação dos dados de treino, teste e validação com as variáveis mais relevantes obtidos na etapa 06, análise da performance dos modelos escolhidos. As métricas usadas para realizar a análise foram a recall at k, precision at k, c urva lift e curva de ganho cumulativo. E escolha do modelo com melhor performance.

**Etapa 08 - Hyperparameter Fine Tunning:** Refinamento de parêmetros do modelo escolhido na etapa 07 e retreino do modelo com os dados de treino + validação.

**Etapa 09 - Tradução e Interpretação dos Resultados:** Análise da performance do modelo escolhido para saber a capacidade de generalização para dados nunca antes vistos e verificar casos de overfitting. Uma vez verificado a capacidade de generalização. Realizar a análise dos resultados para o negócio respondendo as perguntas do CEO.

**Etapa 10 - Deploy do Modelo para Produção:** Criação da Api, criação da classe responsável pelos principais pontos desse projeto que permitem a implementação no modelo, relização do deploy no Web Service do Heroku.

# 4. Top 3 Insights

**Hipótese 06:** Clientes em que seus veículos já foram danificados aceitam mais o seguro veicular.

**Resposta.** Essa afirmação é verdadeira!

<img src="https://github.com/jefferson-datascience/project_health_insurance_cross_sell/blob/main/images/hipotese_6.png" alt="logo" style="zoom: 80%" />

**Hipótese 07:** Clientes que já possuem algum seguro veicular aceitam menos o seguro de automóvel ofertado.

**Resposta.**  Essa afirmação é verdadeira!

<img src="https://github.com/jefferson-datascience/project_health_insurance_cross_sell/blob/main/images/hipotese_7.png" alt="logo" style="zoom: 80%" />


**Hipótese 09:** Clientes com idade acima de 40 anos aceitam mais o seguro veicular

**Resposta.**  Essa afirmação é verdadeira. Melhor ainda, clientes que estão na faixa de idade de 40 a 50 anos aceitam mais o seguro veicular.

<img src="https://github.com/jefferson-datascience/project_health_insurance_cross_sell/blob/main/images/hipotese_9.png" alt="logo" style="zoom: 80%" />

# 5. Modelos de Machine Learning Utilizados
Para escolher o melhor modelo de Machine Learning par resolver os nosso problema, nós selecionamos:

- KNN 
- XGBClassifier
- ExtraTreesClassifier
- Logistic Regressor
- RandomForestClassifier

## Machine Learning Modelo Performance - CrossValidation

Para analisar a performance do nossos modelos, nós usamos duas métricas que são a precision at k e recall at k, considerando k=40000. 

- A precision at k, para k=40000, nos diz a precisão de acerto, em porcentagem, do modelo dentro de 40.000 linhas.

- A recall at k, para k=40000, nos diz que, para os clientes interessados no produto, qual a porcentagem que o modelo conseuge predizer como interessados os clientes que possuem de fato interesse, dentro de 40.000 linhas.


|       **model_name**          | **precision_at_k_40000** | **recall_at_k_40000** |
|-------------------------------|--------------------------|-----------------------|
|           KNN 	              |           0.140   	     |            0.940      |
|    XGBClassifier Model        |           0.149	         |            1.000      |
|  ExtraTreesClassifier Model   |	          0.148	         |            0.994      |
|    LogisticRegressor Model	  |           0.149	         |            1.000      |
| RandomForestClassifier Model	|           0.149          |	          0.997      |

## Modelo de Machine Learning - XGBClassifier

O modelo escolhido foi o XGBClassifier. Realizado o Hyperparameter Fine Tunning e depois feito um último treino com os dados de treino + validação, realizamos a predição com dados nunca antes vistos pelo modelo. Assim, tivemos a seguinte performance:

|       **model_name**          | **precision_at_k_40000** | **recall_at_k_40000** |
|-------------------------------|--------------------------|-----------------------|
|       XGBClassifier Model 	  |           0.23   	       |            0.993      |

Logo, o nosso modelo teve um ótimo desempenho para dados nunca antes vistos. 


# 7. Interpretação dos Resultados para o Negócio.

Para analisar a performance de negócio, nos usaremos duas métricas que nos permite uma ótmia interpretação voltada para o negócio. Usaremos:
  - Curva de Ganho Cumulativo
 
<img src="https://github.com/jefferson-datascience/project_health_insurance_cross_sell/blob/main/images/cumulative_gains.png" alt="logo" style="zoom: 80%" />

  - Curva Lift
  
<img src="https://github.com/jefferson-datascience/project_health_insurance_cross_sell/blob/main/images/lift_curve.png" alt="logo" style="zoom: 80%" />

**Análise de Performance de Negócio**

**1.** Tomando 40% da minha lista organizada pelo modelo, teremos 95% dos clientes interessados em adquirir o novo produto.

**2.** Tomando 40% da minha lista organizada pelo model, em relação a uma lista organizada de forma aleatória, ela é 2,3 vezes melhor.

## Respondendo as Perguntas do CEO.

**2.** Qual a porcentagem de clientes interessados em adquirir um seguro de automóvel? O time de vendas conseguirá contatar todos esses clientes fazendo 20.000 ligações?

- Em nosso conjunto de teste nós temos aproximadamente 1.77% de clientes interessados em adquirir o seguro de automóvel, ou seja, 2250 clientes de um conjunto de teste possui 127037 clientes.
- Observe que ao realizar 20.000 ligações para os clientes que estão na lista organizada pelo nosso modelo, nós estamos tomando 15% do nosso conjunto de dados. A curva de cumulative gains do nosso modelo diz que se tomarmos 15% do nossos dados, temos em torno de 40% dos clientes interessados. Ou seja, em 20.000 ligações nós vamos conseguir atingir 900 clientes interessados.
- Logo, com a campanha tem a capacidade de 20.000 ligações, teremos um faturamento estimado em Rs 4.500.000;

**3.** E se a capacidade do time de vendas aumentar para 40.000 ligações, qual a porcentagem de clientes interessados em adquirir um seguro de automóvel o time de vendas conseguirá contatar?

-Realizando 40.000 ligações para os clientes que estão na lista organizada pelo nosso modelo, nós estamos tomando 31% do nosso conjunto de dados. A curva de cumulative gains do nosso modelo diz que se tomarmos 32% do nossos dados, temos em torno de 80% dos clientes interessados. Ou seja, em 40.000 ligações nós vamos conseguir atingir 1800 clientes interessados.

- Assim, se a campanha da empresa trabalhar com a capacidade de 40.000 ligações, o faturamento estimado será em torno de Rs 9.000.000;

**4.** Quantas ligações o time de vendas precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro de automóvel?

- Segundo a curva de ganho cumulativo, nós temos que tomar em torno 32% da nossa lista ordenanda para atingir 80% do clientes
interessados, ou seja, temos que realizar em torno de 40.652 ligações.

# 8. Conclusões e Lições Aprendidas

O projeto foi concluído com sucesso com um modelo realiza a classificação dos clientes que tem o maior interesse em adquirir o novo produto fornecido pela empresa e, no fim, foi fornecido uma lista rankeada com os clientes que possuem mais interesse em adquirir o produto.

Para problemas dessa natureza, isto é, problemas de Learning to Rank, é importante realizar uma análise minuciosa das variáveis, de modo que, a relação das variáveis do dataset com a variável resposta nos dê características de discrepância de clientes que possuem interesse para clientes que não possuem interesses, pois dessa forma, o modelo consegue realizar melhor a classificação, assim, aperfeiçoando a sua performance. 
Uma outra conclusão interessante a se fazer é que nesse problema as curvas lift e cumulative gains são extremamente importantes para interpretar os resultados do modelo de aprendizem de máquina para a linguagem dos negócios.

A utilização das métricas corretas para o nosso problema foram essenciais para saber analisar o desempenho. Para o nosso problema, o recall e a precision foram ótima métricas, pois a precision nos dá informação de qual é a capacidade de acerto, no geral, do nosso modelo e o recall nos diz a capacidade do nosso modelo de acerto de clientes que tem interesse no produto.

# 9. Próximos Passos

Os próximos passos desse projeto será:

- Realizar um novo ciclo CRISP-DM para melhorar a performance do modelo investigando e criando novas features.
- Analisar em quais canais de comunicação a empresa tem uma melhor taxa de conversão.
- Após 1 semana do modelo em produção, analisar o desempenho X resultados na prática.
- Treinar a equipe de vendas para usar o modelo.
