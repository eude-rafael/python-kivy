<?php

 // Verifica se a requisição é do tipo POST e se há conteúdo no corpo da requisição
if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty(file_get_contents('php://input'))) {
    // Obtém o conteúdo JSON enviado no corpo da requisição
    $data = json_decode(file_get_contents('php://input'), true);

    // Verifica se a chave 'url' está presente no JSON
    if (isset($data['url'])) {
        $out = [
            "recebido" => $data['url']
        ];
    } else {
        $out = [
            "recebido" => "Chave 'url' não encontrada no JSON."
        ];
    }
} else {
    $out = [
        "recebido" => "Nada recebido"
    ];
}

// Responde com o JSON
header('Content-Type: application/json');
echo json_encode($out);



     

    