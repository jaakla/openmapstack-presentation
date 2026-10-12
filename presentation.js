// One logical slide size keeps text, images and spacing proportional on screen.
const SLIDE_SIZE={width:1440,height:900};
class SlideView {
 constructor(stage,onSelect){
  this.stage=stage;this.onSelect=onSelect;this.printing=false;
  this.resizeObserver=new ResizeObserver(()=>this.fit());
  this.resizeObserver.observe(stage);
  document.addEventListener('fullscreenchange',()=>this.fit());
 }
 show(slides,index,overview){
  this.printing=false;this.overview=overview;
  this.stage.classList.toggle('overview-stage',overview);
  if(overview){
   const grid=document.createElement('div');grid.className='overview-grid';
   slides.forEach((slide,i)=>{
    const button=document.createElement('button');button.className='overview-card';
    button.dataset.overviewGo=i;button.setAttribute('aria-current',String(i===index));
    button.setAttribute('aria-label',`${tr('Ava slaid','Open slide')} ${i+1}: ${slide.title}`);
    const preview=document.createElement('div');preview.className='overview-preview';
    preview.inert=true;preview.setAttribute('aria-hidden','true');
    const article=document.createElement('article');article.className='slide canvas-slide';
    article.innerHTML=slide.html();
    // Preview content has no live controls, duplicated IDs or focus targets.
    for(const node of article.querySelectorAll('[id],[for],[aria-labelledby],[aria-describedby]')){
     for(const attr of ['id','for','aria-labelledby','aria-describedby'])node.removeAttribute(attr);
    }
    preview.append(article);
    const caption=document.createElement('span');caption.className='overview-caption';
    caption.textContent=`${String(i+1).padStart(2,'0')} · ${slide.title}`;
    button.append(preview,caption);button.addEventListener('click',()=>this.onSelect(i));
    grid.append(button);
   });
   this.stage.replaceChildren(grid);
  }else{
   this.stage.innerHTML=`<article class="slide" aria-labelledby="slide-title">${slides[index].html()}</article>`;
   const heading=this.stage.querySelector('h1,h2');if(heading)heading.id='slide-title';
  }
  this.fit();
 }
 fit(){
  if(this.printing)return;
  const scaled=!this.overview&&(this.stage.clientWidth>700||Boolean(document.fullscreenElement));
  this.stage.classList.toggle('scaled-stage',scaled);
  const {width,height}=SLIDE_SIZE;
  const fit=(article,box)=>{
   const scale=Math.min(box.clientWidth/width,box.clientHeight/height);
   article.style.transform=`translate(${(box.clientWidth-width*scale)/2}px,${(box.clientHeight-height*scale)/2}px) scale(${scale})`;
  };
  if(this.overview){
   for(const preview of this.stage.querySelectorAll('.overview-preview'))fit(preview.firstElementChild,preview);
  }else{
   const article=this.stage.firstElementChild;if(!article)return;
   article.classList.toggle('canvas-slide',scaled);
   if(scaled)fit(article,this.stage);else article.style.removeProperty('transform');
  }
 }
 beforePrint(){
  this.printing=true;this.stage.classList.remove('scaled-stage','overview-stage');
 }
}
