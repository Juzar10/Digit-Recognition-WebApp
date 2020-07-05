window.addEventListener('load', () => {

  const canvas = document.querySelector('#canvas');
  const ctx = canvas.getContext("2d");
  const clear_buttom = document.querySelector("#clear");

  const submit_button = document.querySelector('#submit');
  const result = document.getElementById("result")

  const canvasWidth = 280;
  const canvasHeight = 280;



  canvas.width = canvasWidth;
  canvas.height = canvasHeight;

  clear();

  // let painting
  let painting = false;

  function startPosition() {
    painting = true;
  }

  function finishPosition() {
    painting = false;
    ctx.beginPath();
  }

  function draw(e) {
    if (!painting) {
      return;
    }
    ctx.lineWidth = 30;
    ctx.lineCap = "round";
    ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
  }

  function execute() {

    $.ajax({
      type: 'POST',
      url: "./predict",
      data: {
        img: canvas.toDataURL("image/png").replace('data:image/png;base64,', '')
      },
      success: function(data) {
        result.innerHTML = "The Result in probably " + data
      }

    });
  };



  submit_button.onclick = execute;

  canvas.addEventListener('mousedown', startPosition);
  canvas.addEventListener('mouseup', finishPosition);
  canvas.addEventListener('mousemove', draw);


  clear_buttom.onclick = clear;

  function clear() {
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

  }

});
