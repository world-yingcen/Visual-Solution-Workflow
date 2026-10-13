(() => {
  const root = document.documentElement;
  const experience = document.querySelector(".flow-experience");
  const worlds = [...document.querySelectorAll(".world")];
  const copies = [...document.querySelectorAll(".scene-copy")];
  const telemetryItems = [...document.querySelectorAll(".system-telemetry li")];
  const currentScene = document.querySelector(".current-scene");
  const tubePath = document.querySelector(".tube-progress");
  const tubePulse = document.querySelector(".tube-pulse");
  const tubePulseHalo = document.querySelector(".tube-pulse-halo");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const brandImage = document.querySelector(".brand img");
  const whiteLogo = brandImage.getAttribute("src");
  const colorLogo = "../首次設計/01 LOGO_OK/標誌中文置中標準組合_標準色logo.png";
  const updateBrand = (light) => {
    const source = light ? colorLogo : whiteLogo;
    if (brandImage.getAttribute("src") !== source) brandImage.setAttribute("src", source);
  };
  let pathLength = 0;
  let queued = false;

  const clamp = (value, min = 0, max = 1) => Math.min(max, Math.max(min, value));
  const range = (value, start, end) => clamp((value - start) / (end - start));
  const smooth = (value) => {
    const x = clamp(value);
    return x * x * (3 - 2 * x);
  };
  const peak = (value, center, radius) => clamp(1 - Math.abs(value - center) / radius);

  const setActiveScene = (index) => {
    root.classList.toggle("is-air", index > 0 || window.scrollY >= experience.offsetHeight - 104);
    updateBrand(root.classList.contains("is-air"));
    copies.forEach((copy, copyIndex) => copy.classList.toggle("is-active", copyIndex === index));
    telemetryItems.forEach((item, itemIndex) => item.classList.toggle("is-active", itemIndex === index));
    if (currentScene) currentScene.textContent = String(index).padStart(2, "0");
  };

  const initializeTube = () => {
    if (!tubePath) return;
    pathLength = tubePath.getTotalLength();
    tubePath.style.strokeDasharray = `${pathLength}`;
    tubePath.style.strokeDashoffset = `${pathLength}`;
  };

  const updateTube = (progress) => {
    if (!tubePath || !pathLength) return;
    tubePath.style.strokeDashoffset = `${pathLength * (1 - progress)}`;
    const point = tubePath.getPointAtLength(pathLength * progress);
    [tubePulse, tubePulseHalo].forEach((pulse) => {
      if (!pulse) return;
      pulse.setAttribute("cx", point.x.toFixed(2));
      pulse.setAttribute("cy", point.y.toFixed(2));
    });
  };

  const resetReducedMotion = () => {
    root.classList.remove("is-air");
    updateBrand(false);
    root.style.setProperty("--p", "0");
    root.style.setProperty("--portal-scale", "0.72");
    root.style.setProperty("--portal-opacity", "1");
    root.style.setProperty("--hero-opacity", "1");
    root.style.setProperty("--flash-opacity", "0");
    worlds.forEach((world) => {
      world.style.removeProperty("clip-path");
      world.style.removeProperty("transform");
      world.style.removeProperty("filter");
      world.querySelector("img")?.style.removeProperty("transform");
    });
    copies.forEach((copy) => copy.classList.add("is-active"));
  };

  const updateExperience = () => {
    queued = false;
    if (!experience) return;

    if (reducedMotion.matches) {
      resetReducedMotion();
      return;
    }

    const rect = experience.getBoundingClientRect();
    const scrollable = Math.max(1, rect.height - window.innerHeight);
    const progress = clamp(-rect.top / scrollable);
    const portalTravel = smooth(range(progress, 0.075, 0.3));
    const revealWellness = smooth(range(progress, 0.19, 0.35));
    const revealWater = smooth(range(progress, 0.43, 0.58));
    const revealEnergy = smooth(range(progress, 0.68, 0.83));
    const heroExit = smooth(range(progress, 0.12, 0.235));
    const flash = Math.max(
      peak(progress, 0.285, 0.035),
      peak(progress, 0.535, 0.03),
      peak(progress, 0.785, 0.03)
    );

    const activeIndex = progress < 0.235 ? 0 : progress < 0.49 ? 1 : progress < 0.735 ? 2 : 3;
    setActiveScene(activeIndex);

    root.style.setProperty("--p", progress.toFixed(4));
    root.style.setProperty("--portal-scale", (0.72 + portalTravel * 10.8).toFixed(4));
    root.style.setProperty("--portal-opacity", (1 - range(progress, 0.23, 0.33)).toFixed(4));
    root.style.setProperty("--hero-opacity", (1 - heroExit).toFixed(4));
    root.style.setProperty("--flash-opacity", (flash * 0.8).toFixed(4));

    if (worlds[0]) {
      const coreZoom = 1.16 + smooth(range(progress, 0, 0.31)) * 1.18;
      const coreX = smooth(range(progress, 0.04, 0.3)) * -7;
      worlds[0].querySelector("img").style.transform = `translate3d(${coreX}vw, 0, 0) scale(${coreZoom})`;
      worlds[0].style.filter = `saturate(${1 + portalTravel * 0.28}) brightness(${1 - heroExit * 0.35})`;
    }

    if (worlds[1]) {
      worlds[1].style.clipPath = `circle(${revealWellness * 150}% at 61.5% 52%)`;
      worlds[1].querySelector("img").style.transform = `translate3d(${(1 - revealWellness) * 4}vw, 0, 0) scale(${1.15 - revealWellness * 0.15})`;
    }

    if (worlds[2]) {
      const waterLine = 112 - revealWater * 128;
      worlds[2].style.clipPath = `polygon(0 ${waterLine}%, 42% ${waterLine - 7}%, 100% ${waterLine + 4}%, 100% 116%, 0 116%)`;
      worlds[2].querySelector("img").style.transform = `translate3d(0, ${(1 - revealWater) * 5}vh, 0) scale(${1.14 - revealWater * 0.14})`;
    }

    if (worlds[3]) {
      const energyEdge = revealEnergy * 118;
      worlds[3].style.clipPath = `polygon(0 0, ${energyEdge}% 0, ${Math.max(0, energyEdge - 14)}% 100%, 0 100%)`;
      worlds[3].querySelector("img").style.transform = `translate3d(${(1 - revealEnergy) * -5}vw, 0, 0) scale(${1.14 - revealEnergy * 0.14})`;
    }

    updateTube(progress);
  };

  const requestUpdate = () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(updateExperience);
  };

  const updatePointer = (event) => {
    if (reducedMotion.matches) return;
    root.style.setProperty("--pointer-x", ((event.clientX / window.innerWidth) * 2 - 1).toFixed(3));
    root.style.setProperty("--pointer-y", ((event.clientY / window.innerHeight) * 2 - 1).toFixed(3));
  };

  initializeTube();
  window.addEventListener("scroll", requestUpdate, { passive: true });
  window.addEventListener("resize", requestUpdate, { passive: true });
  window.addEventListener("pointermove", updatePointer, { passive: true });
  reducedMotion.addEventListener("change", requestUpdate);
  requestUpdate();
})();
