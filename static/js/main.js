// Add event listener when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide flash messages after 3 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 3000);
    });
});