<template>
  <div class="flex flex-center text-center column">
    <h1 class="text-h5 q-px-md text-bold">Разработка сайтов<br> веб-сервисов и мобильных приложений<br>
    </h1>
    <div class="container">
      <p class="q-mt-xl q-px-md">Мы предлагаем комплексное решение:</p>
      <div class="q-mt-md flex justify-between no-wrap overflow-x-scroll q-py-md">
        <q-card
          v-for="(card, index) in cards"
          :key="index"
          dark
          class="rounded bg-gradient-1 q-py-lg q-px-md ml-m-20 shadow-0"
          style="min-width: 220px;"
        >
          <q-icon :name="card.icon" size="lg"/>
          <p class="text-subtitle1">{{ card.title }}</p>
        </q-card>
      </div>
      <js-consultation />
    </div>



  </div>
</template>

<script>
import JsConsultation from "components/service/jsConsultation";
export default {
  name: "jsHomeFirstScreen",
  components: {JsConsultation},
  data() {
    return {
      cards: [
        {icon: 'language', title: 'Веб-сайт'},
        {icon: 'mdi-android-debug-bridge', title: 'Android приложение'},
        {icon: 'mdi-apple', title: 'iOS приложение'},
        {icon: 'mdi-responsive', title: 'PWA приложение'}
      ]
    }
  },
}
</script>

<style scoped>

</style>
