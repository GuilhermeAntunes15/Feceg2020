window.addEventListener('load', () => {
  window.addEventListener('resize', () => {
    let menuButton = document.getElementById('myNav');
    if (menuButton.style.display === 'block') {
      menuButton.style.display = 'none';
    }
  });
});

function changeMenu() {
  let menuButton = document.getElementById('myNav');
  if (menuButton.style.display === 'block') {
    menuButton.style.display = 'none';
  } else {
    menuButton.style.display = 'block';
  }
}
