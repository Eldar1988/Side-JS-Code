<template>
<div class="container">
  <h2 class="text-center text-h5 text-bold">Почему мы</h2>
  <div class="benefits-grid q-mt-xl">
    <div
      v-for="(benefit, index) in benefits"
      :key="index"
    >
      <q-card
        dark
        class="text-center benefit-card rounded flex flex-center column my-shadow"
        style="min-width: 250px"
      >
        <q-card-section>
          <h3 class="text-h6 text-bold text-accent">{{ benefit.title }}</h3>
          <p class="q-mt-sm text-grey-5">{{ benefit.text }}</p>
        </q-card-section>
      </q-card>
    </div>
  </div>
</div>
</template>

<script>
export default {
name: "jsBenefits",
  data() {
    return {
      benefits: [
        {title: 'Качество', text: 'Мы используем современные высокопроизводительные и стабильные решения.'},
        {title: 'Все в одном', text: 'Мы предлагаем комплексное кроссплатформенное решение с одной кодовой базой'},
        {title: 'Обслуживание', text: 'Мы бесплатно поддерживаем работоспособность продукта в течение первого года'},
        {title: 'Готовые решения', text: 'Мы предлагаем готовые решения, отлично подходит для тестирования ниши'},
        {title: 'Масштабируемость', text: 'Мы заранее предусматриваем рост и масштабируемость вашего бизнес-решения'},
        {title: 'Дружелюбность', text: 'Нам очень нравится иметь по-настоящему дружеские отношения с клиентами'}
      ]
    }
  },
}
</script>

<style lang="sass">
.benefits-grid
  display: grid
  grid-template-columns: repeat(3, 1fr)
  grid-gap: 30px

.benefit-card
  min-height: 100%
  //border: 1px solid $accent
  background: rgba(0,0,0,.1)

@media screen and (max-width: 992px)
  .benefits-grid
    max-width: 100%
    overflow-x: scroll
    display: flex
    flex-wrap: nowrap
    grid-gap: 0
    padding: 10px 0

  .benefit-card
    margin-left: 20px
</style>
