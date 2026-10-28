<template>
	<div class="frame">
		<el-form :inline="true" :model="standingQuery" class="form-inline">
			<el-form-item label="id">
				<el-select v-model="standingQuery.tournamentId" placeholder="tournamentId" clearable>
					<el-option v-for="item in tournamentList" :key="item.id" :label="item.name" :value="item.id">
					</el-option>
				</el-select>
			</el-form-item>
			<el-form-item>
				<el-button type="primary" @click="onGetStandingList">Query</el-button>
			</el-form-item>
		</el-form>
		<el-table :data="standingList" border>
			<el-table-column prop="teamLogo" label="图标">
			</el-table-column>
			<el-table-column prop="teamName" label="名称">
			</el-table-column>
			<el-table-column prop="wins" label="胜">
			</el-table-column>
			<el-table-column prop="draws" label="平">
			</el-table-column>
			<el-table-column prop="losses" label="负">
			</el-table-column>
			<el-table-column prop="goalsFor" label="进球">
			</el-table-column>
			<el-table-column prop="goalsAgainst" label="失球">
			</el-table-column>
			<el-table-column prop="goalDifference" label="净胜球">
			</el-table-column>
			<el-table-column prop="points" label="积分">
			</el-table-column>
		</el-table>
	</div>
</template>
<script setup>
import { getList as getStandingList } from "@/api/fb/standing"
import { onMounted, reactive } from "vue"

const standingQuery = reactive({tournamentId: ''})
const standingList = reactive([])
const onGetStandingList = async () => {
	const { result } = await getStandingList(standingQuery)

	standingList.splice(0, standingList.length)

	if (result && result.length > 0) {
		standingList.push(...result)
	}

}
onMounted(() => onGetStandingList())

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
