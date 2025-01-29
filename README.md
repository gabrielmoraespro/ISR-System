# **ISR System**

O **ISR System** (Intelligent Security Response System) é um aplicativo de segurança pública inovador desenvolvido para fornecer uma camada extra de proteção para os usuários em tempo real. Com funcionalidades de geolocalização, alertas rápidos e análise de pontos de risco, o **ISR System** tem como objetivo prevenir crimes, permitindo que os usuários notifiquem as autoridades sobre atividades suspeitas antes que algo aconteça.

## **Funcionalidades Principais**

- **Geolocalização em tempo real**: O aplicativo usa a localização do usuário para monitorar a área e enviar alertas à polícia e outros usuários em caso de risco iminente.
- **Alertas em tempo real**: O usuário pode enviar alertas de segurança diretamente para o backend, que notifica a polícia ou outros serviços de emergência.
- **Integração com Mapas**: Visualize pontos críticos de segurança e navegue por áreas seguras.
- **Comunicação direta**: Com um simples clique, envie seu alerta para o serviço de emergência e compartilhe sua localização.
  
Este projeto é dividido em duas partes principais:
- **Frontend**: Desenvolvido com React Native, para oferecer uma experiência de aplicativo nativo multiplataforma (Android e iOS).
- **Backend**: Desenvolvido com Node.js, que gerencia os alertas e as notificações em tempo real.

## **Tecnologias Utilizadas**

- **Frontend**: React Native, Expo
- **Backend**: Node.js, Express.js
- **Banco de Dados**: Firebase (opcional para dados em tempo real)
- **Mapas**: Google Maps API / Mapbox
- **Geolocalização**: Expo Location / @react-native-community/geolocation

## **Requisitos de Sistema**

- **Node.js**: Versão 14 ou superior.
- **React Native CLI**: Se não estiver utilizando o Expo.
- **Expo CLI**: Para quem optar por usar o Expo para desenvolvimento multiplataforma.

---

## **Passo a Passo para Instalação**

### **1. Instalação no _Kali Linux_**:

1. **Instalar o Node.js e o NPM**:
   - Abra o terminal e instale o Node.js com o seguinte comando:
     ```bash
     sudo apt update
     sudo apt install nodejs npm
     ```

2. **Instalar o Expo CLI (se preferir usar Expo)**:
   ```bash
   sudo npm install -g expo-cli
   


**Clonar o repositório:**

No terminal, execute:
 ```bash
git clone https://github.com/SEU_USUARIO/ISR-System.git
cd ISR-System
 ```
Instalar as dependências do frontend:

Se você estiver utilizando o Expo, instale as dependências com o seguinte comando:
```bash

npm install
Instalar as dependências do backend:

Navegue até o diretório backend e instale as dependências:
```bash

cd backend
npm install
 ```
Rodar o servidor backend:
 ```
No diretório backend, execute:
```bash

node server.js
 ```
Rodar o aplicativo no Expo:

Volte para o diretório do frontend e execute:
```bash

expo start
2. Instalação no Windows:
Instalar o Node.js e o NPM:

Baixe o instalador do Node.js em https://nodejs.org/ e siga as instruções de instalação.
Instalar o Expo CLI: Abra o prompt de comando ou PowerShell e execute:

```bash

npm install -g expo-cli
 ```
Clonar o repositório:

Abra o terminal ou PowerShell e execute:
```bash

git clone https://github.com/SEU_USUARIO/ISR-System.git
cd ISR-System
 ```
Instalar as dependências do frontend:

```bash

npm install
Instalar as dependências do backend:
 ```
```bash

cd backend
npm install
 ```
Rodar o servidor backend:

```bash

node server.js
 ```
Rodar o aplicativo no Expo: Volte para o diretório do frontend e execute:

```bash

expo start
 ```
3. Instalação no macOS:
Instalar o Node.js e o NPM:

Use o Homebrew para instalar o Node.js (se você não tiver o Homebrew, siga as instruções em https://brew.sh/):
```bash

brew install node
Instalar o Expo CLI:
 ```
```bash

npm install -g expo-cli
Clonar o repositório:

```bash

git clone https://github.com/SEU_USUARIO/ISR-System.git
cd ISR-System
Instalar as dependências do frontend:

```bash

npm install
Instalar as dependências do backend:

```bash

cd backend
npm install
Rodar o servidor backend:

```bash

node server.js
Rodar o aplicativo no Expo: Volte para o diretório do frontend e execute:

```bash

expo start
Como Contribuir
Faça um fork deste repositório.
Crie uma branch para sua nova funcionalidade (git checkout -b nova-funcionalidade).
Faça as alterações necessárias.
Commit suas mudanças (git commit -am 'Adicionando nova funcionalidade').
Envie para o repositório remoto (git push origin nova-funcionalidade).
Crie um Pull Request.


**Licença**
Este projeto está licenciado sob a MIT License - consulte o arquivo LICENSE para mais detalhes.

   
