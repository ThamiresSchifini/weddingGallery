<template>
  <div
      class="border rounded border-dark border-1
            m-1 p-1 h-100 photo-container
            d-flex justify-content-between flex-wrap
      ">
    <div :key="photo.id" v-for="photo in photos" class="flex-fill text-center mx-2">
      <PhotoCardComponent :photo="photo" />
    </div>
  </div>
</template>

<script>
import PhotoCardComponent from './PhotoCard'

export default {
  name: 'PhotoListComponent',
  components: {
    PhotoCardComponent,
  },
  props: {
    photos: Array
  }
}
</script>

<style scoped>
    .photo-container {
        background-color: whitesmoke;
    }
</style>
