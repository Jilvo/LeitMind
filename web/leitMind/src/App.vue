<template>
  <!-- Pas forcément besoin d’un style particulier ici,
       on inclut simplement le composant TemplateOne -->
  <TemplateOne />
</template>

<script>
import TemplateOne from "./components/TemplateOne.vue";

export default {
  name: "App",
  components: {
    TemplateOne,
  },
};
</script>

<style scoped>
/* Votre style global ou supplémentaire */
</style>
