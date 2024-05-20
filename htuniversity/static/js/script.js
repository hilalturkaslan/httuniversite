// Butonlara click eventlerini ekleme
document.querySelectorAll('.tab-button').forEach(button => {
    button.addEventListener('click', () => {
        const target = button.getAttribute('data-target');
        // Tüm filterları gizle
        document.querySelectorAll('.filter').forEach(filter => {
            filter.classList.remove('active');
        });
        // Hedef filterı göster
        document.getElementById(target).classList.add('active');
        // Tüm butonları pasif yap
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.classList.remove('active');
        });
        // Seçilen butonu aktif yap
        button.classList.add('active');
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const filters = document.querySelectorAll('.filter');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const target = document.querySelector(button.getAttribute('data-target'));

            filters.forEach(filter => {
                filter.style.display = 'none';
            });

            target.style.display = 'block';
        });
    });
});

function search(inputId, optionId = null) {
    const input = document.getElementById(inputId).value.toLowerCase();
    let optionValue = optionId ? document.getElementById(optionId).value.toLowerCase() : '';
    const resultsDiv = document.querySelector(`#${inputId}`).closest('.filter').querySelector('.search-results');

    // Temporary search results array for demonstration purposes
    const allItems = [
        'e-Yayın 1', 'e-Yayın 2', 'Basılı Yayın 1', 'Basılı Yayın 2',
        'e-Dergi A1', 'e-Dergi B2', 'e-Dergi C3', 'e-Dergi A2'
    ];

    // Filter logic
    let filteredItems = allItems.filter(item => item.toLowerCase().includes(input));
    if (optionId) {
        filteredItems = filteredItems.filter(item => item.toLowerCase().includes(optionValue));
    }

    // Clear previous results
    resultsDiv.innerHTML = '';

    if (filteredItems.length > 0) {
        filteredItems.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.textContent = item;
            resultsDiv.appendChild(itemElement);
        });
    } else {
        const noResultsElement = document.createElement('div');
        noResultsElement.textContent = 'Sonuç bulunamadı';
        resultsDiv.appendChild(noResultsElement);
    }
}
