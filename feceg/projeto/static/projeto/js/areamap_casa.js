window.addEventListener('load', () => {
  const maps = document.querySelectorAll('map');
  maps.forEach((map) => {
    map.addEventListener('click', changeInfo);
  });
});

function changeInfo(e) {
  const root = document.querySelector('.root');
  const { alt, title } = e.target;
  const { text } = e.target.dataset;
  e.preventDefault();

  if (root.style.display == 'none') {
    root.querySelector('.main').textContent = `${alt} - ${title}`;
    root.querySelector('.text').textContent = text;
    const image = root.querySelector('.main-img');
    image.src = `/static/projeto/img/casa/${title}.png`;

    image.addEventListener('load', () => {
      root.style.display = 'block';
    });

    root.querySelector('.close-button').addEventListener('click', changeInfo);
    root.querySelector('.button').addEventListener('click', changeInfo);
  } else root.style.display = 'none';
}
