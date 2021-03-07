<template>
<div class="container">
  <h2 class="text-center text-h5 text-bold">О нас</h2>
  <div>
<!--    <img src="../../assets/images/1.png" class="about-img">-->
  </div>
  <div>
    <q-card
      dark
      class="my-shadow about-card q-pa-md rounded text-grey-5 q-mt-xl"
    >
    <p class="q-mt-md">
      JS Code — небольшая компания, основанная в 2019 году. Мы занимается разработкой сайтов, интернет-магазинов, веб-сервисов и мобильных приложений.
    </p>
    <p class="q-mt-md">
      Мы, как компания, еще молоды, но каждый из нас имеет большой опыт в разработке. В связи с этим цены нашей компании значительно ниже рыночных, но при этом стараемся делать свою работу с максимальной отдачей — работаем на репутацию.
    </p>
    <p class="q-mt-md">
      Мы стараемся с самого начала выстраивать максимально дружеские отношения с клиентами, это помогает работать продуктивно и комфортно.
    </p>
    <p class="q-mt-md">
      Мы любим свое дело и для нас это не работа — это творчество.
    </p>
      <js-consultation class="q-my-md"/>
    </q-card>
  </div>
</div>
</template>

<script>
import JsConsultation from "components/service/jsConsultation";
export default {
  name: "jsAbout",
  components: {JsConsultation}
}
</script>

<style lang="sass">
.about-img
  display: block
  max-width: 50%
  margin: auto

@media screen and (max-width: 800px)
  .about-img
    max-width: 80%

  .about-card
    margin: 50px 20px
</style>
