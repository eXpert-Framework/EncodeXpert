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

function showSubSection(subSectionId) {
    const subSections = document.querySelectorAll('#requirements > div');
    subSections.forEach(subSection => {
        subSection.classList.add('sub-section-hidden');
        subSection.classList.remove('sub-section-visible');
    });

    const selectedSubSection = document.getElementById(subSectionId);
    selectedSubSection.classList.add('sub-section-visible');
    selectedSubSection.classList.remove('sub-section-hidden');
}
