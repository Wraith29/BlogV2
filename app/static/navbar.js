const navbar = document.querySelector("nav#navbar");

const links = ["/", "/profile/all", "/auth/login/", "/auth/register/"];

const link_associations = [
  ["/", "home-link"],
  ["/profile/all", "profiles-link"],
  [
    `/profile/${JSON.parse(sessionStorage.getItem("current_user")).id}`,
    "profile-link",
  ],
  ["/auth/login/", "login-link"],
  ["/auth/register/", "register-link"],
];

for (let link of link_associations) {
  if (
    window.location.pathname === link[0] &&
    sessionStorage.getItem("active_link") !== link[1]
  ) {
    console.log("Setting highlighted link");
    sessionStorage.setItem("active_link", link[1]);
  }
}

let current_user = JSON.parse(sessionStorage.getItem("current_user"));
links.push(`/profile/${current_user.id}`);

for (let child of navbar.children) {
  for (let sub_child of child.children) {
    let link = sub_child.querySelector("a.nav-link");
    if (!links.includes(window.location.pathname)) {
      link.classList.remove("active");
      sessionStorage.setItem("active_link", null);
    }

    if (sessionStorage.getItem("active_link") === link.id) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }

    link.addEventListener("click", (event) => {
      event.preventDefault();
      sessionStorage.setItem("active_link", link.id);
      window.location = link.href;
    });
  }
}
