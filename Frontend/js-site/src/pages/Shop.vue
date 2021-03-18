<template>
<q-page class="flex flex-center column">
  <h1 class="text-h6 text-positive text-center">Здравствуйте!<br>Мы рады, что Вас заинтересовал наш интернет-магазин</h1>
  <p class="text-center q-mt-md">Вам осталось просто оставить заявку, <br>мы проконсультируем Вас по всем вопросам <br>и предоставим тестовую версию для ознакомления</p>
  <js-consultation label="Оставить заявку" service="Заявка по интернет-магазину"/>
</q-page>
</template>

<script>
import JsConsultation from "components/service/jsConsultation";
export default {
name: "shop",
  components: {JsConsultation}
}
</script>

<style scoped>

</style>
