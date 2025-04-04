# Build stage
FROM node:19.8.1 AS build

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos de dependências
COPY package*.json ./

# Instalando as dependências
RUN npm install

# Copiando o restante dos arquivos do projeto
COPY . .

# Definindo as variáveis de ambiente através de ARG
ARG VITE_API_URL
ARG VITE_DEFAULT_LINK_PREFIX

ENV VITE_API_URL=$VITE_API_URL
ENV VITE_DEFAULT_LINK_PREFIX=$VITE_DEFAULT_LINK_PREFIX

# Executando o build do projeto
RUN npm run build

# Nginx stage
FROM nginx:alpine

# Removendo arquivos padrão do nginx
RUN rm -rf /usr/share/nginx/html/*

# Copiando os arquivos gerados no build para o nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Copiando o arquivo de configuração do nginx
COPY ./default.conf /etc/nginx/conf.d/default.conf

# Expondo a porta 80
EXPOSE 80

# Comando para rodar o nginx
CMD ["nginx", "-g", "daemon off;"]
