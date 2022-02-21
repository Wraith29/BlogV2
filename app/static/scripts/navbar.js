const navbar = document.querySelector('nav#navbar');

const links = [
    '/', '/profile/all', '/auth/login/', '/auth/register/'
]

for ( let child of navbar.children ) {
    for ( let sub_child of child.children ) {
        let link = sub_child.querySelector('a.nav-link');
        if ( !links.includes(window.location.pathname) ) {
            link.classList.remove('active');
            sessionStorage.setItem('active_link', null);
        }

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