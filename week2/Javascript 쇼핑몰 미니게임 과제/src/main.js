// Fetch the items from the JSON file
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

// 리스트 업데이트
function displayItems(items) {
    const container = document.querySelector('.items');
    const html = items.map(item => createHTMLString(item)).join('');
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

// HTML 만들기
function createHTMLString(item) {
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

// 버튼 클릭 시 이벤트
function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key ==null || value == null) {
        return;
    }

    const filtered = items.filter(item => item[key] === value);
    displayItems(filtered);
}

// 이벤트 실행 - 로고, 버튼
function setEventListners(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', () => onButtonClick(event, items));
}

/// main
loadItems()
 .then(items => {
    displayItems(items);
    setEventListners(items);
    })
 .catch(console.log)