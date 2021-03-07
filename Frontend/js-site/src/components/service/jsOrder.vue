<template>
  <div>
    <div class="px-m-20 q-mt-md no-padding-d">
      <q-btn
        label="Консультация"
        class="rounded q-py-sm letter-1 q-px-md accent-shadow"
        :style="$q.platform.is.mobile ? `min-width: 100%` : ``"
        color="accent"
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
          <q-toolbar-title class="text-bold text-accent">Консультация</q-toolbar-title>
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
export default {
  name: "jsOrder"
}
</script>

<style scoped>

</style>
