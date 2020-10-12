const toggleButton = document.getElementsByClassName("toggle-button")[0];
const navBarLinksWapper = document.getElementsByClassName(
  "nav-links-wrapper"
)[0];
toggleButton.addEventListener("click", () => {
  navBarLinksWapper.classList.toggle("active");
});
