package com.zhl.soccer.model.qo;

import lombok.Data;
import java.util.List;
import java.lang.Long;
import java.lang.String;

@Data
public class TeamQo {

	private Long id;

	private List<Long> idList;

	private String name;

	private Long tournamentId;

}