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


//Gallery
document.addEventListener('DOMContentLoaded', function() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    let currentIndex = 0;
  
    function showImage(index) {
      const images = Array.from(galleryItems).map(item => item.querySelector('img').src);
      const lightbox = document.createElement('div');
      lightbox.id = 'lightbox';
      lightbox.innerHTML = `
        <div class="lightbox-content">
          <img src="${images[index]}" alt="Enlarged gallery image">
          <span class="close">&times;</span>
          <span class="prev">&lt;</span>
          <span class="next">&gt;</span>
        </div>
      `;
      document.body.appendChild(lightbox);
  
      const closeBtn = lightbox.querySelector('.close');
      const prevBtn = lightbox.querySelector('.prev');
      const nextBtn = lightbox.querySelector('.next');
      const img = lightbox.querySelector('img');
  
      closeBtn.addEventListener('click', closeLightbox);
      prevBtn.addEventListener('click', () => navigate(-1));
      nextBtn.addEventListener('click', () => navigate(1));
      img.addEventListener('click', toggleZoom);
  
      lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) closeLightbox();
      });
  
      document.addEventListener('keydown', handleKeyPress);
  
      function navigate(step) {
        currentIndex = (currentIndex + step + images.length) % images.length;
        img.src = images[currentIndex];
        img.classList.remove('zoomed');
      }
  
      function handleKeyPress(e) {
        switch(e.key) {
          case 'ArrowLeft': navigate(-1); break;
          case 'ArrowRight': navigate(1); break;
          case 'Escape': closeLightbox(); break;
        }
      }
  
      function toggleZoom() {
        img.classList.toggle('zoomed');
      }
  
      function closeLightbox() {
        document.body.removeChild(lightbox);
        document.removeEventListener('keydown', handleKeyPress);
      }
    }
  
    galleryItems.forEach((item, index) => {
      item.addEventListener('click', function() {
        currentIndex = index;
        showImage(currentIndex);
      });
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
    staffModalClose.innerHTML = '';

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

document.addEventListener('DOMContentLoaded', function() {
    const highlightItems = document.querySelectorAll('.highlight-item');
    
    highlightItems.forEach(item => {
        item.addEventListener('click', function() {
            this.classList.toggle('flip');
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const stats = document.querySelectorAll('.stat-number');
    const statisticsSection = document.querySelector('.statistics');
    let animated = false;

    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            obj.textContent = Math.floor(progress * (end - start) + start);
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }

    function startAnimation() {
        if (animated) return;
        animated = true;
        stats.forEach(stat => {
            const end = parseInt(stat.getAttribute('data-target'));
            animateValue(stat, 0, end, 2000);
        });
    }

    // Intersection Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                startAnimation();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    observer.observe(statisticsSection);

    // Scroll event as a fallback
    function checkScroll() {
        const rect = statisticsSection.getBoundingClientRect();
        if (rect.top <= window.innerHeight && rect.bottom >= 0) {
            startAnimation();
            window.removeEventListener('scroll', checkScroll);
        }
    }

    window.addEventListener('scroll', checkScroll);

    // Check immediately in case the section is already visible
    checkScroll();
});
function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        let value = Math.floor(progress * (end - start) + start);
        obj.textContent = value;
        if (obj.nextElementSibling && obj.nextElementSibling.tagName === 'SPAN') {
            obj.textContent = value + obj.nextElementSibling.textContent;
        }
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

(function() {
    emailjs.init("xcxKiRYGT8ejGSrNR");
})();

document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var submitButton = document.getElementById('submit-btn');
    var originalText = submitButton.textContent;

    submitButton.disabled = true;
    submitButton.innerHTML = 'Sending... <i class="fa fa-paper-plane"></i>';
    submitButton.classList.add('sending');

    emailjs.sendForm('service_59bwpcv', 'template_dh4cnlc', this)
        .then(function(response) {
            console.log('SUCCESS!', response.status, response.text);
            submitButton.innerHTML = 'Message Sent <i class="fa fa-check"></i>';
            
            setTimeout(function() {
                submitButton.innerHTML = originalText + ' <i class="fa fa-paper-plane"></i>';
                submitButton.disabled = false;
                submitButton.classList.remove('sending');
            }, 3000);
        }, function(error) {
            console.log('FAILED...', error);
            submitButton.innerHTML = 'Failed to Send <i class="fa fa-times"></i>';
            
            setTimeout(function() {
                submitButton.innerHTML = originalText + ' <i class="fa fa-paper-plane"></i>';
                submitButton.disabled = false;
                submitButton.classList.remove('sending');
            }, 3000);
        });
});


document.addEventListener('DOMContentLoaded', function() {
    var homeLink = document.getElementById('homeLink');
    homeLink.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent the default anchor behavior
        window.location.href = '#home'; // Navigate to #home
        setTimeout(function() {
            location.reload(); // Refresh the page after a short delay
        }, 100);
    });
});
