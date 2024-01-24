
def corpoEmail(email,nome):
    corpo = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>
            <p>Olá {nome}, seja bem-vindo à ferramenta de levantamento de compras institucionais de TIC da UFC.</p>
            <a href="https://pedidostic.ufc.br/" target="_blank"> Aqui você acessa a ferramenta</a>.</p>
            
            <p>Segue suas credenciais para acesso ao sistema.</p>
            <p><b>Login: {email}</b></p>
            <p><b>Senha:SIAPE</b></p>
            
            <p>Salienta-se que o pedido deve ser feito no prazo informado. Finalizado o prazo, o sistema não poderá ser mais acessado. Caso haja alguma necessidade de inclusão ou alteração, deve ser realizada via abertura de processo no Sistema Eletrônico de Informações (SEI), <a href="https://www.sei.ufc.br" target="_blank">www.sei.ufc.br</a>, tipo: Administração Geral: Projetos de TI (Documento de Intenção de Demanda - DID), especificando e justificando os ajustes.</p>
            
            <p>Conforme apresentado em reunião do CATI, disponibilizamos o Cronograma a seguir:</p>
            
            <ul>
                <li>20/12/2023 - Ofício Circular via processo no SEI para realização do levantamento de demandas de TIC (as demandas específicas já poderão ser solicitadas a partir desta data);</li>
                <li>12/01/2024 - Prazo limite para o envio das informações do usuário, representante da unidade maior (apenas 1 por unidade);</li>
                <li>22/01/2024 - Lançamento da Ferramenta de Levantamento de Pedidos de Compras Institucionais de TIC (a partir desta data poderá ser solicitada a aquisição dos itens institucionais na Ferramenta);</li>
                <li>19/02/2024 - Data final para o envio de demandas institucionais e específicas (Ferramenta de Levantamento e/ou DIDs);</li>
                <li>20/03/2024 - Reunião do CATI para aprovação da proposta de consolidação das demandas de TIC da UFC.</li>
            </ul>
            <p> Segue em anexo um manual com orientações sobre o uso da ferramenta </p>
    
            <p>Para maiores esclarecimentos sobre o processo de levantamento de demandas de TIC, favor consultar a página da STI: <a href="https://sti.ufc.br/informacoes-gerais/governanca-de-ti/" target="_blank">https://sti.ufc.br/informacoes-gerais/governanca-de-ti/</a>.</p>
        </body>
        </html>
    """
    return corpo
