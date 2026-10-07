# Optional local verification recipe; not a claimed production hosting image.
FROM node:22-bookworm-slim
WORKDIR /app
RUN corepack enable
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
RUN corepack pnpm install --frozen-lockfile
COPY . .
CMD ["node", "tests/integration.mjs"]
