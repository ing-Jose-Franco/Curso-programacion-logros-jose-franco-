const contactForm = document.getElementById('contact-form'), 
  contactName = document.getElementById('contact-name'),
  contactEmail = document.getElementById('contact-email'),
  contactSbuject = document.getElementById('contact-subject'),
  contactMessage = document.getElementById('contact-message'),
  message = document.getElementById('message');

  const sendEmail = (e) => {
    e.preventDefault();

    if(
        contactName.value === '' || 
        contactEmail.value === "" || 
        contactSbuject === '' || 
        contactMessage.value === ''
    ) {
        message.textContent = 'Rellene todo los campos';
        message.classList.remove('color-first');
        message.classList.add('color-red');

        setTimeout(() => {
            message.textContent = '';
        }, 3000);
    } else{
    emailjs
    .sendForm(
        'service_et8mr3r', 
        'template_gk4aj1t', 
        '#contact-form', 
        'iJBnpuXfCoWXSkfwe'
    )
    .then(
        () => {
            message.textContent = 'Mensaje Enviado!';
            message.classList.add('color-first')

            setTimeout(() => {
            message.textContent = '';
        }, 5000);
    },
    (error) => {
        alert('OOPs! ALGO SALIO MAL...', error);
  }
);

        contactName.value = '';
        contactEmail.value = '';
        contactSbuject.value = '';
        contactMessage.value = '';
    }
};

  contactForm.addEventListener('submit', sendEmail)