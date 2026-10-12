package com.zhl.utils.rest;

import lombok.AllArgsConstructor;
import lombok.Data;
import java.util.List;
import java.lang.Long;

@Data
@AllArgsConstructor
public class PageBean<T> {

	private int current;

	private int size;

	private Long total;

	private List<T> records;

}