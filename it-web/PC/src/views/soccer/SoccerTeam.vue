<template>
	<div class="frame">
		<el-form :inline="true" :model="teamQuery" class="form-inline">
			<el-form-item label="名称">
				<el-input v-model="teamQuery.name" placeholder="name" clearable>
				</el-input>
			</el-form-item>
			<el-form-item label="id">
				<el-input v-model="teamQuery.tournamentId" placeholder="tournamentId" clearable>
				</el-input>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="onGetTeamPage">Query</el-button>
			</el-form-item>
		</el-form>
		<el-table :data="teamPage" border>
			<el-table-column prop="name" label="名称">
			</el-table-column>
			<el-table-column prop="logo" label="图标">
				<template #default="{ row }">
					<el-image v-if="row.logo" :src="imgUrl(row.logo)" fit="contain" style="width: 24px; height: 24px" lazy>
					</el-image>
				</template>
			</el-table-column>
			<el-table-column prop="tournamentId" label="id">
			</el-table-column>
		</el-table>
		<div>
			<el-pagination v-model:current-page="teamQuery.current" v-model:page-size="teamQuery.size" layout="prev, pager, next, jumper" :total="teamQuery.total" @current-change="onTeamPageChange">
			</el-pagination>
		</div>
	</div>
</template>
<script setup>
import { imgUrl } from "@/utils/image"
import { getPage as getTeamPage } from "@/api/fb/team"
import { onMounted, reactive } from "vue"

const teamQuery = reactive({
	name: '',
	tournamentId: ''
})
const teamPage = reactive([])
const onGetTeamPage = async () => {
	const { result } = await getTeamPage(teamQuery)
	teamQuery.total = result.total

	teamPage.splice(0, teamPage.length)

	if (result.records && result.records.length > 0) {
		teamPage.push(...result)
	}

}
onMounted(() => onGetTeamPage())

</script>
<style scoped>
.frame {
	width: 800px;
	margin: auto;
	padding-top: 30px;
}

.form-inline {
}


</style>
