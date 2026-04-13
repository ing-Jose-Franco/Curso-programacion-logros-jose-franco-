








const styleSwitcher = document.getElementById('style-switcher'),
switcherToggle = document.getElementById('switcher-toggler'),
switcherClose = document.getElementById('switcher-close');

switcherToggle.addEventListener('click', () => {
    styleSwitcher.classList.add('show-switcher');
});

switcherClose.addEventListener('click', () => {
    styleSwitcher.classList.remove('show-switcher');
});




const colors = document.querySelectorAll('.theme-img');

window.addEventListener('DOMContentLoaded', () => {
    const savedHue = localStorage.getItem('hue');

    if(savedHue) {
        document.documentElement.style.setProperty('--hue', savedHue);
    }
});

colors.forEach((color) => {
    color.onclick = () => {
        const activeHue = color.style.getPropertyValue('--hue');

        document.documentElement.style.setProperty('--hue', activeHue);
        localStorage.setItem('hue', activeHue);
    }
});