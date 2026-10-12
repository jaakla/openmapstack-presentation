// A local canvas and camera: the same deck works online and in the offline HTML.
const PREZI_FRAME = {width:1440,height:900,gapX:260,gapY:250,columns:6};
function preziPositions(count,columns=PREZI_FRAME.columns){
 const {width,height,gapX,gapY}=PREZI_FRAME;
 return Array.from({length:count},(_,index)=>{
  const row=Math.floor(index/columns),column=row%2?columns-1-index%columns:index%columns;
  return {x:column*(width+gapX),y:row*(height+gapY),width,height};
 });
}

class PreziView {
 constructor(stage,onSelect){
  this.stage=stage;this.onSelect=onSelect;this.index=-1;this.overview=false;
  this.motion=matchMedia('(prefers-reduced-motion: reduce)');
  this.onMotionChange=()=>{if(this.world)this.moveTo(this.viewCamera(),false);};
  this.motion.addEventListener('change',this.onMotionChange);
  this.resizeObserver=new ResizeObserver(()=>{
   const size=`${stage.clientWidth},${stage.clientHeight}`;
   if(size===this.size)return;this.size=size;
   if(this.world){this.arrange();this.updateLabels();this.moveTo(this.viewCamera(),false);}
  });
  this.size=`${stage.clientWidth},${stage.clientHeight}`;
  this.resizeObserver.observe(stage);
 }

 mount(slides){
  this.stop();this.slides=slides;
  this.stage.classList.add('prezi-stage');
  this.stage.innerHTML='<div class="prezi-world"></div>';
  this.world=this.stage.querySelector('.prezi-world');
  const route=document.createElementNS('http://www.w3.org/2000/svg','svg');
  route.setAttribute('class','prezi-route');route.setAttribute('aria-hidden','true');
  const path=document.createElementNS(route.namespaceURI,'polyline');
  route.append(path);this.world.append(route);
  this.arrange();
  this.positions.forEach((position,index)=>{
   const frame=document.createElement('section');frame.className='prezi-frame';
   frame.style.left=position.x+'px';frame.style.top=position.y+'px';
   frame.dataset.index=index;this.world.append(frame);this.drawFrame(index,false);
  });
  this.world.addEventListener('click',event=>{
   const choice=event.target.closest('[data-prezi-go]');
   if(choice&&this.overview)this.onSelect(Number(choice.dataset.preziGo));
  });
  this.updateLabels();
 }

 arrange(){
  // Portrait screens get larger thumbnails instead of six cramped columns.
  const columns=this.stage.clientWidth<700&&this.stage.clientHeight>this.stage.clientWidth?3:PREZI_FRAME.columns;
  const {width,height}=PREZI_FRAME;
  this.positions=preziPositions(this.slides.length,columns);
  this.bounds={x:-80,y:-80,width:Math.max(...this.positions.map(p=>p.x+width))+160,
               height:Math.max(...this.positions.map(p=>p.y+height))+240};
  for(const frame of this.world.querySelectorAll('.prezi-frame')){
   const position=this.positions[Number(frame.dataset.index)];
   frame.style.left=position.x+'px';frame.style.top=position.y+'px';
  }
  const route=this.world.querySelector('.prezi-route');
  route.setAttribute('width',this.bounds.width);route.setAttribute('height',this.bounds.height);
  route.querySelector('polyline').setAttribute('points',this.positions.map(p=>`${p.x+width/2},${p.y+height/2}`).join(' '));
 }

 drawFrame(index,active){
  const frame=this.world.querySelector(`[data-index="${index}"]`),slide=this.slides[index];
  frame.classList.toggle('is-current',active);
  const article=document.createElement('article');
  article.className='slide prezi-slide';article.innerHTML=slide.html();
  if(active){
   article.id='prezi-active';article.setAttribute('aria-labelledby','slide-title');
   const heading=article.querySelector('h1,h2');if(heading)heading.id='slide-title';
   this.active=article;
  }else{
   // Thumbnails must not duplicate live control IDs or enter the tab order.
   article.classList.add('prezi-preview');article.inert=true;article.setAttribute('aria-hidden','true');
   for(const node of article.querySelectorAll('[id],[for],[aria-labelledby],[aria-describedby]')){
    for(const name of ['id','for','aria-labelledby','aria-describedby'])node.removeAttribute(name);
   }
  }
  const choice=document.createElement('button');choice.className='prezi-card-go';
  choice.dataset.preziGo=index;choice.hidden=!this.overview;
  choice.setAttribute('aria-label',`${tr('Ava slaid','Open slide')} ${index+1}: ${slide.title}`);
  choice.setAttribute('aria-current',String(active));
  choice.innerHTML=`<span class="prezi-card-number">${String(index+1).padStart(2,'0')}</span><span class="prezi-card-caption">${esc(slide.title)}</span>`;
  frame.replaceChildren(article,choice);
 }

