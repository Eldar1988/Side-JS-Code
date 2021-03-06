<template>
  <div>
    <div class="px-m-20 q-mt-md no-padding-d">
      <q-btn
        label="Консультация"
        class="full-width rounded q-py-sm letter-1"
        color="accent"
        outline
        @click="dialog = true"
      />
    </div>
    <q-dialog v-model="dialog">
      <q-card
        dark
        style="width: 500px; max-width: 100%"
      >
        <q-toolbar class="flex justify-between">
          <q-toolbar-title class="text-bold">Консультация</q-toolbar-title>
          <q-btn icon="close" dense flat v-close-popup/>
        </q-toolbar>
        <q-card-section>
          <p>Заполните форму обратной связи<br>Мы свяжемся с вами в течении 5 минут</p>
          <div class="q-mt-lg">
            <q-form>
              <q-input
                ref="name"
                v-model="formData.name"
                label="Ваше имя*"
                dark outlined
                color="positive"
              />
              <q-input
                v-model="formData.phone"
                label="Номер телефона*"
                dark outlined
                color="positive"
                type="tel"
                class="q-mt-md"
                mask="# ### ### ####"
              />
              <q-input
                v-model="formData.phone"
                label="Комментарий (необязательно)"
                dark outlined
                color="positive"
                class="q-mt-md "
                type="textarea"
              />
              <q-btn
                label="Отправить"
                color="accent" outline
                class="q-mt-md full-width q-py-sm rounded text-bold"
                @click="sentData"
              />
            </q-form>
          </div>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import notifier from "src/service/notifier";

export default {
  name: "jsConsultation",
  data() {
    return {
      dialog: false,
      formData: {
        name: '',
        phone: '',
        text: ''
      }
    }
  },
  methods: {
    validate(name, phone) {
      if (name === '') {
        notifier('Необходимо указать имя')
        return false
      }
      if (phone === '') {
        notifier('Необходимо указать номер телефона')
        return false
      }
      return true
    },
    async sentData() {
      let valid = this.validate(this.formData.name, this.formData.phone)
      if (valid) {
        notifier('Success', 'positive')
      }
    }
  }
}
</script>

<style scoped>

</style>
