// let nav_list = document.querySelector('ul#navbar-items');

// let links = [
//     '/',
//     '/profile'
// ]

// if (!links.includes(window.location.pathname)) {
//     for (let list_item of nav_list.children) {
//         let link = list_item.querySelector('a.nav-link');
//         link.classList.remove('active');
//         sessionStorage.setItem('active_link', null);
//     }
// }

const navbar = document.querySelector('nav#navbar');

for ( let child of navbar.children ) {
    for ( let sub_child of child.children ) {
        console.log(sub_child);
        console.log(sub_child.querySelector('a.nav-link'));
        let link = sub_child.querySelector('a.nav-link');
        if ( sessionStorage.getItem('active_link') === link.id ) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }

        link.addEventListener('click', (e) => {
            e.preventDefault();
            sessionStorage.setItem( 'active_link', link.id );
            window.location = link.href;
        })
    }
}