<template>
  <!-- min-h-screen pour prendre toute la hauteur de la fenêtre -->
  <div class="flex flex-col min-h-screen sm:flex-row template-one">

    <!-- Section arrière-plan visible à partir de la taille "sm" -->
    <div
      class="hidden sm:flex sm:w-2/3 justify-center items-center p-5
             bg-no-repeat bg-cover bg-center"
      :style="{ backgroundImage: `url(${backgroundImage})` }"
    ></div>

    <!-- Section de contenu -->
    <div
      class="w-full sm:w-1/3 bg-gray-100 p-10
             flex flex-col justify-center items-center shadow-lg"
    >
      <div class="text-center my-auto">
        <!-- <img :src="logo" alt="logo" class="mx-auto mb-4 w-32" /> -->
        <div class="title text-3xl font-semibold mb-3">{{ title }}</div>
        <div class="disclaimer font-light text-xl">
          <vue-typed-js :strings="disclaimer">
            <h1 class="typing"></h1>
          </vue-typed-js>
        </div>
      </div>

      <!-- <div class="mt-auto text-center social-media-container text-lg">
        <a
          v-if="facebook"
          :href="facebook"
          target="_blank"
          class="mx-2 my-3 inline-block hover:text-gray-500"
        >
          Facebook
        </a>
        <a
          v-if="instagram"
          :href="instagram"
          target="_blank"
          class="mx-2 my-3 inline-block hover:text-gray-500"
        >
          Instagram
        </a>
        <a
          v-if="youtube"
          :href="youtube"
          target="_blank"
          class="mx-2 my-3 inline-block hover:text-gray-500"
        >
          YouTube
        </a>
        <a
          v-if="linkedin"
          :href="linkedin"
          target="_blank"
          class="mx-2 my-3 inline-block hover:text-gray-500"
        >
          LinkedIn
        </a>
      </div> -->
    </div>
  </div>
</template>

<script>
import VueTypedJs from 'vue-typed-js'
// Import des assets
import logo from '@/assets/logo.svg'
import backgroundImage from '@/assets/bg.jpg'

export default {
  name: "TemplateOne",
  components: {
    VueTypedJs,
  },
  data() {
    return {
      logo,
      backgroundImage,
      // Données en dur pour l'exemple
      title: "LeitMind, Coming Soon...",
      disclaimer: [
        "Our website is under construction.",
        "We'll be here soon with our new awesome site."
      ],
      facebook: "https://www.facebook.com/",
      instagram: "https://www.instagram.com/",
      youtube: "https://www.youtube.com/",
      linkedin: "https://www.linkedin.com/",
    };
  },
};
</script>

<style scoped>
/* .template-one { */
  /* Si vous voulez parfaire le style de fond en CSS pur au lieu de classes Tailwind :
     .background-container {
       background-size: cover;
       background-position: center;
     }
  */
/* } */
</style>