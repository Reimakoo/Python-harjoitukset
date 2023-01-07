let list = ['First item', 'Second item', 'Third item']
let element = document.getElementById('target')

for (let i = 0; i !== list.length; i++) {
    let list_item = document.createElement('li')
    list_item.innerText = list[i]
    element.appendChild(list_item)

    if (i === 1) {
        list_item.classList.add('my-item')
    }
}