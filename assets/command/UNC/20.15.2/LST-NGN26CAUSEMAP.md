---
id: UNC@20.15.2@MMLCommand@LST NGN26CAUSEMAP
type: MMLCommand
name: LST NGN26CAUSEMAP（查询5G N26接口原因值映射配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGN26CAUSEMAP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM流程管理
- 5G N26接口原因值映射配置
status: active
---

# LST NGN26CAUSEMAP（查询5G N26接口原因值映射配置）

## 功能

**适用NF：AMF**

该命令用于查询5G N26接口原因值映射配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROT | 流程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流程类型，根据场景来确认是否需要配置相应的流程。<br>数据来源：全网规划<br>取值范围：<br>- LTE_TO_NR_HO（EPC到5GC切换）<br>- NR_TO_LTE_ATTACH（5GS到LTE附着）<br>- NR_TO_LTE_TAU（5GS到LTE TAU）<br>- ALL（所有的失败流程）<br>- RESERV_PROC1（预留字段1）<br>- RESERV_PROC2（预留字段2）<br>默认值：无<br>配置原则：<br>指定流程和“ALL”类型同时配置时，指定流程配置的原因值映射优先级高于“ALL”类型配置的原因值映射。 |
| SCAUSE | 原始原因值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下发到MME的原始原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGN26CAUSEMAP]] · 5G N26接口原因值映射配置（NGN26CAUSEMAP）

## 使用实例

- 不输入查询条件，查询表中全部5G N26接口原因值映射配置记录，执行如下命令：
  ```
  %%LST NGN26CAUSEMAP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  流程类型      原始原因值   目标原因值  

  EPC到5GC切换  96           54      
  5GS到LTE附着  96           54      
  (结果个数 = 2)

  ---    END
  ```
- 查询流程类型为5GS到LTE附着，原始原因值为96的5G N26接口原因值映射配置记录，执行如下命令：
  ```
  %%LST NGN26CAUSEMAP:PROT=NR_TO_LTE_ATTACH,SCAUSE=96;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    流程类型  =  5GS到LTE附着
  原始原因值  =  96
  目标原因值  =  54
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-N26接口原因值映射配置（LST-NGN26CAUSEMAP）_70798977.md`
