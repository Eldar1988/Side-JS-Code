<template>
  <q-card
    dark
    class="service-card my-shadow"
  >
    <q-card-section>
      <h3 class="text-h6 text-uppercase">{{ service.title }}</h3>
      <p class="subtitle text-bold text-positive">{{ service.subtitle }}</p>
      <p class="q-mt-md text-subtitle1 text-bold">{{ service.price }}</p>
      <q-btn
        :label="showMore ? 'Свернуть' : 'Подробнее'"
        color="accent"
        outline unelevated
        class="q-mt-md rounded accent-shadow q-px-md"
        @click="showMore = !showMore"
      />
      <div v-show="showMore">
          <div class="service-card-items q-mt-md text-left">
            <p v-for="(item, index) in service.items" :key="index" class="text-grey-5">
              <q-icon color="accent" name="done_all"/>
              {{ item }}
            </p>
          </div>
          <q-separator dark class="q-mt-md"/>
          <div class="tech">
            <p class="subtitle q-mt-lg text-bold">Используются технологии:</p>
            <div class="tech-icons q-mt-md flex justify-center">
              <div v-for="(tech, index) in service.techs" :key="index">
                <q-btn :icon="tech.icon" :label="tech.label" stack flat class="q-py-sm q-ml-sm rounded" color="accent"
                       no-caps/>
              </div>
            </div>
          </div>
          <q-separator dark class="q-mt-md"/>
          <div class="price q-mt-md text-h6 text-positive"><span>{{ service.price }}</span></div>
          <js-consultation/>
          <js-consultation label="Заказать" color="positive" :service="service.title + ' ' + service.subtitle"/>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import JsConsultation from "components/service/jsConsultation";

export default {
  name: "jsServiceCard",
  components: {JsConsultation},
  props: {
    service: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      showMore: false
    }
  },
}
</script>

<style scoped>

</style>
