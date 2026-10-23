@echo off
title Sistema Web Flask
echo ===================================================
echo Iniciando o Servidor da Aplicacao Web...
echo ===================================================

:: Navega ate a pasta onde este script .bat esta localizado
cd /d "%~dp0"

:: Ativa o ambiente virtual Python
call venv\Scripts\activate.bat

:: Inicia o servidor Python em segundo plano na mesma janela
start /b python app.py

:: Mensagem de status no terminal
echo Aguardando o servidor carregar...

:: Aguarda 3 segundos para garantir que o Flask iniciou na porta 5000
timeout /t 3 /nobreak >nul

:: Abre a aplicação no navegador padrao do Windows
echo Abrindo o navegador...
start http://127.0.0.1:5000

echo ===================================================
echo Sistema rodando em http://127.0.0.1:5000
echo ATENCAO: Mantenha esta janela aberta enquanto usar.
echo ===================================================