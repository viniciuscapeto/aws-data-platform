---

## 🧩 Git e GitHub

Este projeto utiliza Git para versionamento de código e GitHub para armazenamento do repositório remoto.

O Git permite acompanhar alterações feitas nos arquivos do projeto, criar histórico de versões e enviar o código para o GitHub.

---

## 🔧 Configuração inicial do Git

Antes de usar o Git, é recomendado configurar seu nome e e-mail.

```bash
git config --global user.name "Seu Nome"
```

Define o nome do autor dos commits.

```bash
git config --global user.email "seu-email@email.com"
```

Define o e-mail do autor dos commits.

Para conferir a configuração atual:

```bash
git config --global --list
```

---

## 📌 Iniciar o Git no projeto

Dentro da pasta raiz do projeto:

```bash
git init
```

Esse comando inicializa o Git no projeto atual.

Depois dele, o Git começa a monitorar os arquivos da pasta.

Exemplo:

```bash
cd aws_data_platform
git init
```

---

## 🔍 Verificar status dos arquivos

```bash
git status
```

Esse é um dos comandos mais importantes do Git.

Ele mostra:

- arquivos novos ainda não versionados
- arquivos modificados
- arquivos prontos para commit
- branch atual
- se há alterações pendentes

Exemplo de uso:

```bash
git status
```

É uma boa prática rodar esse comando antes de fazer `add`, `commit` ou `push`.

---

## 🚫 Arquivos que não devem ir para o GitHub

O projeto usa um arquivo `.gitignore` para evitar que arquivos sensíveis ou desnecessários sejam enviados para o GitHub.

Conteúdo recomendado:

```gitignore
venv/
__pycache__/
.env
*.pyc
```

Explicação:

| Item | Motivo |
|---|---|
| `venv/` | Ambiente virtual local, não deve ir para o repositório |
| `__pycache__/` | Cache gerado automaticamente pelo Python |
| `.env` | Contém senha, endpoint, usuário e dados sensíveis |
| `*.pyc` | Arquivos compilados automaticamente pelo Python |

Criar o `.gitignore` no Windows CMD:

```bash
type nul > .gitignore
```

Adicionar conteúdo via CMD:

```bash
echo venv/ > .gitignore
echo __pycache__/ >> .gitignore
echo .env >> .gitignore
echo *.pyc >> .gitignore
```

Conferir o conteúdo:

```bash
type .gitignore
```

---

## ⚠️ Remover arquivo sensível do Git

Se o arquivo `.env` foi adicionado ao Git por engano, use:

```bash
git rm --cached .env
```

Esse comando remove o `.env` do controle do Git, mas mantém o arquivo no seu computador.

Depois faça um commit:

```bash
git commit -m "remove arquivo env do versionamento"
```

Importante: se o `.env` já foi enviado para o GitHub com senhas reais, recomenda-se trocar essas senhas ou chaves depois.

---

## ➕ Adicionar arquivos para commit

```bash
git add .
```

Adiciona todos os arquivos modificados e novos para a área de preparação do Git.

A área de preparação é como uma “fila” dos arquivos que entrarão no próximo commit.

Também é possível adicionar um arquivo específico:

```bash
git add README.md
```

Ou uma pasta específica:

```bash
git add api/
```

---

## 💾 Criar um commit

```bash
git commit -m "mensagem do commit"
```

O commit salva uma versão do projeto no histórico do Git.

Exemplo:

```bash
git commit -m "estrutura inicial do projeto com FastAPI e RDS"
```

Boas mensagens de commit devem explicar o que foi alterado.

Exemplos bons:

```bash
git commit -m "adiciona conexão com PostgreSQL no RDS"
git commit -m "cria pipeline de ingestão de dados"
git commit -m "adiciona endpoint para listar dados"
git commit -m "atualiza README com instruções do projeto"
```

Evite mensagens genéricas demais, como:

```bash
git commit -m "alterações"
git commit -m "teste"
git commit -m "coisas"
```

---

## 🌐 Conectar projeto local ao GitHub

Depois de criar um repositório no GitHub, conecte o projeto local ao repositório remoto.

Exemplo:

```bash
git remote add origin https://github.com/seu-usuario/aws-data-platform.git
```

Esse comando cria uma conexão chamada `origin` apontando para seu repositório no GitHub.

Para conferir os remotes configurados:

```bash
git remote -v
```

Se precisar remover um remote configurado errado:

```bash
git remote remove origin
```

Depois adicione o remote correto novamente:

```bash
git remote add origin https://github.com/seu-usuario/aws-data-platform.git
```

---

## 🌿 Definir branch principal

```bash
git branch -M main
```

Esse comando renomeia ou define a branch principal como `main`.

Hoje, `main` é o nome mais usado para a branch principal de projetos no GitHub.

---

## 🚀 Enviar código para o GitHub

Primeiro push:

```bash
git push -u origin main
```

Explicação:

- `git push` envia commits para o GitHub
- `origin` é o nome do repositório remoto
- `main` é a branch enviada
- `-u` cria uma ligação entre sua branch local e a branch remota

