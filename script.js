document.getElementById('send-btn').addEventListener('click', function() {
    var userMessage = document.getElementById('user-input').value;

    // Append user message
    var chatWindow = document.getElementById('chat-window');
    var newMessage = document.createElement('div');
    newMessage.classList.add('message', 'user-message');
    newMessage.innerHTML = `<span class="message-text">${userMessage}</span>`;
    chatWindow.appendChild(newMessage);

    // Clear input field
    document.getElementById('user-input').value = '';

    // Simulate bot reply (you can replace this with an actual bot response)
    var botReply = document.createElement('div');
    botReply.classList.add('message', 'bot-message');
    botReply.innerHTML = '<span class="message-text">Processing...</span>';
    chatWindow.appendChild(botReply);

    // Scroll to the bottom
    chatWindow.scrollTop = chatWindow.scrollHeight;
});
