# Guia de Contribuição - VoughtGuard

Bem-vinda ao projeto! Leia este guia com atenção antes de começar.

O fluxo descrito aqui é exatamente o que será avaliado.

---

## Pré-requisitos

Antes de começar, certifique-se de ter concluído:

- [ ] **[Trilha 01 - Fundamentos](https://github.com/Starlight-git-project/trilha-01-fundamentos)** - commits, `.gitignore`, variáveis de ambiente
- [ ] **[Trilha 02 - Governança](https://github.com/Starlight-git-project/trilha-02-governanca)** - branches, PRs, code review

Se ainda não concluiu, comece por lá. O projeto prático assume que você já domina esses conceitos.✨

---

## Suas issues

Cada uma tem issues atribuídas. Veja a sua antes de começar qualquer coisa.

| Issue | Responsável | Semana |
|-------|------------|--------|
| #1 — Estrutura do repositório | Aluna A | Semana 1 |
| #2 — `limpeza.py` | Aluna B | Semana 1 |
| #3 — `qualidade.py` | Aluna C | Semana 1 |
| #4 — `transformacao.py` | Aluna A | Semana 2 |
| #5 — Tabelas analíticas | Aluna B | Semana 2 |
| #6 — `docs/orquestracao.md` | Aluna C | Semana 2 |
| #7 — Testes de limpeza | Aluna B | Semana 3 |
| #8 — Testes de transformação | Aluna C | Semana 3 |
| #9 — `pipeline.py` final | Aluna A | Semana 3 |

Respeite as dependências, algumas issues só podem começar depois de outras mergeadas.

---

## Passo 1 - Fork do repositório

Faça fork deste repositório para a sua conta pessoal:

1. Clique em **Fork** no canto superior direito
2. Selecione sua conta como destino
3. Aguarde a criação do fork

---

## Passo 2 - Clone do fork

```bash
git clone https://github.com/SEU-USUARIO/voughtguard-pipeline-fraud-detection.git
cd voughtguard-pipeline-fraud-detection
```

---

## Passo 3 - Configure o remote original

Isso permite que você envie suas alterações diretamente para o repositório do projeto. Onde os commits contam para o seu perfil e os badges [Github](https://github.com/drknzz/GitHub-Achievements).

```bash
git remote add upstream https://github.com/Starlight-git-project/voughtguard-pipeline-fraud-detection.git

# Verifique os remotes configurados
git remote -v
# origin    https://github.com/SEU-USUARIO/voughtguard-... (fetch)
# origin    https://github.com/SEU-USUARIO/voughtguard-... (push)
# upstream  https://github.com/Starlight-git-project/voughtguard-... (fetch)
# upstream  https://github.com/Starlight-git-project/voughtguard-... (push)
```

---

## Passo 4 - Configure o ambiente

```bash
# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com seus valores locais
# NUNCA commite este arquivo
```

---

## Passo 5 - Baixe o dataset

Acesse: [Kaggle — Synthetic Financial Fraud Dataset](https://www.kaggle.com/datasets/umitka/synthetic-financial-fraud-dataset/data)

Salve o arquivo em `data/raw/transactions.csv`

`data/raw/` está no `.gitignore` — **nunca commite dados**.

---

## Passo 6 - Crie sua branch a partir do upstream

```bash
# Garante que você está na main atualizada do repositório original
git fetch upstream
git switch main
git merge upstream/main

# Cria sua branch
git switch -c feature/nome-da-sua-branch
```

Branches por issue:

| Issue | Branch |
|-------|--------|
| #1 | `feature/estrutura-repositorio` |
| #2 | `feature/limpeza-dados` |
| #3 | `feature/relatorio-qualidade` |
| #4 | `feature/transformacao-dados` |
| #5 | `feature/tabelas-analiticas` |
| #6 | `docs/orquestracao` |
| #7 | `test/limpeza` |
| #8 | `test/transformacao` |
| #9 | `feature/pipeline-final` |

**Nunca trabalhe diretamente na `main`.**

---

## Passo 7 - Desenvolva com commits semânticos

```bash
git add src/limpeza.py
git commit -m "feat(limpeza): implementar remover_nulos_criticos"

git add tests/test_limpeza.py
git commit -m "test(limpeza): cobrir remover_nulos_criticos com casos de borda"
```

### Tipos aceitos

| Tipo | Quando usar |
|------|------------|
| `feat` | Nova função ou funcionalidade |
| `fix` | Correção de bug |
| `test` | Testes |
| `docs` | Documentação |
| `refactor` | Refatoração |
| `chore` | Configuração, dependências |

### Commits que serão apontados no review

```bash
# Esses serão comentados como [bloqueante]
git commit -m "fix"
git commit -m "arrumei"
git commit -m "wip"
git commit -m "."
```

---

## Passo 8 - Envie para o repositório original

```bash
# Envia sua branch direto para o upstream (repo da Starlight)
git push upstream feature/nome-da-sua-branch
```

Seus commits vão direto para o repositório original - aparecem no seu perfil e contam para[ badges](https://github.com/drknzz/GitHub-Achievements). ✅

---

## Passo 9 - Abra o Pull Request

No GitHub, acesse o repositório original da Starlight - Voughtguard:

1. Clique em **Compare & pull request**
2. **Base:** `develop` ← `feature/nome-da-sua-branch`
3. Preencha título e descrição usando o template que aparece automaticamente
4. Em **Development**, clique em **Closes** e adicione o número da sua issue (ex: `Closes #2`)
5. Clique em **Create pull request**

---

## Passo 10 - Checklist antes de pedir review

- [ ] Nenhum arquivo `.env` aparece em `git status`
- [ ] Nenhuma credencial hardcoded no código
- [ ] `pytest tests/` passa sem erros
- [ ] Commits com mensagens semânticas
- [ ] Funções com type hints e docstrings
- [ ] PR com título semântico e descrição preenchida

---

## O que esperar do review

O review usa os prefixos do checklist da [Trilha 02](https://github.com/Starlight-git-project/trilha-02-governanca):

| Prefixo | O que significa |
|---------|----------------|
| `[bloqueante]` | Precisa ser resolvido antes do merge |
| `[sugestão]` | Melhoria desejável, não bloqueia |
| `[dúvida]` | Pedido de esclarecimento |
| `[elogio]` | Boa prática que merece destaque |

### Como responder

**Bloqueante:** implemente e confirme com o hash do commit.
```
Corrigido no commit abc1234
```

**Sugestão:** implemente se concordar, ou justifique.
```
Mantive a abordagem porque X. Posso ajustar se preferir.
```

Marque a conversa como resolvida **só depois** de implementar ou justificar, nunca antes.

### ⚠️ Aprovação cancelada após novos commits

Se você fizer novos commits **depois de receber uma aprovação**, a aprovação será cancelada automaticamente. Isso é intencional, garante que o revisor sempre vê o código final.

Se precisar ajustar algo após a aprovação:
1. Faça as correções
2. Commite com mensagem clara: `fix(limpeza): corrigir tipo de retorno conforme review`
3. Avise o revisor no PR pedindo um novo review

Isso não é punição, é como funciona em times profissionais.🤩

---

## Regras do projeto

1. **Nunca commite na `main` diretamente** - todo código passa por PR
2. **Nunca commite o `.env`** - credenciais ficam fora do repositório
3. **Nunca commite dados** - `data/` está no `.gitignore`
4. **Um PR por issue** - não misture responsabilidades
5. **Resolva todos os comentários antes de pedir merge**
6. **Sempre envie para o `upstream`** - não para o `origin` - para garantir badges e avaliação

---

## Dúvidas

Comente na issue correspondente ou abra uma **Discussion** no repositório.

---

<div align="center">

⭐ [Starlight Git Project](https://github.com/Starlight-git-project) · open source · feito para profissionais de dados

</div>
