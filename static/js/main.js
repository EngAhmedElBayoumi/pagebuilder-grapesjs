const openNavBtn = document.getElementById("openSideBtn");
const navOverlay = document.getElementById("navOverlay");
const sideNav = document.getElementById("sideNav");
const exitNavBtn = document.getElementById("exitNavBtn");

//seervices nav
const openServNavBtn = document.getElementById("openServNavBtn");
const servNav = document.getElementById("servNav");
const closeServNavBtn = document.getElementById("closeServNavBtn");

openNavBtn.addEventListener("click", function () {
  navOverlay.classList.add("active");
  sideNav.classList.add("active");
});
exitNavBtn.addEventListener("click", function () {
  navOverlay.classList.remove("active");
  sideNav.classList.remove("active");
});
navOverlay.addEventListener("click", function () {
  navOverlay.classList.remove("active");
  sideNav.classList.remove("active");
  servNav.classList.remove("active");
});
