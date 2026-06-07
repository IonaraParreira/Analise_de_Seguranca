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
