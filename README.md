# Amart Shipping — P0 (site de exemplo)

Protótipo estático do site da Amart Shipping, em português.

## Como abrir

**VS Code + Live Server (recomendado)**
1. Abra a pasta `P0-NAUTICA` no VS Code.
2. Instale a extensão recomendada *Live Server* (o VS Code sugere sozinho).
3. Clique com o botão direito em `index.html` → **Open with Live Server**
   (ou no botão **Go Live** na barra inferior). Abre em `http://127.0.0.1:5500`.

**Sem VS Code**
- Dê dois cliques em `iniciar-site.bat` (usa o Python e abre `http://127.0.0.1:8770`).

## Estrutura

```
index.html      Início
about.html      Sobre (equipe, eventos, vagas)
tech.html       Tecnologia (serviços, mapa de praças)
news.html       Notícias
legal.html      Aviso legal
privacy.html    Privacidade
assets/
  css/          estilos (compilado)
  js/           scripts (compilado)
  img/          fotos e ilustrações
  logos/        logos de parceiros e imprensa
  fonts/        fontes Helvetica Now Display
  3d/           modelos 3D (.glb) e texturas usadas na página inicial
_serve.py       servidor local simples (alternativa ao Live Server)
iniciar-site.bat
```

A pasta `_arquivo/` fica só na máquina local (está no `.gitignore`): guarda a cópia
original de referência, backups e imagens/vídeos que não são usados no site.

## Observações

- O CSS e o JS são arquivos já compilados; edite os textos diretamente nos `.html`.
- O formulário de contato e o boletim não enviam dados: apenas exibem a mensagem de sucesso.
