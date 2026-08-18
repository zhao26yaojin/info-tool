<template>
	<view class="container">
		<view class="header">
			<u-icon name="list" size="50" @click="onMenuIconClick">
			</u-icon>
		</view>
		<view v-show="showL1Menu" class="menu-container">
			<ul>
				<li>
					<view @click="onL1MenuClick('soccer')">Soccer</view>
				</li>
			</ul>
		</view>
	</view>
</template>
<script setup>

const onMenuIconClick = () => {
	selectL1Menu.name.value = ""
}
const onL1MenuClick = () => {
selectL1Menu.name == tag ? selectL1Menu.name = "": selectL1Menu.name = tag}
const onL2MenuClick = () => {
	showL1Menu.name.value = false
}

</script>
<style scoped>
.container {
	position: relative;
}

.header {
	height: 100rpx;
	border-bottom: 2rpx #858a83 solid;
}

.menu-container {
	position: absolute;
	left: 0;
	top: 100rpx;
	width: 320rpx;
	height: 100vh;
	background-color: #f3f3f3;
}


</style>
