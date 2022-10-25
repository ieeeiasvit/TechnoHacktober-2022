let controller=new ScrollMagic.Controller();
let timeline=new TimelineMax();

timeline
.to(".girl", 10, { y: -200 })
.fromTo(".bg1", { y: -50 }, { y: 0, duration: 15 }, "-=10")
.to(".content", 10, { top: "0%" }, "-=10")
  .fromTo(".content-images", { opacity: 0 }, { opacity: 1, duration: 3 })
  .fromTo(".text", { opacity: 0 }, { opacity: 1, duration: 3 });

let scene = new ScrollMagic.Scene({
  triggerElement: "section",
  duration: "300%",
  triggerHook: 0,
})
  .setTween(timeline)
  .setPin("section")
  .addTo(controller);
