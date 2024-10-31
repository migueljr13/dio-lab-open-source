# Transformação de Dados

Este documento descreve as etapas realizadas para transformar e integrar dados de diversas tabelas relacionadas a funcionários, departamentos e gerentes. As transformações visam padronizar cabeçalhos, ajustar dados e estruturar relacionamentos para facilitar consultas e análises futuras.

## Sumário
1. [Padronização de Cabeçalhos](#padronização-de-cabeçalhos)
2. [Ajustes em Tipos de Dados](#ajustes-em-tipos-de-dados)
3. [Transformação e Separação de Endereços](#transformação-e-separação-de-endereços)
4. [Drill-Down e Unificação de Localização](#drill-down-e-unificação-de-localização)
5. [Criação de Tabelas Unificadas](#criação-de-tabelas-unificadas)
6. [Seleção de Campos Relevantes](#seleção-de-campos-relevantes)
7. [Mesclagem de Funcionário e Gerente](#mesclagem-de-funcionario-e-gerente)
8. [Remoção de Dados Redundantes e Colunas Não Utilizadas](#remoção-de-dados-redundantes-e-colunas-não-utilizadas)

---

### 1. Padronização de Cabeçalhos
   - **Descrição**: Padronizado os nomes das colunas usando sufixos específicos para cada entidade, como `_depto`, `_func`, `_depend`, `_end`, `_prod` e `_proj`, que representam respectivamente departamento, funcionário, dependente, endereço, produto e projeto.
   - **Detalhe**: Colunas específicas foram renomeadas para melhor entendimento, como:
     - `mngr` → `gerente`
     - `ssn` → `matricula`
     - `data_nasc` → `data_nascimento`

### 2. Ajustes em Tipos de Dados
   - **Descrição**: O campo `salario` foi transformado para um tipo decimal fixo com duas casas decimais.
   - **Objetivo**: Garantir a precisão nas operações financeiras e uniformidade nas consultas.

### 3. Transformação e Separação de Endereços
   - **Descrição**: O campo de endereço na tabela `employee` foi dividido em colunas mais específicas, incluindo `numero`, `logradouro`, `cidade` e `estado`.
   - **Objetivo**: Facilitar consultas baseadas em componentes individuais do endereço.

### 4. Drill-Down e Unificação de Localização
   - **Descrição**: Na tabela de `departamento`, foi realizado um drill-down nos dados de localização, mesclando `nome_depto` e `local_depto` para torná-los únicos.
   - **Objetivo**: Evitar duplicidades e facilitar a identificação de departamentos com base na localização.

### 5. Criação de Tabelas Unificadas
   - **Descrição**: Mesclado as tabelas `employee` e `departamento` usando uma junção externa esquerda com base no campo `numero_depto`.
   - **Nova Tabela**: A tabela resultante foi renomeada para `funcionario_departamento`.
   - **Campos Selecionados**:
     - Incluem `matricula_func`, `nome_func`, `salario`, `matricula_mngr_func`, `numero_depto`, `nome_depto`, e `matricula_mngr_depto`.
   - **Objetivo**: Centralizar as informações de funcionários e seus departamentos.

### 6. Seleção de Campos Relevantes
   - **Descrição**: Reduzido a quantidade de colunas na tabela `funcionario_departamento` para focar em informações essenciais de funcionários e gerentes.
   - **Campos Mantidos**: Foram mantidos apenas os campos necessários para relacionamentos e consultas frequentes.

### 7. Mesclagem de Funcionário e Gerente
   - **Descrição**: Mesclado a tabela `employee` consigo mesma usando uma junção externa esquerda, criando uma nova consulta chamada `funcionario_gerente`, com base nos campos `matricula_mngr` e `matricula`.
   - **Campos Selecionados**: Foram mantidos apenas `nome` e `matricula`, tanto para funcionário quanto para gerente.
   - **Objetivo**: Destacar as relações entre funcionários e seus respectivos gerentes.

### 8. Remoção de Dados Redundantes e Colunas Não Utilizadas

   - **Descrição**: Removido linha inferior, como o funcionário não tem um gerente .
   - **Objetivo**: Otimizar a estrutura dos dados, eliminando redundâncias que não agregam valor às análises.

### 9. Nova consulta de Funcionário
   - **Descrição**: identificar os gerentes de cada funcionário cadastrado.

   - **Objetivo**: Possibilidade de otimização dos dados com esta consulta.

   - **Consulta**: 
 ```
  count(*) as total_employees
  from employee e
  left join employee e2 on e.Super_ssn = e2.Ssn
  where e.Super_ssn is not null
  group by e.Super_ssn;
 ```
---

### Observações Finais
Essas transformações foram realizadas para simplificar e otimizar a consulta e análise de dados entre funcionários, departamentos e gerentes, facilitando a geração de relatórios e o entendimento das hierarquias na empresa.

