<template>
  <q-page class="">
    <img src="../assets/images/cub-3.png" alt="" class="cub-image">
    <js-home-first-screen style="width: 100%; height: 100vh"/>
    <section>
      <js-benefits />
    </section>
  </q-page>
</template>

<script>
import JsHomeFirstScreen from "components/home/jsHomeFirstScreen";
import JsBenefits from "components/home/jsBenefits";
export default {
  name: 'PageIndex',
  components: {JsBenefits, JsHomeFirstScreen}
}
</script>
