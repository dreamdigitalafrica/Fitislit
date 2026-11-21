(() => {
  const form = document.getElementById('enquiry-form');
  if (!form) return;
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const body = `Name: ${form.elements.name.value}\nEmail: ${form.elements.email.value}\n\n${form.elements.message.value}`;
    window.location.href = `mailto:Shebasimprint@gmail.com?subject=${encodeURIComponent('Sheba Imprint enquiry')}&body=${encodeURIComponent(body)}`;
    document.getElementById('enquiry-status').textContent = 'Your email app will open with your enquiry. Send it there when ready.';
  });
})();
