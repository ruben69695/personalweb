const menu = document.getElementById('menu');
const alignedCenterClassName = 'align-self-center';

function reportWindowSize() {
  if (window.innerWidth > 875) {
    menu.classList.add(alignedCenterClassName);
    return;
  }

  menu.classList.remove(alignedCenterClassName);
}

function loadHandler() {
    reportWindowSize();
}

window.onresize = reportWindowSize;
window.onload = loadHandler;