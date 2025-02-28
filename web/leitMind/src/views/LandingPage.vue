<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Hotjar from '@hotjar/browser';

onMounted(() => {
  if (typeof window !== 'undefined') {
    Hotjar.init(5322100, 6);
  }
});

const features = [
  {
    title: 'Apprentissage Quotidien',
    description: 'Recevez chaque jour de nouvelles questions adaptées à vos centres d\'intérêt',
    icon: '📚'
  },
  {
    title: 'Intelligence Adaptative',
    description: 'L\'application s\'adapte à votre niveau et à votre progression',
    icon: '🎯'
  },
  {
    title: 'Communauté Active',
    description: 'Partagez vos connaissances et apprenez des autres utilisateurs',
    icon: '🤝'
  }
]

const categories = [
  { name: 'Sciences', icon: '🔬', color: '#4f46e5' },
  { name: 'Histoire', icon: '📜', color: '#7c3aed' },
  { name: 'Culture', icon: '🎭', color: '#9333ea' },
  { name: 'Technologie', icon: '💻', color: '#6366f1' }
]

const isMenuOpen = ref(false)
const cursorPos = ref({ x: 0, y: 0 })
const cursorScale = ref(1)
const scrollProgress = ref(0)

// Gestion du curseur personnalisé
const updateCursorPosition = (e) => {
  cursorPos.value = {
    x: e.clientX,
    y: e.clientY
  }
}

const updateCursorScale = (scale) => {
  cursorScale.value = scale
}

// Gestion du scroll
const handleScroll = () => {
  const scrolled = window.scrollY
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight
  scrollProgress.value = (scrolled / maxScroll) * 100

  // Animation des éléments au scroll
  const elements = document.querySelectorAll('.animate-on-scroll')
  elements.forEach(el => {
    const rect = el.getBoundingClientRect()
    const isVisible = rect.top < window.innerHeight - 100
    if (isVisible) {
      el.classList.add('visible')
    }
  })
}

// Lifecycle hooks
onMounted(() => {
  window.addEventListener('mousemove', updateCursorPosition)
  window.addEventListener('scroll', handleScroll)
  handleScroll()
})

