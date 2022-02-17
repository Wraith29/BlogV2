let nav_list = document.querySelector('ul#navbar-items');

let links = [
    '/',
    '/profile'
]

if (!links.includes(window.location.pathname)) {
    for (let list_item of nav_list.children) {
        let link = list_item.querySelector('a.nav-link');
        link.classList.remove('active');
        sessionStorage.setItem('active_link', null);
    }
}

for (let child of nav_list.children) {
    let link = child.querySelector('a.nav-link');
    let path = link.href;
    
    if (sessionStorage.getItem('active_link') === link.id) {
        link.classList.add('active');
    } else {
        link.classList.remove('active');
    }

    link.addEventListener('click', (ev) => {
        ev.preventDefault();
        sessionStorage.setItem('active_link', link.id)
        window.location = path;
    });
}