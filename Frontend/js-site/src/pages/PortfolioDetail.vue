<template>
  <q-page>
    <q-breadcrumbs class="q-ma-md">
      <q-breadcrumbs-el icon="home" class="text-positive" to="/"/>
      <q-breadcrumbs-el :label="pr.title" />
    </q-breadcrumbs>
    <section class="">
      <div class="mt-100 text-center">
        <h1 class="text-h5 text-bold">{{ pr.title }}</h1>
        <p class="text-subtitle1 text-positive">{{ pr.type }}</p>
        <div v-html="pr.text" class="q-mt-md text-grey-5"></div>
        <div class="rp-grid">
          <div>
            <iframe width="100%" :src="pr.site_url" name="iframe" scrolling="auto" class="rounded shadow-10 frame"> </iframe>
          </div>
          <p class="text-grey-5 q-mt-md">Перейти на сайт: <a :href="pr.site_url" class="text-positive" target="_blank">{{ pr.title }}</a></p>
        </div>
      </div>
    </section>
  </q-page>
</template>

<script>
export default {
  name: "PortfolioDetail",
  computed: {
    pr() {
      return this.$store.getters.getPortfolio
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchPortfolioDetail', currentRoute.params.slug)
  }
}
</script>

<style lang="sass">
.frame
  border: none
  margin-top: 50px
  max-width: 90%
  height: 750px
  @media screen and (max-width: 550px)
    height: 600px
</style>
