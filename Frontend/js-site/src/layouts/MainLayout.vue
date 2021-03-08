<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-dark text-grey-4">
      <q-toolbar>
        <q-toolbar-title class="text-bold text-uppercase text-positive">
          <router-link to="/" class="text-positive">
          <span class="">//</span> JS Code
          </router-link>
        </q-toolbar-title>

        <q-btn dense flat round icon="view_list" size="lg" @click="right = !right" color="accent"  />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="right" side="right" behavior="mobile" elevated content-class="bg-dark">
      <js-drawer-content />
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
    <js-footer />
    <js-mobile-bottom-bar/>


  </q-layout>
</template>

<script>
import JsFooter from "components/jsFooter";
import JsMobileBottomBar from "components/service/jsMobileBottomBar";
import JsDrawerContent from "components/header/jsDrawerContent";
export default {
  components: {JsDrawerContent, JsMobileBottomBar, JsFooter},
  data () {
    return {
      right: false
    }
  }
}
</script>
