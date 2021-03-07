<template>
  <q-page class="">
    <img src="../assets/images/cub-3.png" alt="" class="cub-image">
    <js-home-first-screen style="width: 100%; height: 100vh"/>
    <section>
      <js-benefits />
    </section>
    <section class="mt-100">
      <js-services />
    </section>
    <section class="mt-100">
      <js-portfolio/>
    </section>
    <section class="mt-100">
      <js-about />
    </section>

  </q-page>
</template>

<script>
import JsHomeFirstScreen from "components/home/jsHomeFirstScreen";
import JsBenefits from "components/home/jsBenefits";
import JsServices from "components/home/jsServices";
import JsAbout from "components/home/jsAbout";
import JsPortfolio from "components/home/jsPortfolio";
export default {
  name: 'PageIndex',
  components: {JsPortfolio, JsAbout, JsServices, JsBenefits, JsHomeFirstScreen}
}
</script>
