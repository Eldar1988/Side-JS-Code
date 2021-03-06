import {Notify} from 'quasar'

export default function notifier(text, color='dark') {
  Notify.create({message: text, color: color, position: 'top'})
}
