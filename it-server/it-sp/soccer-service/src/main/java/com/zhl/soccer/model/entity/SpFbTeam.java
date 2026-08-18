package com.zhl.soccer.model.entity;

import lombok.Data;
import java.lang.Long;
import java.lang.String;

@Data
public class SpFbTeam {

	private Long id;

	private String name;

	private Long country_id;

}