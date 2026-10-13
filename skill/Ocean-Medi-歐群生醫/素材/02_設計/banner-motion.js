(() => {
  const mode = new URLSearchParams(location.search).get('motion');
  if (!['on', 'reduce'].includes(mode)) return;
  document.body.classList.remove('full-frame');
  document.body.classList.add('motion-preview');
  const host = document.querySelector('#standalone');
  host.replaceChildren(frame('start'));
  const scene = host.querySelector('.scene');
  // Decorative bubbles stay in edge zones, outside copy and subject details.
  const bubbles = document.createElement('div');
  bubbles.className = 'air-bubbles';
  bubbles.setAttribute('aria-hidden', 'true');
  const bubbleLayout = [
    [2,25,1.2,7,-2,12], [3.4,68,2.1,10,-5,-16],
    [12,14,1.3,9,-3,18], [29,17,2.5,12,-7,-20],
    [38,8,1.1,8,-1,14], [19,87,1.5,11,-6,20],
    [96,24,1.5,9,-4,-12], [97,52,2.2,13,-8,-20],
    [94,85,1.2,8,-3,12]
  ];
  for (const [x,y,size,duration,delay,drift] of bubbleLayout) {
    const bubble = document.createElement('span');
    bubble.className = 'air-bubble';
    for (const [key,value] of Object.entries({x:x+'%',y:y+'%',size:size+'cqw',duration:duration+'s',delay:delay+'s',drift:drift+'px'})) bubble.style.setProperty('--'+key,value);
    bubbles.append(bubble);
  }
  scene.append(bubbles);
  let sceneVisible = true;
  function pauseBubbles(){scene.classList.toggle('bubbles-paused',!sceneVisible || document.hidden)}
  const visibilityObserver = new IntersectionObserver(([entry])=>{sceneVisible=entry.isIntersecting;pauseBubbles()});
  visibilityObserver.observe(scene);
  document.addEventListener('visibilitychange',pauseBubbles);
  const elements = Object.fromEntries(['lens', 'lens-small', 'horizon', 'distance'].map(name => [name, scene.querySelector('.' + name)]));
  const photo = scene.querySelector('.picture img');
  const notes = document.createElement('div');
  notes.className = 'trial-notes';
  notes.innerHTML = `<p>OCEAN MEDI / BANNER MOTION STUDY / 2560 × 1280</p>
    <h2>Banner 動態試做，以下是試做導覽落點，非完整首頁。</h2>
    <p>往下捲動：前景靠近再退開；往回捲動：沿原路還原。正文與操作不跟著漂移。英文依客戶提供的對照表，Excel 原檔未更動。</p>
    <p><a href="?motion=reduce">檢視減少動態版本</a> · <a href="?motion=on">一般動態</a> · <a href="?">返回分鏡提案</a></p>
    <section id="about"><h2 lang="en">About OCEAN</h2><p lang="en">With a Heart to Protect Our Loved Ones<br>Creating a Healthier, Hydrogen-Infused Life</p></section>
    <section id="applications"><h2 lang="en">Comprehensive Protection</h2><p lang="en">Personal Wellness / Environmental Protection / Hydrogen Energy</p></section>
    <section id="innovation"><h2 lang="en">Innovation &amp; Patents</h2><p>此輪僅驗證 Banner 導覽可即時操作，完整內容於首頁階段整合。</p></section>
    <section id="partnership"><h2 lang="en">Partnership Inquiry</h2><p><a href="mailto:sales@octec.com.tw">sales@octec.com.tw</a></p><p>來源：工作表1 C39。此按鈕開啟郵件程式，不會自動寄出。</p></section>`;
  document.body.append(notes);
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  const config = {hold: .2, peak: .65, scrollScreens: .6};
  const clamp = value => Math.max(0, Math.min(1, value));
  const ease = t => t * t * (3 - 2 * t);
  const mix = (a, b, t) => a + (b - a) * t;
  const poses = [[0,0,1,0,0],[ -15,29,1.03,17,-35],[10,-8,1,-15,8]];
  let distance = innerHeight * config.scrollScreens;
  let scheduled = false;
  function render() {
    scheduled = false;
    const reduced = preference.matches || mode === 'reduce';
    document.body.classList.toggle('is-reduced', reduced);
    const progress = reduced ? 1 : clamp(scrollY / distance);
    const second = progress > config.peak;
    const t = ease(clamp(second ? (progress-config.peak)/(1-config.peak) : (progress-config.hold)/(config.peak-config.hold)));
    const from = poses[second ? 1 : 0], to = poses[second ? 2 : 1];
    const pose = from.map((value, index) => mix(value, to[index], t));
    elements.lens.style.transform = `translate(${pose[0]}%,${pose[1]}%) scale(${pose[2]})`;
    elements['lens-small'].style.transform = `translate(${pose[3]}%,${pose[4]}%)`;
    elements.horizon.style.transform = `translateX(${-12*progress}px) rotate(-25deg)`;
    photo.style.transform = `translateY(${-8*progress}px) scale(${1.04+.01*progress})`;
    scene.dataset.progress = progress.toFixed(3);
  }
  function requestRender(){if(!scheduled){scheduled=true;requestAnimationFrame(render)}}
  function resize(){distance=innerHeight*config.scrollScreens;requestRender()}
  addEventListener('scroll',requestRender,{passive:true});
  addEventListener('resize',resize,{passive:true});
  preference.addEventListener('change',requestRender);
  render();
})();
