# docker-secure-app
![CI](https://github.com/josaelaraujo/docker-secure-app/actions/workflows/ci.yml/badge.svg)

API Flask minimalista, containerizada com foco em boas práticas de segurança
para produção.

## Tecnologias
Python 3.12, Flask, Docker, Docker Compose

## Decisões de segurança tomadas
- **Multi-stage build**: a imagem final não carrega ferramentas de build.
- **Usuário não-root**: validado com `docker run ... whoami` → `appuser`.
- **Filesystem read-only**: validado tentando escrever dentro do container em execução (falha como esperado).
- **Secrets via .env**: nenhuma credencial versionada.
- **Healthcheck**: monitoramento automático de `/health`.

## Pipeline CI/CD

A cada push/PR na main, o GitHub Actions executa:
1. Lint (flake8)
2. Testes automatizados (pytest)
3. SAST — análise estática de código em busca de falhas de segurança (Bandit)
4. Scan de vulnerabilidades na imagem Docker (Trivy) — o pipeline falha se houver CVEs CRITICAL ou HIGH

## Como rodar
\`\`\`bash
cp .env.example .env
docker compose up --build
curl http://localhost:5000/health
\`\`\`

## Próximos passos
- Scan de vulnerabilidades da imagem com Trivy (ver projeto de CI/CD)