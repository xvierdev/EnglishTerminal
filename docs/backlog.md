# Backlog do Projeto - English Terminal

## Visão Geral

Este projeto visa criar um aplicativo interativo para auxiliar no aprendizado de vocabulário em inglês, através da tradução de palavras.

## Requisitos

### A Fazer

| ID | Descrição | Prioridade | Esforço (Pontos) | Critérios de Aceitação | Categoria | Responsável |
|---|---|---|---|---|---|---|
| 2 | Implementar script de atualização automática do aplicativo. | Média | 5 | O aplicativo verifica e instala atualizações automaticamente. | Melhoria | [Nome] |
| 3 | Adicionar modo de jogo para tradução de português para inglês. | Alta | 8 | O jogo apresenta palavras em português e o usuário traduz para inglês. | Funcionalidade | [Nome] |
| 6 | Desenvolver versão web do aplicativo. | Alta | 21 | O aplicativo é acessível através de um navegador, sem necessidade de download. | Funcionalidade | [Nome] |
| 7 | Adicionar modo de jogo tradução de pronomes. | Alta | 5 | O jogo apresenta pronomes em inglês e o usuário traduz para português e vice-versa. | Funcionalidade | [Nome] |
| 8 | Adicionar modo listening para que eu ouça audios e escreva o que eu ouvi. | Média | 13 | O aplicativo apresenta áudios curtos em inglês e o usuário digita o que ouviu. O aplicativo verifica a resposta. | Funcionalidade | [Nome] |

### Concluídos

* **Modos de Jogo Temáticos:**
    * Modo "Dias da Semana": Palavras relacionadas aos dias da semana.
    * Modo "Números": Palavras relacionadas a números.
* **Respostas Flexíveis:** Permitir múltiplas respostas corretas para palavras com múltiplos significados.
* **Registro de Progresso:**
    * Salvar recordes de pontuação em arquivo.
    * Exibir pontuação ao final de cada partida.
* **Logs Detalhados:**
    * Gerar logs com pontuação, data/hora e detalhes de erros (resposta do usuário vs. resposta correta).
* **Banco de Dados de Palavras:** Utilizar uma lista de palavras em inglês para as perguntas.
* **Tradução Interativa:** Apresentar palavras em inglês e capturar a tradução em português.
* **Sistema de Pontuação:** Implementar sistema de pontuação baseado no número de acertos.
* **Permitir entrada de palavras em português sem acentuação.**
* **Criar sistema de autenticação e gerenciamento de perfis de usuário.**
* **Empacotar o projeto Python em um arquivo executável.**

## Melhorias Adicionais

* **Interface do Usuário:** Melhorar a interface para torná-la mais intuitiva e agradável.
* **Desempenho:** Otimizar o código para melhorar o desempenho do aplicativo.
* **Testes:** Implementar testes automatizados para garantir a qualidade do código.
* **Documentação:** Criar documentação completa do projeto.

## Detalhamento e Priorização

### Prioridades

As tarefas foram classificadas em três níveis de prioridade:

*   **Alta:** Tarefas essenciais para o funcionamento básico do aplicativo ou para melhorias significativas na experiência do usuário.
*   **Média:** Tarefas importantes, mas não críticas, que podem ser implementadas em iterações futuras.
*   **Baixa:** Tarefas opcionais ou de menor impacto, que podem ser implementadas quando houver tempo disponível.

### Esforço

O esforço estimado para cada tarefa é medido em pontos, que representam a complexidade e o tempo necessário para sua conclusão.

### Critérios de Aceitação

Os critérios de aceitação definem as condições que devem ser atendidas para que uma tarefa seja considerada concluída.

### Observações

*   A coluna "Responsável" deve ser preenchida com o nome da pessoa responsável por cada tarefa.
*   O backlog está sujeito a alterações e atualizações à medida que o projeto avança.
*   As "Melhorias Adicionais" representam ideias e sugestões que podem ser incorporadas ao projeto no futuro.

## Detalhamento Adicional

**ID 7: Adicionar modo de jogo tradução de pronomes.**

*   **Esforço (Pontos):** 5
    *   *Justificativa:* Requer a criação de um novo modo de jogo, lógica de seleção de pronomes (inglês-português e português-inglês) e interface de interação.
*   **Critérios de Aceitação:**
    *   O jogo deve apresentar pronomes em inglês para serem traduzidos para português.
    *   O jogo deve apresentar pronomes em português para serem traduzidos para inglês.
    *   O jogo deve verificar a resposta do usuário e fornecer feedback imediato (correto/incorreto).
    *   O jogo deve registrar a pontuação do usuário.
    *   Deve haver um conjunto de dados de pronomes em inglês e português a serem utilizados no jogo.
    *   A interface do usuário deve ser clara e intuitiva.

**ID 8: Adicionar modo listening para que eu ouça audios e escreva o que eu ouvi.**

*   **Esforço (Pontos):** 13
    *   *Justificativa:* Requer a implementação de reprodução de áudio, captura de entrada de texto do usuário, verificação da entrada com um texto de referência, lógica para lidar com pequenas variações na escrita (erros de digitação, etc.) e interface do usuário. Integração de funcionalidades de áudio e reconhecimento de fala (opcional, mas desejável).
*   **Critérios de Aceitação:**
    *   O aplicativo deve reproduzir arquivos de áudio curtos em inglês.
    *   O usuário deve ser capaz de digitar o que ouve.
    *   O aplicativo deve comparar a entrada do usuário com o texto correto (script do áudio).
    *   O aplicativo deve fornecer feedback sobre a correção da resposta, destacando erros.
    *   Deve existir um banco de dados de áudios e seus respectivos scripts (textos).
    *   O sistema deve ser tolerante a pequenos erros de digitação.
    *   Deve haver uma opção para repetir o áudio.
    *   A interface do usuário deve ser clara e permitir fácil interação (reprodução, digitação, envio).
    *   (Opcional) Implementar um sistema de reconhecimento de fala para avaliar a pronúncia do usuário.