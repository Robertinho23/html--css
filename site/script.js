document.addEventListener("DOMContentLoaded", function() {
    const jogosLista = document.querySelector("#jogos .jogos-lista");
    const prevJogo = document.getElementById("prevJogo");
    const nextJogo = document.getElementById("nextJogo");

    let currentIndex = 0;
    const cardWidth = 180; // Largura de cada card de jogo
    const gap = 20; // Espaçamento entre os cards
    const visibleCards = 3; // Quantidade de cards visíveis por vez
    const totalCards = jogosLista.children.length;

    // Calcula a quantidade de scroll para um "passo" do carrossel (um card + gap)
    const step = cardWidth + gap;

    function updateCarousel() {
        const offset = currentIndex * step;
        jogosLista.scrollTo({ left: offset, behavior: "smooth" });
    }

    nextJogo.addEventListener("click", () => {
        currentIndex++;
        if (currentIndex > totalCards - visibleCards) {
            currentIndex = 0; // Volta para o início se chegar ao final
        }
        updateCarousel();
    });

    prevJogo.addEventListener("click", () => {
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = totalCards - visibleCards; // Vai para o final se estiver no início
            // Garante que o currentIndex não seja negativo se o total de cards for menor que os visíveis
            if (currentIndex < 0) currentIndex = 0;
        }
        updateCarousel();
    });

    // Inicializa o carrossel na posição correta
    updateCarousel();
});



    // Lógica para o botão 'Voltar ao Topo'
    const voltarTopoBtn = document.querySelector(".voltar-topo");

    window.addEventListener("scroll", () => {
        if (window.scrollY > 200) { // Mostra o botão após rolar 200px
            voltarTopoBtn.classList.add("show");
        } else {
            voltarTopoBtn.classList.remove("show");
        }
    });

    voltarTopoBtn.addEventListener("click", (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
