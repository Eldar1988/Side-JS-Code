<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-dark text-grey-4">
      <q-toolbar>
        <q-toolbar-title class="text-bold text-uppercase text-positive">
          <span class="text-accent">//</span> JS Code
        </q-toolbar-title>

        <q-btn dense flat round icon="view_list" size="lg" @click="right = !right" color="accent"  />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="right" side="right" behavior="mobile" elevated>
      <!-- drawer content -->
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      right: false
    }
  }
}
</script>
