<template>
  <header class="position-fixed border border-primary border-2 p-2 w-100">
    <div class="d-flex justify-content-between w-100">
      <h1>Wedding Gallery</h1>
      <button class="btn btn-primary" id="show-modal" @click="onClickLogin">{{ userName ?? 'LOGIN' }}</button>
    </div>
  </header>
</template>

<script>


export default {
  name: 'HeaderComponent',
  props: {
    userName: String
  },
  data() {
    return {
      showLoginModal: false
    }
  },
  methods: {
    onClickLogin() {
      this.$emit('login');
      this.showLoginModal = true;
    },
  }
}
</script>

<style scoped>
header {
  top: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
  background-color: white;
  height: 70px;
}
</style>
