<template>
  <div class="mobile-bottom-btn">
    <q-fab
      v-model="fab1"
      color="accent"
      icon="call"
      direction="up"
      class="accent-shadow"
      vertical-actions-align="left"
    >
      <q-fab-action color="primary" icon="call" label="Позвонить +7 778 166 5240" type="a" href="tel:+77781665240"/>
      <q-fab-action color="positive" text-color="dark" icon="mdi-whatsapp" label="Написать +7 778 166 5240" type="a" href="https://wa.me/77781665240"/>
    </q-fab>
  </div>
</template>

<script>
export default {
  name: "jsMobileBottomBar",
  data() {
    return {
      fab1: false
    }
  },
}
</script>

<style lang="sass">
.mobile-bottom-btn
  position: fixed
  bottom: 10px
  left: 10px
</style>
