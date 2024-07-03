// Mobile menu toggle
document.getElementById("hamburger").addEventListener("click", function() {
    var menu = document.getElementById("menu");
    menu.classList.add("show");
});

document.getElementById("close-btn").addEventListener("click", function() {
    var menu = document.getElementById("menu");
    menu.classList.remove("show");
});

// Close menu when clicking outside
document.addEventListener("click", function(event) {
    var menu = document.getElementById("menu");
    var hamburger = document.getElementById("hamburger");
    if (!menu.contains(event.target) && !hamburger.contains(event.target)) {
        menu.classList.remove("show");
    }
});

// Slideshow functionality
let slideIndex = 0;
const slides = document.getElementsByClassName("slide");
const dots = document.getElementsByClassName("dot");
showSlides();

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides() {
    let i;
    for (i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].classList.remove("active");
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].classList.add("active");
    dots[slideIndex-1].classList.add("active");
    setTimeout(showSlides, 5000); // Change image every 5 seconds
}

// Date and time update
function updateDateTime() {
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    document.getElementById("date").textContent = now.toLocaleDateString('en-US', options);
    document.getElementById("time").textContent = now.toLocaleTimeString('en-US');
}

setInterval(updateDateTime, 1000);
updateDateTime();

// Typing effect for welcome message
const welcomeMessage = "Welcome to Emmalord Educational Complex";
const welcomeElement = document.getElementById("welcome-message");
let i = 0;

function typeWriter() {
    if (i < welcomeMessage.length) {
        welcomeElement.innerHTML += welcomeMessage.charAt(i);
        i++;
        setTimeout(typeWriter, 50);
    }
}

window.addEventListener('load', typeWriter);

// Animate statistics
function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = Math.floor(progress * (end - start) + start);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Animate statistics when they come into view
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            animateValue(document.getElementById("studentCount"), 0, 1000, 2000);
            animateValue(document.getElementById("teacherCount"), 0, 50, 2000);
            animateValue(document.getElementById("satisfactionRate"), 0, 98, 2000);
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

observer.observe(document.querySelector('.statistics'));

// Smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Simple form validation
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = this.querySelector('input[name="name"]').value;
        const email = this.querySelector('input[name="email"]').value;
        const message = this.querySelector('textarea[name="message"]').value;

        if (name && email && message) {
            alert('Thank you for your message. We will get back to you soon!');
            this.reset();
        } else {
            alert('Please fill in all fields.');
        }
    });
}

// Highlight today's date in the table
document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody tr');
    const today = new Date();
    const todayStr = `${today.toLocaleString('default', { month: 'long' })} ${today.getDate()}, ${today.getFullYear()}`;

    rows.forEach(row => {
        const dateCell = row.cells[2];
        if (dateCell.textContent.includes(todayStr)) {
            row.classList.add('highlight');
        }
    });
});

// JavaScript for Gallery Lightbox
document.addEventListener('DOMContentLoaded', () => {
    const galleryImages = document.querySelectorAll('.gallery-grid img');
    const lightbox = document.createElement('div');
    const lightboxImage = document.createElement('img');
    const closeButton = document.createElement('span');

    lightbox.classList.add('lightbox');
    closeButton.classList.add('lightbox-close');
    closeButton.innerHTML = '&times;';

    lightbox.appendChild(lightboxImage);
    lightbox.appendChild(closeButton);
    document.body.appendChild(lightbox);

    galleryImages.forEach((image) => {
        image.addEventListener('click', () => {
            lightboxImage.src = image.src;
            lightbox.classList.add('active');
        });
    });

    closeButton.addEventListener('click', () => {
        lightbox.classList.remove('active');
    });

    lightbox.addEventListener('click', (e) => {
        if (e.target !== lightboxImage) {
            lightbox.classList.remove('active');
        }
    });
});

// Staff modal functionality
document.addEventListener('DOMContentLoaded', () => {
    const staffCards = document.querySelectorAll('.staff-card');
    const staffModal = document.createElement('div');
    const staffModalContent = document.createElement('div');
    const staffModalClose = document.createElement('span');

    staffModal.classList.add('staff-modal');
    staffModalContent.classList.add('staff-modal-content');
    staffModalClose.classList.add('staff-modal-close');
    staffModalClose.innerHTML = '&times;';

    staffModal.appendChild(staffModalClose);
    staffModal.appendChild(staffModalContent);
    document.body.appendChild(staffModal);

    staffCards.forEach((card) => {
        card.addEventListener('click', () => {
            staffModalContent.innerHTML = card.innerHTML;
            staffModal.classList.add('active');
        });
    });

    staffModalClose.addEventListener('click', () => {
        staffModal.classList.remove('active');
    });

    staffModal.addEventListener('click', (e) => {
        if (e.target === staffModal) {
            staffModal.classList.remove('active');
        }
    });
});
