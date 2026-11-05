
document.addEventListener("DOMContentLoaded", () => {

    // =====================================
    // 1. MENÚ RESPONSIVE
    // =====================================

    const nav = document.querySelector("header nav");

    if (nav) {
        const menuButton = document.createElement("button");

        menuButton.classList.add("menu-toggle");
        menuButton.innerHTML = "☰";
        menuButton.setAttribute("aria-label", "Abrir menú");
        menuButton.setAttribute("aria-expanded", "false");

        nav.parentElement.insertBefore(menuButton, nav);

        menuButton.addEventListener("click", () => {
            const isOpen = nav.classList.toggle("menu-open");

            menuButton.setAttribute("aria-expanded", isOpen);
            menuButton.setAttribute(
                "aria-label",
                isOpen ? "Cerrar menú" : "Abrir menú"
            );

            menuButton.innerHTML = isOpen ? "&times;" : "☰";
        });

        nav.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                nav.classList.remove("menu-open");
                menuButton.setAttribute("aria-expanded", "false");
                menuButton.innerHTML = "☰";
            });
        });
    }


    // =====================================
    // 2. DESPLAZAMIENTO SUAVE
    // =====================================

    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener("click", event => {
            const target = document.querySelector(
                link.getAttribute("href")
            );

            if (target) {
                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });


    // =====================================
    // 3. BOTÓN VOLVER ARRIBA
    // =====================================

    const topButton = document.createElement("button");

    topButton.classList.add("back-to-top");
    topButton.innerHTML = "↑";
    topButton.setAttribute("aria-label", "Volver arriba");

    document.body.appendChild(topButton);

    window.addEventListener("scroll", () => {
        topButton.classList.toggle(
            "visible",
            window.scrollY > 400
        );
    });

    topButton.addEventListener("click", () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });


    // =====================================
    // 4. ANIMACIONES AL DESPLAZARSE
    // =====================================

    const sections = document.querySelectorAll(
        "main section"
    );

    sections.forEach(section => {
        section.classList.add("reveal");
    });

    const revealObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("reveal-visible");
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.12
    });

    sections.forEach(section => {
        revealObserver.observe(section);
    });


    // =====================================
    // 5. RESALTAR SECCIÓN ACTUAL EN EL MENÚ
    // =====================================

    const menuLinks = document.querySelectorAll(
        'header nav a[href^="#"]'
    );

    const sectionObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                menuLinks.forEach(link => {
                    link.classList.toggle(
                        "active",
                        link.getAttribute("href") ===
                        `#${entry.target.id}`
                    );
                });
            }
        });
    }, {
        threshold: 0.4
    });

    document.querySelectorAll("main section[id]").forEach(section => {
        sectionObserver.observe(section);
    });


    // =====================================
    // 6. VALIDACIÓN DEL FORMULARIO
    // =====================================

    const form = document.querySelector(".formulario-contacto");

    if (form) {
        form.addEventListener("submit", event => {

            const requiredFields = form.querySelectorAll("[required]");
            let valid = true;

            requiredFields.forEach(field => {
                field.style.borderColor = "";

                if (!field.value.trim()) {
                    valid = false;
                    field.style.borderColor = "#e63946";
                }
            });

            const email = form.querySelector('input[type="email"]');

            if (email && email.value.trim() && !email.validity.valid) {
                valid = false;
                email.style.borderColor = "#e63946";
            }

            if (!valid) {
                event.preventDefault();
                alert("Por favor, revisa los datos del formulario.");
            }
        });

        form.querySelectorAll("input, textarea").forEach(field => {
            field.addEventListener("input", () => {
                field.style.borderColor = "";
            });
        });
    }


    // =====================================
    // 7. CONTADORES ANIMADOS
    // =====================================

    const counters = document.querySelectorAll("[data-counter]");

    const counterObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const finalValue = Number(counter.dataset.counter);

                if (!Number.isFinite(finalValue)) {
                    counterObserver.unobserve(counter);
                    return;
                }

                const duration = 1500;
                const startTime = performance.now();

                function updateCounter(currentTime) {
                    const progress = Math.min(
                        (currentTime - startTime) / duration,
                        1
                    );

                    counter.textContent = Math.floor(
                        finalValue * progress
                    );

                    if (progress < 1) {
                        requestAnimationFrame(updateCounter);
                    }
                }

                requestAnimationFrame(updateCounter);
                counterObserver.unobserve(counter);
            }
        });
    }, {
        threshold: 0.5
    });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });


    // =====================================
    // 8. AÑO AUTOMÁTICO DEL FOOTER
    // =====================================

    const yearElement = document.querySelector("#current-year");

    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }


    // =====================================
    // 9. BARRA DE PROGRESO DE PÁGINA
    // =====================================

    const progressBar = document.createElement("div");
    progressBar.classList.add("scroll-progress");

    document.body.appendChild(progressBar);

    window.addEventListener("scroll", () => {
        const scrollableHeight =
            document.documentElement.scrollHeight - window.innerHeight;

        const progress = scrollableHeight > 0
            ? (window.scrollY / scrollableHeight) * 100
            : 0;

        progressBar.style.width = `${progress}%`;
    });

});
