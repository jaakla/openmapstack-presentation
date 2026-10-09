// Actual Tartu bridges dashboard screenshots are embedded by build.py.
const IMAGES = __IMAGES__;
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const shot=(key,label)=>`<div class="screenshot-frame"><div class="photo-label">${tr("Päris demo: Tartu Emajõe kergliiklussillad","Actual demo: Tartu bridges · screenshot in Estonian")}</div><button class="photo-button" data-image="${key}" aria-label="${tr("Suurenda ekraanipilti","Enlarge screenshot")}: ${esc(label)}"><img class="photo" src="${IMAGES[key]}" alt="${esc(label)}"></button><p class="caption">${esc(label)}. ${tr("Klõpsa pildil suurendamiseks.","Click the image to enlarge.")}</p></div>`;

// Fixed templates come from layouts.json; all slide wording comes from Markdown.
const DECK = __DECK__;
function slideMarkup(template){
 const components={network:networkGraphic,chart:chartGraphic,metric:metricMarkup,
  'controls-true':()=>demoControls(true),'controls-false':()=>demoControls(false)};
 return template.replace(/<oms-component data-name="([^"]+)"><\/oms-component>/g,(_,name)=>components[name]())
  .replace(/<oms-shot data-key="([^"]+)">([\s\S]*?)<\/oms-shot>/g,(_,key,label)=>{
   const node=document.createElement('template');node.innerHTML=label;
   return shot(key,node.content.textContent);
  }).replace('__BRIDGE_HIDDEN__',demoState.bridge?'':'hidden');
}
const makeSlides=lang=>DECK[lang].map(slide=>({...slide,html:()=>slideMarkup(slide.html)}));
const SLIDES_ET=makeSlides('et');
const SLIDES_EN=makeSlides('en');
