function showSection(sectionId) {
    const sections = document.querySelectorAll('main > section');
    sections.forEach(section => {
        section.classList.add('section-hidden');
        section.classList.remove('section-visible');
    });

    const selectedSection = document.getElementById(sectionId);
    selectedSection.classList.add('section-visible');
    selectedSection.classList.remove('section-hidden');
}
