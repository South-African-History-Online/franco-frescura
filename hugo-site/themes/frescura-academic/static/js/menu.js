/**
 * Franco Frescura Archive - Navigation JavaScript
 * Mobile-first interactive menu functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navMenu = document.getElementById('navMenu');
    const body = document.body;
    const dropdownItems = document.querySelectorAll('.nav-item.has-dropdown > .nav-link');

    // Check if we're on mobile
    const isMobile = () => window.innerWidth <= 767;

    /**
     * Toggle mobile menu
     */
    function toggleMobileMenu() {
        const isActive = mobileMenuToggle.classList.contains('active');

        mobileMenuToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        body.classList.toggle('menu-open');

        // Update ARIA attributes
        mobileMenuToggle.setAttribute('aria-expanded', !isActive);
    }

    /**
     * Close mobile menu
     */
    function closeMobileMenu() {
        mobileMenuToggle.classList.remove('active');
        navMenu.classList.remove('active');
        body.classList.remove('menu-open');
        mobileMenuToggle.setAttribute('aria-expanded', 'false');

        // Close all dropdowns
        document.querySelectorAll('.dropdown-open').forEach(item => {
            item.classList.remove('dropdown-open');
        });
    }

    // Mobile menu toggle click
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            toggleMobileMenu();
        });
    }

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (isMobile() && !event.target.closest('.site-header') && navMenu.classList.contains('active')) {
            closeMobileMenu();
        }
    });

    // Prevent menu from closing when clicking inside
    if (navMenu) {
        navMenu.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }

    /**
     * Handle dropdown menus
     */
    dropdownItems.forEach(function(link) {
        link.addEventListener('click', function(e) {
            if (isMobile()) {
                e.preventDefault();
                const parent = this.parentElement;
                const wasOpen = parent.classList.contains('dropdown-open');

                // Close other dropdowns
                document.querySelectorAll('.dropdown-open').forEach(item => {
                    if (item !== parent) {
                        item.classList.remove('dropdown-open');
                    }
                });

                // Toggle current dropdown
                parent.classList.toggle('dropdown-open');
            }
        });
    });

    /**
     * Close menu on navigation link click (mobile)
     */
    const navLinks = navMenu.querySelectorAll('a:not(.nav-item.has-dropdown > .nav-link)');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (isMobile()) {
                closeMobileMenu();
            }
        });
    });

    /**
     * Handle window resize
     */
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            if (!isMobile()) {
                closeMobileMenu();
            }
        }, 250);
    });

    /**
     * Keyboard navigation support
     */
    document.addEventListener('keydown', function(e) {
        // Close menu on Escape key
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            closeMobileMenu();
            mobileMenuToggle.focus();
        }
    });

    /**
     * Smooth scroll for anchor links
     */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerOffset = 120;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                if (isMobile() && navMenu.classList.contains('active')) {
                    closeMobileMenu();
                }
            }
        });
    });

    /**
     * Add animation to cards on scroll
     */
    if ('IntersectionObserver' in window) {
        const cardObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateY(20px)';

                    setTimeout(() => {
                        entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, 100);

                    cardObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        document.querySelectorAll('.card').forEach(card => {
            cardObserver.observe(card);
        });
    }

    /**
     * Log info
     */
    console.log('%cFranco Frescura Archive', 'font-size: 18px; font-weight: bold; color: #B8662C;');
    console.log('%cModern Mobile-First Design', 'font-size: 12px; color: #5C5447;');
});
