// script.js

// Smooth scrolling
const scrollLinks = document.querySelectorAll('a.scroll-link');

scrollLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        targetElement.scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form handling
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(form);
    // Handle form submission (e.g., send to API)
    console.log('Form submitted', formData);
});

// Animations
const animatedElements = document.querySelectorAll('.animate');

function checkVisibility() {
    animatedElements.forEach(element => {
        const rect = element.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            element.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', checkVisibility);
checkVisibility();

// Interactive elements
const toggleButtons = document.querySelectorAll('.toggle');
toggleButtons.forEach(button => {
    button.addEventListener('click', function() {
        const content = this.nextElementSibling;
        content.classList.toggle('active');
    });
});