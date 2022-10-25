const dino = document.getElementById("dino");
const obstacles = document.getElementById("obstacles");
const points = document.getElementById("points");

function jump() {
  dino.classList.add("jump-animation");
  setTimeout(() => {
    dino.classList.remove("jump-animation");
  }, 500);
}

document.addEventListener("keypress", () => {
  if (!dino.classList.contains("jump-animation")) {
    jump();
  }
});

setInterval(() => {
    points.innerText++;
  const dinoTop = parseInt(
    window.getComputedStyle(dino).getPropertyValue("top")
  );
  const rockLeft = parseInt(
    window.getComputedStyle(obstacles).getPropertyValue("left")
  );
  if (rockLeft < 0) {
    obstacles.style.display = "none";
  } else {
    obstacles.style.display = "";
  }

  if(rockLeft<50 && rockLeft>0 && dinoTop>250){
      alert("You got "+ points.innerText+ " \n\nPlay Again" );
      location.reload();
  }
}, 50);
