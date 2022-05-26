<template>
  <div class="card my-2 d-flex justify-content-center mx-auto">
    <img :src="photo.url" class="card-img-top border-bottom" alt="foto do casamento">

    <div class="card-body">
      <div class="border">
          <h5 class="card-title">{{ photo.author }}</h5>
          <h6 class="card-subtitle mb-2 text-muted">Author: {{ photo.description }}</h6>
      </div>

      <div class="d-flex justify-content-between py-2 w-100">
        <button @click="onAddLike()" :disabled="!canGiveLike"  class="btn btn-outline-primary" >
          <i class="fa-solid fa-heart" ></i>
          {{ likesCount }}
        </button>
        <div class="p-1"></div>
        <div class="input-group">
          <input type="text" class="form-control" @keyup.enter="onComment()" v-model="newComment" placeholder="escreva aqui">
        </div>
      </div>

      <ul class="list-group list-group-flush border">
        <li class="list-group-item" :key="comment" v-for="comment in commentsList">
          <PhotoCommentComponent :text="comment" />
        </li>
      </ul>

      <div v-show="!photo.is_approved">
        <button @click="onApprove(true)" :disabled="!canApprove"  class="btn btn-outline-success" >
          <i class="fa-solid fa-thumbs-up" ></i>
        </button>
        <button @click="onApprove(false)" :disabled="!canApprove"  class="btn btn-outline-danger" >
          <i class="fa-solid fa-thumbs-down" ></i>
        </button>
      </div>

    </div>
  </div>

</template>

<script>
import PhotoCommentComponent from './PhotoComment'
import {photoService} from "@/services/Photo.service";

export default {
  name: 'PhotoCardComponent',
  components: {
    PhotoCommentComponent,
  },
  props: {
    photo: {
      _id: String,
      likes: Number,
      comments: Array,
    },
  },
  methods: {
    async onAddLike() {
      // Optimistic update for improved UX
      this.canGiveLike = false;
      this.likesCount += 1;

      const wasSuccess = await photoService.putLike(this.photo._id);

      if (!wasSuccess) {
        this.canGiveLike = true;
        this.likesCount -= 1;
      }
    },
    async onComment() {
      // Save text and erase input field
      const newCommentCopy = this.newComment;
      this.newComment = '';

      // Optimistic update for improved UX
      this.commentsList.push(newCommentCopy);


      const wasSuccess = await photoService.putComment(this.photo._id, newCommentCopy);

      if (!wasSuccess) {
        this.commentsList.pop();
      }
    },
    async onApprove(isApproved) {
      // Optimistic update for improved UX
      this.approvedResult = isApproved;
      this.canApprove = false;

      const wasSuccess = await photoService.putApprove(this.photo._id, isApproved);

      if (!wasSuccess) {
        this.approvedResult = null;
        this.canApprove = true;
      }
    },
  },
  data() {
    return {
      likesCount: this.photo.likes,
      canGiveLike: true,

      commentsList: this.photo.comments,

      canApprove: true,
      approvedResult: null,

      newComment: null,
    }
  },
}
</script>

<style scoped>
.card {
  min-width: 350px;
  max-width: 500px;
  background-color: mistyrose;
}
.card-img-top {
  min-height: 250px;
}
.btn {
background-color: white;
}
.border {
background-color:white
}
</style>
