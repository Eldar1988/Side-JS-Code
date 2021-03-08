<template>
  <div class="container">
    <h2 class="text-center text-h5 text-bold">Наше портфолио</h2>
    <p class="text-center q-mt-md text-grey-5">Здесь только последних работ<br>для получения полного портофлио свяжитесь с нами</p>
    <div class="portfolios-grid q-mt-xl">
      <q-card
        v-for="portfolio in portfolios"
        :key="portfolio.id"
        dark
        class="shadow-0 portfolio-card rounded"
        style="background: rgba(0,0,0,.1)"
      >
        <q-img :src="portfolio.image_url" class="portfolio-image" contain>
          <template v-slot:loading>
            <q-skeleton class="portfolio-image full-width"/>
          </template>
        </q-img>
        <q-card-section class="text-center">
          <h4 class="text-h6">{{ portfolio.title }}</h4>
          <p class="text-grey-5">{{ portfolio.type }}</p>
          <q-btn
            label="Подробнее"
            color="accent"
            class="q-mt-md q-px-md rounded accent-shadow"
            :to="`/portfolio/${portfolio.slug}`"
          />
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "jsPortfolio",
  computed: {
    portfolios() {
      return this.$store.getters.getPortfolios
    }
  },
  created() {
    this.$store.dispatch('fetchPortfolios')
  }
}
</script>

<style lang="sass">
.portfolios-grid
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 30px

.portfolio-card
  padding: 20px



.portfolio-image
  height: 350px

@media screen and (max-width: 800px)

  .portfolios-grid
    display: flex
    grid-gap: 0
    flex-wrap: nowrap
    overflow-x: scroll

  .portfolio-card
    min-width: 250px
    margin-left: 20px

  .portfolio-image
    height: 200px
</style>
