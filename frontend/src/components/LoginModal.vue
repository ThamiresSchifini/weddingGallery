<script>
export default {
  name: 'LoginModalComponent',
  props: {
    warning: String
  },
  methods: {
    onLogin($event) {
      this.$emit('login', $event, this.name, this.password);
    },
    close() {
      this.$emit('close');
    },
  },
  data() {
    return {
      name: '',
      password: ''
    }
  }
};
</script>

<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal mx-auto position-relative"
           role="dialog"
      >
        <header
            class="modal-header text-primary"
            id="modalTitle"
        >
          <h1>Admin area</h1>
          <button
              type="button"
              class="btn-close"
              @click="close"
              aria-label="Close modal"
          >
            x
          </button>
        </header>

        <section
            class="modal-body"
            id="modalDescription"
        >

          <div class="input-group my-2">
            <input type="text" class="form-control" v-model="name" placeholder="Username">
          </div>

          <div class="input-group my-2">
            <input type="password" class="form-control" v-model="password" placeholder="Password">
          </div>
        </section>

        <footer class="modal-footer">
          <div v-show="warning" class="alert alert-warning mb-3" role="alert">
            {{ warning }}
          </div>

          <button
              type="button"
              class="btn btn-primary"
              @click="onLogin"
              aria-label="Login button"
          >
            Login
          </button>
        </footer>
      </div>
    </div>
  </transition>
</template>

<style>
</style>
