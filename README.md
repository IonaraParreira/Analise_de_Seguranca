<h1>🧐 O que o html.escape() faz de verdade?</h1>
Imagine que um hacker tente invadir o seu sistema digitando isso no campo da URL:
https://siteparceiro.com<script>roubar_senhas()</script>

Se o seu sistema aceitar esse texto bruto e depois exibir essa URL em uma página Web, o navegador da vítima vai achar que <script> é uma ordem real em JavaScript e vai executar o ataque (isso é o famoso XSS - Cross-Site Scripting).

Quando o Python roda o html.escape(), ele faz uma "tradução" dos caracteres perigosos para um formato de texto inofensivo. Veja a transformação:

O caractere < vira &lt; (significa Less Than / Menor que)

O caractere > vira &gt; (significa Greater Than / Maior que)

Dessa forma, o código malicioso perde os "braços" (< >) e vira apenas um texto comum. O navegador não vai executar nada, ele vai apenas desenhar o texto na tela de forma segura.

<h1>🛠️ Como esse fluxo funciona na Segurança?</h1>
  
Esse processo cria uma barreira onde o dado perigoso é neutralizado antes de causar qualquer danção na aplicação.
Dividi o código em funções para seguir o princípio de Responsabilidade Única (SOLID), onde cada bloco de código cuida de apenas uma tarefa crítica de segurança.


<h2>🧼 Implementando a Camada de Sanitização</h2>

Para tornar o script resiliente a falhas e ataques, foi adicionada uma etapa de **Sanitização** antes da validação. O fluxo agora segue o princípio de segurança de defesa em profundidade:

1. **Recebimento do Input:** O sistema recebe a string bruta do usuário.
2. **Sanitização (.strip() + .lower()):** Remove espaços acidentais e padroniza a caixa do texto, evitando evasão de filtros por variação de maiúsculas.
3. **Neutralização de HTML (html.escape):** Sanitiza caracteres especiais (`<`, `>`, `&`), prevenindo ataques de Injeção de Código e Cross-Site Scripting (XSS).
4. **Validação Estrita:** O dado limpo passa pelo crivo dos métodos `.startswith()` e `.endswith()`.

<h1>🛑 Validação</h1>
A Validação é uma checagem do tipo "tudo ou nada". O sistema analisa o dado que o usuário digitou e decide se ele segue as regras estabelecidas.

Se a URL começar com https:// e terminar com .com, o sistema aceita.

Se o usuário digitar algo malicioso ou errado, o sistema rejeita o bloco inteiro e exibe uma mensagem de erro (URL inválida!).

No exercício: O if com .startswith() e .endswith() barra a entrada inválida. O dado malicioso nem chega a entrar no sistema.

<h1>🧹 Sanitização</h1>
A Sanitização (ou limpeza) é o ato de modificar, limpar ou transformar o dado do usuário para torná-lo seguro, em vez de simplesmente rejeitá-lo.

Se o usuário digitasse https://siteparceiro.com <script>malicioso</script>, um sanitizador iria remover as tags <script> ou neutralizá-las, deixando apenas a URL limpa.

Se o usuário digitasse a URL com espaços em branco nas pontas, a sanitização usaria um .strip() para apagar os espaços antes de validar.

🔬 Testes e Evidências

<img width="821" height="112" alt="image" src="https://github.com/user-attachments/assets/d3ee2926-9cca-450f-a9c1-afe4c172c856" />

<br>
<br>
<img width="837" height="120" alt="Captura de tela 2026-06-07 152455" src="https://github.com/user-attachments/assets/35d09bda-3cf9-4c65-a81c-5a28687b3be7" />
