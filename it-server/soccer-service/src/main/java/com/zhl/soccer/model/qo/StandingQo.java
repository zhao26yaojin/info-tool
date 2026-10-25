package com.zhl.soccer.model.qo;

import lombok.Data;
import java.lang.Long;
import java.lang.String;

@Data
public class StandingQo {

	private Long id;

	private Long tournamentId;

	private String name;

}