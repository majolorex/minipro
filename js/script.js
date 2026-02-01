// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const links = document.querySelectorAll('.nav-links li');

hamburger.addEventListener('click', () => {
    // Toggle Nav
    navLinks.classList.toggle('nav-active');

    // Animate Links
    links.forEach((link, index) => {
        if (link.style.animation) {
            link.style.animation = '';
        } else {
            link.style.animation = `fadeInUp 0.5s ease forwards ${index / 7 + 0.3}s`;
        }
    });

    // Hamburger Animation
    hamburger.classList.toggle('toggle');
});

// Scroll Effect for Header
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    if (window.scrollY > 100) {
        header.style.background = '#fff';
        header.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    } else {
        // Optional: Transparent background when at top if desired
        // header.style.background = 'transparent';
        // header.style.boxShadow = 'none';
    }
});
