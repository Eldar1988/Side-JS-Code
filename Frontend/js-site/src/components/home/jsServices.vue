<template>
  <div class="services container">
    <h2 class="text-center text-h5 text-bold">Наши услуги</h2>
    <div class="services-grid">
      <div
        v-for="(service, index) in services"
        :key="index"
      >
        <js-service-card :service="service"/>
      </div>

    </div>
  </div>
</template>

<script>
import JsServiceCard from "components/home/jsServiceCard";
export default {
  name: "jsServices",
  components: {JsServiceCard},
  data() {
    return {
      services: [
        {
          title: 'Интернет-магазин',
          subtitle: 'готовое решение',
          items: [
            'Рекомендуется для тестирования товарной ниши',
            'Средняя скорость и функциональность',
            'Адаптивность',
            'Удобная административная панель',
            'Подключение платежных систем',
            'Дополнительные необходимые услуги (имеются ограничения)'
          ],
          techs: [
            {icon: 'mdi-wordpress', label: 'WordPress'},
            {icon: 'mdi-language-php', label: 'PHP'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-database-search', label: 'MySQL'},
          ],
          price: 'от 90 000 тенге'
        },
        {
          title: 'Интернет-магазин',
          subtitle: 'разработка на заказ',
          items: [
            'Высокая скорость и функциональность',
            'Кроссплатформенность: Web, Android, iOS, PWA',
            'Удобная административная панель',
            'Подключение платежных систем',
            'Интеграция с магазином Kaspi.kz',
            'Эксклюзивный дизайн',
            'Дополнительные необходимые услуги'
          ],
          techs: [
            {icon: 'mdi-language-python', label: 'Python'},
            {icon: 'mdi-vuejs', label: 'Vue JS'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-language-typescript', label: 'TypeScript'},
            {icon: 'mdi-nodejs', label: 'NodeJS'},
            {icon: 'mdi-database-search', label: 'PostgreSQL'},
            {icon: 'mdi-sass', label: 'Sass'},
          ],
          price: 'от 200 000 тенге'
        },
        {
          title: 'Лендинги',
          subtitle: 'готовое решение',
          items: [
            'Высокая скорость',
            'Адаптивность',
            'Удобная административная панель',
            'Дополнительные необходимые услуги (имеются ограничения)'
          ],
          techs: [
            {icon: 'mdi-language-html5', label: 'HTML 5'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-language-php', label: 'PHP'},
            {icon: 'mdi-language-css3', label: 'CSS3'},
          ],
          price: '35 000 тенге'
        },
        {
          title: 'Лендинги',
          subtitle: 'разработка на заказ',
          items: [
            'Высокая скорость',
            'Адаптивность',
            'Эксклюзивный дизайн',
            'Удобная административная панель',
            'Дополнительные необходимые услуги'
          ],
          techs: [
            {icon: 'mdi-vuejs', label: 'Vue JS'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-language-php', label: 'PHP'},
            {icon: 'mdi-nodejs', label: 'NodeJS'},
            {icon: 'mdi-sass', label: 'Sass'},
          ],
          price: 'от 70 000 тенге'
        },
        {
          title: 'Многостраничный сайт',
          subtitle: 'готовое решение',
          items: [
            'Высокая скорость и функциональность',
            'Адаптивность',
            'Удобная административная панель',
            'Дополнительные необходимые услуги (имеются ограничения)'
          ],
          techs: [
            {icon: 'mdi-wordpress', label: 'WordPress'},
            {icon: 'mdi-language-php', label: 'PHP'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-database-search', label: 'MySQL'},
          ],
          price: 'от 90 000 тенге'
        },
        {
          title: 'Многостраничный сайт',
          subtitle: 'разработка на заказ',
          items: [
            'Высокая скорость и функциональность',
            'Кроссплатформенность: Web, Android, iOS, PWA',
            'Удобная административная панель',
            'Эксклюзивный дизайн',
            'Дополнительные необходимые услуги'
          ],
          techs: [
            {icon: 'mdi-language-python', label: 'Python'},
            {icon: 'mdi-vuejs', label: 'Vue JS'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-language-typescript', label: 'TypeScript'},
            {icon: 'mdi-nodejs', label: 'NodeJS'},
            {icon: 'mdi-database-search', label: 'PostgreSQL'},
            {icon: 'mdi-sass', label: 'Sass'},
          ],
          price: 'от 150 000 тенге'
        },
        {
          title: 'Веб-сервисы',
          subtitle: 'разработка на заказ',
          items: [
            'Высокая скорость',
            'Функциональность любой сложности',
            'Кроссплатформенность: Web, Android, iOS, PWA',
            'Удобная административная панель',
            'Эксклюзивный дизайн',
            'Дополнительные необходимые услуги'
          ],
          techs: [
            {icon: 'mdi-language-python', label: 'Python'},
            {icon: 'mdi-vuejs', label: 'Vue JS'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-language-typescript', label: 'TypeScript'},
            {icon: 'mdi-nodejs', label: 'NodeJS'},
            {icon: 'mdi-database-search', label: 'PostgreSQL'},
            {icon: 'mdi-sass', label: 'Sass'},
          ],
          price: 'от 120 000 тенге'
        },
        {
          title: 'Блоги и форумы',
          subtitle: 'разработка на заказ',
          items: [
            'Высокая скорость',
            'Функциональность любой сложности',
            'Кроссплатформенность: Web, Android, iOS, PWA',
            'Удобная административная панель',
            'Эксклюзивный дизайн',
            'Дополнительные необходимые услуги'
          ],
          techs: [
            {icon: 'mdi-language-python', label: 'Python'},
            {icon: 'mdi-vuejs', label: 'Vue JS'},
            {icon: 'mdi-language-javascript', label: 'JavaScript'},
            {icon: 'mdi-language-typescript', label: 'TypeScript'},
            {icon: 'mdi-nodejs', label: 'NodeJS'},
            {icon: 'mdi-database-search', label: 'PostgreSQL'},
            {icon: 'mdi-sass', label: 'Sass'},
          ],
          price: 'от 120 000 тенге'
        },
      ]
    }
  },
}
</script>

<style lang="sass">
.services-grid
  margin-top: 30px
  display: grid
  grid-template-columns: 1fr
  grid-gap: 30px

.service-card
  text-align: center
  border-radius: 10px

  h3
    color: $positive
    font-weight: 700

  .subtitle
    color: $grey-4

.service-card-items
  p
    margin-top: 10px


@media screen and (max-width: 650px)
  .services-grid
    grid-template-columns: 1fr
    margin: 20px


</style>
