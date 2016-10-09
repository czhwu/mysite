/**
 * Created by caozhengwu on 2016-10-09.
 */
marque(320,196,"icefable1","box1left")
var scrollElem;
var stopscroll;
var stoptime;
var preTop;
var leftElem;
var currentTop;
var marqueesHeight;
function marque(width,height,marqueName,marqueCName){
    try{
      marqueesHeight = height;
      stopscroll     = false;

      scrollElem = document.getElementById("adsfar");
      with(scrollElem){
        style.width     = width;
        style.height    = marqueesHeight;
        style.overflow  = 'hidden';
        noWrap          = true;
      }

      scrollElem.onmouseover = new Function('stopscroll = true');
      scrollElem.onmouseout  = new Function('stopscroll = false');

      preTop     = 0;
      currentTop = 0;
      stoptime   = 0;

      leftElem = document.getElementById("adsfar");
      scrollElem.appendChild(leftElem.cloneNode(true));

      init_srolltext();

    }catch(e) {}
}
function init_srolltext(){
  scrollElem.scrollTop = 0;
  setInterval('scrollUp()', 18);
}

function scrollUp(){
  if(stopscroll) return;
  currentTop += 1;
  if(currentTop == marqueesHeight+1) {
    stoptime += 1;
    currentTop -= 1;
    if(stoptime == (marqueesHeight)*1) {//停顿时间
      currentTop = 0;
      stoptime = 0;
    }
  }else{

    preTop = scrollElem.scrollTop;
    scrollElem.scrollTop += 1;
    if(preTop == scrollElem.scrollTop){
      scrollElem.scrollTop = marqueesHeight;
      scrollElem.scrollTop += 1;
    }
  }
}