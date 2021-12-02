# [Python] Pandas

* 구조화된 데이터의 처리를 지원.
* 데이터 처리, 통계 분석을 위해 사용.



## 기본

* series : 하나의 column에 해당하는 데이터의 모음.
  * ndarray의 subclass
  * index를 직접 지정 가능
* data frame : table 전체를 포함.
  * series를 모아서 data frame(table)이 됨.
  * indexing
    * loc : index location = 지정된 인덱스 이름 사용.
    * iloc : index position = 지정된 인덱스 말고, 데이터 순서대로 번호를 붙인 인덱스 사용.



## selection & drop

* column 이름으로 selection
  * 1개의 column 선택 : `df['col']`
  * 여러 개의 column 선택 : `df[['col1', 'col2', ...]]`
  * boolean index : `df['account'][df['account'] < 250000]`
* index 재설정
  * `df.index = 원하는 index 값들`
  * `df.reset_index()` : 현재의 index와 같은 값을 가진 index column이 추가됨.
    * `drop=True` : 기존의 index는 삭제.
    * `inplace=True` : 데이터 프레임 자체에 변화가 일어남.
* drop
  * index로 drop : `df.drop(index)`
  * 한 번에 여러 개 삭제 : `df.drop([index1, index2, ...])`
  * 지정 축을 기준으로. ex) `df.drop(['col1', 'col2', ...], axis=1)`



## dataframe operation

### series operation

* 모든 연산은 index를 기준으로 수행.
* 두 피연산자(series) 중 하나라도 가지고 있지 않은 index가 있으면, 그 값은 **NaN**.

### dataframe operation

* column과 index를 동시에 고려하여 연산.
* 가능한 연산 : add, sub, div, mul
* series에서와 마찬가지로 하나라도 가지고 있지 않은 col, idx가 있으면 결과 값은 NaN.
* 연산의 `fill_value`를 통해 값 설정 가능. (없는 col, idx를 무슨 값으로 대체할 지 결정.)

### series, dataframe operation

* 그냥 +, - 등을 사용하면 연산이 되지 않음.
* axis를 지정.
* 지정된 aixs를 기준으로 broadcasting이 발생하여 연상.



## lambda, map, apply

### map

* `series.map()`
  * lambda 사용 가능.
  * dict 타입 입력 : index(key 값)에 맞추어 데이터 교체
  * series 타입 입력 : 같은 위치의 데이터로 교체

### apply

* 입력한 함수에  대해, series 전체에 해당 함수 적용.
  * ex) 특정 column의 최대값.
* `df.apply()`

### applymap

* series 단위가 아닌 element 단위로 함수 적용.



## built-in function

* `describe` : 숫자 타입 데이터의 요약
* `unique` : series의 유일한 값들
* 연산 함수
  * sum, sub, mean, min, max, count, median, mad, var 등
* `isnull` : null 값의 여부를 반환 (df와 shape이 같다.)
* `sort_values` : 정렬.
* `corr` : 상관계수.
  * `df.col1.corr(col2)`
* `cov` : 공분산.
  * `df.col1.cov(col2)`
* `corrwith` : 지정 col 외의 나머지 모든 col과의 상관계수
  * `df.corrwith(col)`
* `value_counts` : 각 값이 몇 개씩 있는 지.



## groupby

* 같은 데이터까리 묶음.
* `df.groupby('col1')['col2'].sum()`  
  * col1 : 묶음의 기준. (GROUP BY col1)
  * col2 : 연산을 적용 받는 column. (SUM(col2))
  * 여러 개의 column을 사용하여 묶을 수도 있음.

### **hierarchical index**

* 여러 개의 column을 사용하여 그룹핑을 한 경우, 결과의 index가 여러 개.
* 각 index에는 level이 존재.
* 특정 level을 지정하여, 해당 index를 기준으로만 연산 가능.

### grouped

* groupby에 의해 split된 상태.
* aggregation : `grouped.agg(연산)`
* transformation
  * 개별 데이터의 변환.
  * `grouped.transform(func)`
* filter
  * 특정 조건의 데이터 검색.
  * `grouped.filter(func(조건))`



## merge & concat

### merge

* 두 개의 데이터를 하나로 합침.
* `pd.merge(df1, df2, on='기준 column')`
* 기준 column의 이름이 양쪽이 다를 때 : `pd.merge(df1, df2, left_on='col1', right_on='col2')`
* join 방법 결정. `how=''` 
  * `left`
  * `right`
  * `outer`
  * `inner` : 기본값
* index based join
  * index를 기준으로 merge.
  * `right_index=True, left_index=True`

### concat

* 같은 column을 가지고 있는 데이터들을 붙임.



