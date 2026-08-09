# docker-secure-app

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

## Como rodar
\`\`\`bash
cp .env.example .env
docker compose up --build
curl http://localhost:5000/health
\`\`\`

## Próximos passos
- Scan de vulnerabilidades da imagem com Trivy (ver projeto de CI/CD)