 show(slides,index,refresh=false,overview=false){
  const previous=this.index,wasOverview=this.overview;
  const rebuilt=refresh||this.slides!==slides||!this.world?.isConnected;
  if(rebuilt)this.mount(slides);
  else if(previous!==index&&previous>=0)this.drawFrame(previous,false);
  this.index=index;
  this.overview=overview;
  this.drawFrame(index,true);this.updateLabels();
  const changed=previous>=0&&previous!==index;
  const via=changed&&!wasOverview&&!rebuilt?this.travelCamera(previous,index):null;
  this.moveTo(this.viewCamera(),!rebuilt&&(changed||wasOverview!==this.overview),via);
 }

 updateLabels(){
  if(!this.world)return;
  this.stage.classList.toggle('is-overview',this.overview);
  for(const choice of this.world.querySelectorAll('[data-prezi-go]'))choice.hidden=!this.overview;
  this.world.style.setProperty('--prezi-label-size',`${Math.max(38,12/this.fit(this.bounds).scale)}px`);
  if(this.active){this.active.inert=this.overview;this.active.setAttribute('aria-hidden',String(this.overview));}
 }

 fit(bounds,maxScale=Infinity){
  const width=this.stage.clientWidth,height=this.stage.clientHeight;
  const scale=Math.max(.01,Math.min((width-40)/bounds.width,(height-100)/bounds.height,maxScale));
  return {scale,x:width/2-(bounds.x+bounds.width/2)*scale,
          y:(height+40)/2-(bounds.y+bounds.height/2)*scale};
 }
 viewCamera(){return this.fit(this.overview?this.bounds:this.positions[this.index]);}
 travelCamera(from,to){
  const a=this.positions[from],b=this.positions[to];
  const bounds={x:Math.min(a.x,b.x)-100,y:Math.min(a.y,b.y)-100,
                width:Math.abs(a.x-b.x)+a.width+200,height:Math.abs(a.y-b.y)+a.height+200};
  return this.fit(bounds,this.fit(b).scale*.43);
 }
 transform(camera){return `translate(${camera.x}px,${camera.y}px) scale(${camera.scale})`;}

 moveTo(camera,animate,via=null){
  this.stop();
  const start=getComputedStyle(this.world).transform,target=this.transform(camera);
  this.world.style.transform=target;
  if(!animate||this.motion.matches||!this.world.animate){this.setMoving(false);return;}
  const frames=[{transform:start,offset:0}];
  if(via)frames.push({transform:this.transform(via),offset:.45});
  frames.push({transform:target,offset:1});
  this.setMoving(true);
  const animation=this.world.animate(frames,{duration:via?1150:750,easing:'cubic-bezier(.4,0,.2,1)'});
  this.animation=animation;
  animation.onfinish=()=>{
   if(this.animation!==animation)return;
   this.animation=null;animation.cancel();this.setMoving(false);
  };
 }
 setMoving(moving){
  this.stage.classList.toggle('is-moving',moving);this.stage.setAttribute('aria-busy',String(moving));
  if(this.active)this.active.inert=moving||this.overview;
 }
 stop(){
  if(!this.animation)return;
  this.world.style.transform=getComputedStyle(this.world).transform;
  this.animation.onfinish=null;this.animation.cancel();this.animation=null;
 }
 destroy(){
  this.stop();this.resizeObserver.disconnect();this.motion.removeEventListener('change',this.onMotionChange);
  this.stage.classList.remove('prezi-stage','is-overview','is-moving');this.stage.removeAttribute('aria-busy');
 }
}
