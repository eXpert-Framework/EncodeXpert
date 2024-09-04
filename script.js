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

document.addEventListener('DOMContentLoaded', function() {
    // Find all dropdown buttons
    var dropdowns = document.querySelectorAll('.dropdown');

    // Attach click event to each dropdown button
    dropdowns.forEach(function(dropdown) {
        var button = dropdown.querySelector('.dropbtn');
        button.addEventListener('click', function() {
            // Toggle the "show" class on the dropdown content
            dropdown.classList.toggle('show');
        });
    });

    // Close the dropdown if the user clicks outside of it
    window.addEventListener('click', function(event) {
        dropdowns.forEach(function(dropdown) {
            if (!dropdown.contains(event.target)) {
                dropdown.classList.remove('show');
            }
        });
    });
});
