<!DOCTYPE html>
<html>
<head>
  <style>
    #text {
      font-size: 16px;
    }
  </style>
</head>
<body>

<p id="text">Texto de exemplo com tamanho de fonte ajustável.</p>
<button onclick="aumentarFonte()">Aumentar Fonte</button>
<button onclick="diminuirFonte()">Diminuir Fonte</button>

<script>
  function aumentarFonte() {
    var texto = document.getElementById("text");
    var tamanhoFonte = window.getComputedStyle(texto, null).getPropertyValue('font-size');
    var novoTamanho = parseInt(tamanhoFonte) + 2;
    texto.style.fontSize = novoTamanho + "px";
  }

  function diminuirFonte() {
    var texto = document.getElementById("text");
    var tamanhoFonte = window.getComputedStyle(texto, null).getPropertyValue('font-size');
    var novoTamanho = parseInt(tamanhoFonte) - 2;
    texto.style.fontSize = novoTamanho + "px";
  }
</script>

</body>
</html>