onUnmounted(() => {
  window.removeEventListener('mousemove', updateCursorPosition)
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <div class="landing-page">
    <!-- Curseur personnalisé -->
    <div class="custom-cursor"
         :style="{
           transform: `translate(${cursorPos.x}px, ${cursorPos.y}px) scale(${cursorScale})`,
         }">
      <div class="cursor-dot"></div>
    </div>

    <!-- Indicateur de progression -->
    <div class="scroll-progress" :style="{ width: scrollProgress + '%' }"></div>

    <!-- Hero Section -->
    <header class="hero">
      <nav class="nav">
        <div class="logo hover-effect">LeitMind</div>
        <button class="menu-toggle hover-effect" @click="isMenuOpen = !isMenuOpen">
          <span></span>
        </button>
        <div class="nav-links" :class="{ 'active': isMenuOpen }">
          <a href="#features"
             class="hover-effect"
             @mouseenter="updateCursorScale(2)"
             @mouseleave="updateCursorScale(1)">Fonctionnalités</a>
          <a href="#categories"
             class="hover-effect"
             @mouseenter="updateCursorScale(2)"
             @mouseleave="updateCursorScale(1)">Catégories</a>
          <a href="#download"
             class="hover-effect"
             @mouseenter="updateCursorScale(2)"
             @mouseleave="updateCursorScale(1)">Télécharger</a>
          <button class="cta-button hover-effect"
                  @mouseenter="updateCursorScale(2)"
                  @mouseleave="updateCursorScale(1)">Essayer Gratuitement</button>
        </div>
      </nav>
      <div class="hero-content">
        <h1 class="animate-on-scroll fade-up">Apprenez Chaque Jour,<br>Une Question à la Fois</h1>
        <p class="animate-on-scroll fade-up delay-1">Développez vos connaissances quotidiennement grâce à des questions personnalisées et une expérience d'apprentissage unique</p>
        <div class="app-buttons animate-on-scroll fade-up delay-2">
          <button class="store-button hover-effect"
                  @mouseenter="updateCursorScale(2)"
                  @mouseleave="updateCursorScale(1)">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Download_on_the_App_Store_Badge.svg" alt="App Store" />
          </button>
          <button class="store-button hover-effect"
                  @mouseenter="updateCursorScale(2)"
                  @mouseleave="updateCursorScale(1)">
            <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" alt="Play Store" />
          </button>
        </div>
        <div class="phone-mockup animate-on-scroll fade-up delay-3">
          <img src="https://placehold.co/280x560" alt="App Screenshot" class="phone-screen" />
        </div>
      </div>
    </header>

    <!-- Features Section -->
    <section id="features" class="features">
      <h2 class="animate-on-scroll fade-up">Comment ça marche ?</h2>
      <div class="features-grid">
        <div v-for="(feature, index) in features"
             :key="feature.title"
             class="feature-card animate-on-scroll fade-up hover-effect"
             :class="'delay-' + index"
             @mouseenter="updateCursorScale(2)"
             @mouseleave="updateCursorScale(1)">
          <div class="feature-icon">{{ feature.icon }}</div>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <!-- Categories Section -->
    <section id="categories" class="categories">
      <h2 class="animate-on-scroll fade-up">Explorez Nos Catégories</h2>
      <div class="categories-grid">
        <div v-for="(category, index) in categories"
             :key="category.name"
             class="category-card animate-on-scroll fade-up hover-effect"
             :class="'delay-' + index"
             :style="{ backgroundColor: category.color }"
             @mouseenter="updateCursorScale(2)"
             @mouseleave="updateCursorScale(1)">
          <div class="category-icon">{{ category.icon }}</div>
          <h3>{{ category.name }}</h3>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section id="download" class="cta">
      <h2 class="animate-on-scroll fade-up">Commencez Votre Voyage d'Apprentissage</h2>
      <p class="animate-on-scroll fade-up delay-1">Rejoignez plus de 10 000 apprenants qui enrichissent leurs connaissances chaque jour</p>
      <div class="app-buttons animate-on-scroll fade-up delay-2">
        <button class="store-button hover-effect"
                @mouseenter="updateCursorScale(2)"
                @mouseleave="updateCursorScale(1)">
          <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Download_on_the_App_Store_Badge.svg" alt="App Store" />
        </button>
        <button class="store-button hover-effect"
                @mouseenter="updateCursorScale(2)"
                @mouseleave="updateCursorScale(1)">
          <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg" alt="Play Store" />
        </button>
      </div>
    </section>
  </div>
</template>

<style scoped>
.landing-page {
  min-height: 100vh;
}

.hero {
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
  color: white;
  padding: 2rem;
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: 500;
}

.hero-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.hero-content h1 {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.hero-content p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  max-width: 600px;
}

.app-buttons {
  display: flex;
  gap: 1rem;
  margin-bottom: 3rem;
}

.store-button {
  background: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
}

.store-button img {
  height: 40px;
}

.store-button:hover {
  transform: translateY(-2px);
}

.phone-mockup {
  margin-top: 2rem;
  position: relative;
}

.phone-screen {
  border-radius: 2rem;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.features {
  padding: 5rem 2rem;
  background-color: #f8fafc;
}

.features h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: #1e293b;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  text-align: center;
  transition: transform 0.2s;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  color: #1e293b;
  margin-bottom: 1rem;
}

.categories {
  padding: 5rem 2rem;
  background-color: white;
}

.categories h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: #1e293b;
}

.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
}

.category-card {
  color: white;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  transition: transform 0.2s;
  cursor: pointer;
}

.category-card:hover {
  transform: translateY(-5px);
}

.category-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.category-card h3 {
  font-size: 1.25rem;
  margin: 0;
}

.cta {
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
  color: white;
  text-align: center;
  padding: 5rem 2rem;
}

.cta h2 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
}

.cta p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

@media (max-width: 768px) {
  .menu-toggle {
    display: block;
    background: none;
    border: none;
    color: white;
    font-size: 1.5rem;
  }

  .nav-links {
    display: none;
  }

  .nav-links.active {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #4f46e5;
    padding: 1rem;
    z-index: 10;
  }

  .hero-content h1 {
    font-size: 2.5rem;
  }

  .app-buttons {
    flex-direction: column;
  }

  .phone-mockup {
    transform: scale(0.8);
  }
}

/* Curseur personnalisé */
.custom-cursor {
  width: 20px;
  height: 20px;
  border: 2px solid #4f46e5;
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  transition: transform 0.1s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.cursor-dot {
  width: 4px;
  height: 4px;
  background-color: #4f46e5;
  border-radius: 50%;
}

/* Barre de progression */
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 4px;
  background: linear-gradient(90deg, #4f46e5, #7c3aed);
  z-index: 1000;
  transition: width 0.2s ease;
}

/* Effets de hover */
.hover-effect {
  position: relative;
  transition: all 0.3s ease;
}

.hover-effect::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -2px;
  left: 0;
  background-color: currentColor;
  transition: width 0.3s ease;
}

.hover-effect:hover::after {
  width: 100%;
}

.nav-links a:hover,
.nav-links button:hover {
  transform: translateY(-2px);
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
}

/* Animations au scroll */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}

.delay-1 { transition-delay: 0.2s; }
.delay-2 { transition-delay: 0.4s; }
.delay-3 { transition-delay: 0.6s; }

/* Améliorations des transitions existantes */
.feature-card,
.category-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature-card:hover,
.category-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}
</style>