Depois do primeiro push, normalmente basta usar:

```bash
git push
```

---

## 📥 Baixar atualizações do GitHub

Se o repositório remoto tiver alterações que ainda não estão no seu computador:

```bash
git pull
```

Esse comando baixa as alterações do GitHub e tenta integrar ao seu projeto local.

Uso comum:

```bash
git pull origin main
```

---

## 🔁 Fluxo comum de trabalho com Git

No dia a dia, o fluxo mais comum é:

```bash
git status
git add .
git commit -m "descreva aqui a alteração"
git push
```

Exemplo real:

```bash
git status
git add .
git commit -m "adiciona integração com pipeline de dados"
git push
```

---

## 🧪 Exemplo completo: primeiro envio do projeto

Sequência comum para enviar o projeto pela primeira vez:

```bash
git init
git status
git add .
git commit -m "primeiro commit do projeto AWS Data Platform"
git branch -M main
git remote add origin https://github.com/seu-usuario/aws-data-platform.git
git push -u origin main
```

Antes de rodar `git add .`, confirme se o `.gitignore` já existe e se o `.env` está listado nele.

---

## 🧹 Verificar se o `.env` não está sendo rastreado

```bash
git ls-files .env
```

Se esse comando não mostrar nada, está correto.

Se aparecer `.env`, ele ainda está sendo rastreado. Nesse caso, rode:

```bash
git rm --cached .env
git commit -m "remove env do versionamento"
git push
```

---

## 🕘 Ver histórico de commits

```bash
git log
```

Mostra o histórico completo de commits.

Versão mais resumida:

```bash
git log --oneline
```

Exemplo de saída:

```text
08aa90d remove arquivo env do versionamento
d91a22b adiciona endpoint de dados
b1c3f90 primeiro commit
```

---

## ✏️ Corrigir mensagem do último commit

Se você escreveu a mensagem errada no último commit:

```bash
git commit --amend -m "nova mensagem do commit"
```

Se esse commit ainda não foi enviado para o GitHub, basta seguir normalmente.

Se já foi enviado, pode ser necessário usar:

```bash
git push --force-with-lease
```

Use esse comando com cuidado, pois ele altera o histórico remoto.

---

## 👤 Corrigir autor do commit

Se o Git usou nome ou e-mail errado no commit, configure primeiro:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@email.com"
```

Depois, para corrigir o último commit:

```bash
git commit --amend --reset-author
```

Se o commit já foi enviado:

```bash
git push --force-with-lease
```

---

## 🧯 Erros comuns

### Repository not found

Erro:

```text
remote: Repository not found.
fatal: repository not found
```

Possíveis causas:

- o repositório ainda não foi criado no GitHub
- a URL do remote está errada
- você autenticou com outra conta do GitHub
- o repositório é privado e sua conta não tem acesso

Verifique o remote:

```bash
git remote -v
```

Corrija, se necessário:

```bash
git remote remove origin
git remote add origin https://github.com/seu-usuario/aws-data-platform.git
```

---

### Arquivo `.env` apareceu no GitHub

Se o `.env` foi enviado por engano:

```bash
git rm --cached .env
git commit -m "remove env do repositório"
git push
```

Depois, troque senhas ou chaves que estavam nesse arquivo.

---

### Fiz comandos com o venv ativado. Tem problema?

Não tem problema.

Quando aparece:

```bash
(venv) C:\Users\...\aws_data_platform>
```

isso só significa que o ambiente virtual Python está ativo.

O Git funciona normalmente com ou sem o `venv` ativado.

O importante é estar dentro da pasta correta do projeto.

---

## ✅ Checklist antes de fazer push

Antes de enviar para o GitHub, confira:

- [ ] O `.gitignore` existe
- [ ] O `.env` está dentro do `.gitignore`
- [ ] O `venv/` está dentro do `.gitignore`
- [ ] O comando `git status` não mostra arquivos sensíveis
- [ ] O remote aponta para o repositório correto
- [ ] A branch principal é `main`
- [ ] O commit tem uma mensagem clara

Comandos úteis para conferir:

```bash
git status
git remote -v
git branch
git ls-files .env
```

---

## 📌 Resumo dos principais comandos Git

| Comando | Para que serve |
|---|---|
| `git init` | Inicia o Git no projeto |
| `git status` | Mostra o estado atual dos arquivos |
| `git add .` | Prepara arquivos para commit |
| `git commit -m "mensagem"` | Salva uma versão no histórico |
| `git remote add origin URL` | Conecta o projeto local ao GitHub |
| `git remote -v` | Mostra o repositório remoto configurado |
| `git branch -M main` | Define a branch principal como main |
| `git push -u origin main` | Envia o projeto pela primeira vez |
| `git push` | Envia commits novos para o GitHub |
| `git pull` | Baixa atualizações do GitHub |
| `git log --oneline` | Mostra histórico resumido de commits |
| `git rm --cached arquivo` | Para de rastrear um arquivo sem apagá-lo localmente |

---