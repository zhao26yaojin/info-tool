<template>
	<div class="container">
		<div class="sidebar">
			<h5 class="title">info tool</h5>
			<el-menu height="100%" background-color="#545C64FF" active-text-color="#aba39b" text-color="#fff" router>
				<el-sub-menu>
					<template #title>
						<span>soccer</span>
					</template>
					<el-menu-item index="/soccer/team">team</el-menu-item>
					<el-menu-item index="/soccer/standing">standing</el-menu-item>
				</el-sub-menu>
			</el-menu>
		</div>
		<router-view>
		</router-view>
	</div>
</template>
<script setup>


</script>
<style scoped>
.container {
	min-height: 100vh;
	display: flex;
}

.sidebar {
	width: 200px;
	background-color: #545C64FF;
}

.title {
	height: 50px;
	color: white;
	font-size: 20px;
	text-align: center;
	line-height: 50px;
}


</style>
