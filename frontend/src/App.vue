<template>
  <div id="app">
    <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">Sympose</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="sass">
@import "styles"
</style>
