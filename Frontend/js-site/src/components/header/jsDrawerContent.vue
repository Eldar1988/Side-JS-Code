<template>
  <div>
    <q-toolbar class="bg-positive">
      <q-toolbar-title class="text-bold text-uppercase text-dark text-center">
        <router-link to="/" class="text-dark">
          <span class="">//</span> JS Code
        </router-link>
      </q-toolbar-title>
    </q-toolbar>

    <div class="q-px-sm q-mt-lg">
      <q-list separator>
        <q-item clickable v-ripple to="/" active-class="text-accent">
          <q-item-section avatar>
            <q-icon name="home"/>
          </q-item-section>
          <q-item-section class="text-uppercase">Главная</q-item-section>
        </q-item>
        <q-item clickable v-ripple @click="scrollTo('benefits')" to="/#benefits" active-class="text-accent">
          <q-item-section avatar>
            <q-icon name="home"/>
          </q-item-section>
          <q-item-section class="text-uppercase">Почему мы</q-item-section>
        </q-item>
        <q-item clickable v-ripple to="/#service" @click="scrollTo('service')" active-class="text-accent">
          <q-item-section avatar>
            <q-icon name="settings_suggest"/>
          </q-item-section>
          <q-item-section class="text-uppercase">Услуги</q-item-section>
        </q-item>
        <q-item clickable v-ripple to="/#protfolio" @click="scrollTo('portfolio')" active-class="text-accent">
          <q-item-section avatar>
            <q-icon name="widgets"/>
          </q-item-section>
          <q-item-section class="text-uppercase">Портфолио</q-item-section>
        </q-item>
      </q-list>

      <q-btn
        type="a"
        href="tel:+77781665240"
        label="+7 778 166 5240"
        icon="call"
        class="full-width rounded q-py-sm q-mt-xl"
        color="positive"
        outline
      />
      <q-btn
        type="a"
        href="https://wa.me/77781665240"
        label="+7 778 166 5240"
        icon="mdi-whatsapp"
        class="full-width rounded q-py-sm q-mt-sm"
        color="positive"
        outline
      />
      <div class="text-center">
        <js-consultation/>
      </div>
    </div>
  </div>
</template>

<script>
import JsConsultation from "components/service/jsConsultation";

export default {
  name: "jsDrawerContent",
  components: {JsConsultation},
  methods: {
    scrollTo(id) {
      this.$root.$emit('scrollTo', id)
    }
  }
}
</script>

<style scoped>

</style>
