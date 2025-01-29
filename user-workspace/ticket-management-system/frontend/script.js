document.addEventListener('DOMContentLoaded', () => {
    const ticketList = document.getElementById('ticket-list');
    const newTicketButton = document.getElementById('new-ticket');

    // Função para carregar tickets do backend
    function loadTickets() {
        fetch('/tickets')
            .then(response => response.json())
            .then(data => {
                ticketList.innerHTML = ''; // Limpar a lista antes de adicionar novos tickets
                data.forEach(ticket => {
                    const li = document.createElement('li');
                    li.textContent = `ID: ${ticket.id}, Título: ${ticket.title}, Descrição: ${ticket.description}`;
                    ticketList.appendChild(li);
                });
            })
            .catch(error => {
                ticketList.innerHTML = '<p>Erro ao carregar tickets.</p>';
                console.error('Erro:', error);
            });
        // Exemplo: fetch('/api/tickets')
        ticketList.innerHTML = '<p>Carregando tickets...</p>';
        // Simulação de carregamento
        setTimeout(() => {
            ticketList.innerHTML = '<p>Lista de tickets carregada com sucesso!</p>';
        }, 1000);
    }

    // Evento para criar um novo ticket
newTicketButton.addEventListener('click', (event) => {
    event.preventDefault(); // Previne o comportamento padrão do botão
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const status_id = document.getElementById('status_id').value;
    const department_id = document.getElementById('department_id').value;

    const newTicket = {
        title: title,
        description: description,
        status_id: parseInt(status_id),
        department_id: parseInt(department_id)
    };

    fetch('/tickets', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newTicket)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert('Ticket criado com sucesso!');
            loadTickets(); // Recarrega a lista de tickets
        }
    })
    .catch(error => {
        console.error('Erro ao criar ticket:', error);
        alert('Erro ao criar ticket.');
    });
    });

    // Carregar tickets ao iniciar
    loadTickets();
});
