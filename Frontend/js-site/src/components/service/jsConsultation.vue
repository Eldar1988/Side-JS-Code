<template>
  <div>
    <div class="px-m-20 q-mt-md no-padding-d">
      <q-btn
        :label="label"
        :class="color === 'positive' ? `rounded q-py-sm letter-1 q-px-md` : `rounded q-py-sm letter-1 q-px-md accent-shadow`"
        :style="$q.platform.is.mobile ? `min-width: 100%` : ``"
        :color="color"
        outline unelevated
        @click="dialog = true"
      />
    </div>
    <q-dialog v-model="dialog" position="top">
      <q-card
        dark
        style="width: 500px; max-width: 100%"
      >
        <q-toolbar class="flex justify-between">
          <q-toolbar-title class="text-bold text-accent">{{ service === 'Консультация' ? 'Консультация' : service}}</q-toolbar-title>
          <q-btn icon="close" color="accent" dense flat v-close-popup/>
        </q-toolbar>
        <q-card-section>
          <p>Заполните форму обратной связи<br>Мы свяжемся с вами в течении 5 минут
            <br><br>Или позвоните по номеру <a href="tel:+77781665240" class="text-positive q-ml-sm">+7 778 166 5250</a></p>
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
                v-model="formData.text"
                label="Комментарий (необязательно)"
                dark outlined
                color="positive"
                class="q-mt-md "
                type="textarea"
              />
              <q-btn
                label="Отправить"
                color="positive"
                text-color="dark"
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
  props: {
    label: {
      type: String,
      default: 'Консультация'
    },
    color: {
      type: String,
      default: 'accent'
    },
    service: {
      type: String,
      default: 'Консультация'
    }
  },
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
        this.formData.service = this.service

        await this.$axios(`${this.$store.getters.getServerURL}/contacts/create_callback/`, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          data: JSON.stringify(this.formData)
        }).then(response => {
          if(response.status === 201) {
            notifier('Спасибо! Ваша заявка принята', 'accent')
            this.dialog = false
          } else {
            notifier('Извините. Произошла ошибка. Попробуйте еще раз')
          }
        })
      }
    }
  }
}
</script>

<style scoped>

</style>
