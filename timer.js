// Presentation pacing uses equal time per slide, independent of speaker notes.
class PresentationTimer {
 constructor(clock, controls, translate, reveal) {
  this.clock=clock;this.controls=controls;this.tr=translate;this.reveal=reveal;
  this.index=null;this.count=1;this.target=20;this.auto=true;this.mode="remaining";
  this.elapsed=0;this.running=false;this.started=false;
  this.anchor=performance.now();this.phase=this.anchor;
  try { const saved=JSON.parse(localStorage.getItem('openmapstack-timer-settings'));
   if(saved){this.target=Math.max(1,Math.min(180,Number(saved.target)||20));this.auto=saved.auto!==false;if(["remaining","elapsed","clock"].includes(saved.mode))this.mode=saved.mode;}
  } catch {}
  clock.innerHTML='<svg viewBox="0 0 80 80" aria-hidden="true"><circle class="timer-track" cx="40" cy="40" r="36"/><circle class="timer-time" cx="40" cy="40" r="36" pathLength="100"/><circle class="timer-track timer-inner" cx="40" cy="40" r="30"/><circle class="timer-slides timer-inner" cx="40" cy="40" r="30" pathLength="100"/></svg><span class="timer-readout" aria-hidden="true"><span class="timer-strip"><span class="timer-count"><strong></strong><small></small></span><span class="timer-remaining"></span></span></span>';
  controls.innerHTML='<label class="timer-mode-field"><span id="timer-mode-label"></span><select id="timer-mode"><option value="remaining"></option><option value="elapsed"></option><option value="clock"></option></select></label><button class="btn" id="timer-start"></button><button class="btn" id="timer-reset"></button><label><span id="timer-target-label"></span> <input id="timer-target" type="number" min="1" max="180"> min</label><label><input id="timer-auto" type="checkbox"><span id="timer-auto-label"></span></label>';
  this.targetInput=controls.querySelector('#timer-target');this.targetInput.value=this.target;
  this.modeInput=controls.querySelector("#timer-mode");this.modeInput.value=this.mode;
  this.modeInput.addEventListener("change",()=>{this.mode=this.modeInput.value;this.phase=performance.now()-3000;this.save();this.draw();});
  this.autoInput=controls.querySelector('#timer-auto');this.autoInput.checked=this.auto;
  clock.addEventListener('click',event=>{reveal(5000);if(event.detail)clock.blur();else controls.querySelector('button').focus();});
  controls.querySelector('#timer-start').addEventListener('click',()=>{this.elapsed=this.spent();this.running=!this.running;this.started=true;this.anchor=performance.now();this.draw();});
  controls.querySelector('#timer-reset').addEventListener('click',()=>{this.elapsed=0;this.running=false;this.started=false;this.phase=performance.now();this.draw();});
  this.targetInput.addEventListener('change',()=>{this.target=Math.max(1,Math.min(180,Number(this.targetInput.value)||20));this.targetInput.value=this.target;this.save();this.draw();});
  this.autoInput.addEventListener('change',()=>{this.auto=this.autoInput.checked;this.save();this.draw();});
  this.interval=setInterval(()=>this.draw(),100);
 }
 save(){try{localStorage.setItem('openmapstack-timer-settings',JSON.stringify({target:this.target,auto:this.auto,mode:this.mode}));}catch{}}
 spent(){return this.elapsed+(this.running?(performance.now()-this.anchor)/1000:0);}
 update(index,count){
  if(this.index!==null&&index!==this.index){
   this.phase=performance.now();
   if(this.auto&&!this.started){this.started=true;this.running=true;this.anchor=performance.now();}
  }
  this.index=index;this.count=count;this.draw();
 }
 format(seconds){const n=Math.ceil(Math.abs(seconds));return `${seconds<0?'+':''}${Math.floor(n/60)}:${String(n%60).padStart(2,'0')}`;}
 draw(){
  if(this.index===null)return;
  const tr=this.tr,e=this.spent(),total=this.target*60,unit=total/this.count;
  const delta=e-(this.index+.5)*unit,remaining=total-e;
  const pace=!this.started?'idle':e>total||delta>2*unit?'slow':delta>unit?'late':delta < -unit?'fast':'on-time';
  this.clock.dataset.pace=pace;
  this.clock.querySelector('.timer-slides').setAttribute('stroke-dasharray',`${(this.index+1)/this.count*100} 100`);
  this.clock.querySelector('.timer-time').setAttribute('stroke-dasharray',`${Math.min(100,e/total*100)} 100`);
  const showTime=(this.started||this.mode==="clock")&&Math.floor((performance.now()-this.phase)/3000)%2===1;
  this.clock.classList.toggle('shows-time',showTime);
  this.clock.querySelector('strong').textContent=this.index+1;
  this.clock.querySelector('small').textContent='/'+this.count;
  const now=new Date();
  const timeText=this.mode==='clock'?`${String(now.getHours()).padStart(2,'0')}:${String(now.getMinutes()).padStart(2,'0')}`:this.mode==='elapsed'?this.format(Math.floor(e)):this.format(remaining);
  const timeLabel=this.mode==='clock'?tr('Kellaaeg','Local time'):this.mode==='elapsed'?tr('Aega algusest','Elapsed time'):remaining<0?tr('Üle aja','Over time'):tr('Aega lõpuni','Time remaining');
  const readout=this.clock.querySelector('.timer-remaining');readout.textContent=timeText;
  readout.classList.toggle('timer-long',timeText.length>5);
  const status={idle:tr('Valmis','Ready'),fast:tr('Graafikust ees','Ahead of schedule'),'on-time':tr('Graafikus','On schedule'),late:tr('Graafikust maas','Behind schedule'),slow:tr('Liiga aeglane','Too slow')}[pace];
  this.clock.setAttribute('aria-label',`${tr('Slaid','Slide')} ${this.index+1}/${this.count}. ${timeLabel} ${timeText}. ${status}. ${tr('Näita juhtnuppe','Show controls')}`);
  this.controls.querySelector('#timer-start').textContent=this.running?tr('Paus','Pause'):this.started?tr('Jätka','Resume'):tr('Käivita','Start');
  this.controls.querySelector('#timer-reset').textContent=tr('Lähtesta aeg','Reset timer');
  this.controls.querySelector('#timer-target-label').textContent=tr('Kestus','Duration');
  this.controls.querySelector('#timer-mode-label').textContent=tr('Ajanäit','Time display');
  for(const [value,et,en] of [['remaining','Aeg lõpuni','Time remaining'],['elapsed','Aeg algusest','Elapsed time'],['clock','Kellaaeg (HH:MM)','Local time (HH:MM)']])this.modeInput.querySelector(`[value="${value}"]`).textContent=tr(et,en);
  this.targetInput.setAttribute('aria-label',tr('Sihtaeg minutites','Target time in minutes'));
  this.controls.querySelector('#timer-auto-label').textContent=tr('Automaatne start','Auto start');
 }
}
