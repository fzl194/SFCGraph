---
id: UNC@20.15.2@MMLCommand@ADD MODULE
type: MMLCommand
name: ADD MODULE（增加业务模块）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MODULE
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 业务模块
status: active
---

# ADD MODULE（增加业务模块）

## 功能

**适用NF：NCG**

该命令用于对CG的多对RU上的业务模块进行配置和维护管理。它包含添加、删除和查询业务模块命令，配置实现话单接收，分拣，转换，存储功能的模块，是CG核心业务处理部分。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 该命令最大记录数为256。
- 每个RU上最多配置4个业务模块，否则有资源不足的风险。
- 每个AP最多可以接入300条链路，AP的链路接入数量可以通过执行CHK ACTRL命令获取。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MNAME | 模块名 | 可选必选说明：必选参数<br>参数含义：用于表示一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- 首先执行[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)命令，查询出当前的RUID。该参数输入格式固定为'AP'接RUID_APID，APID值为1~4。例如：RUID为66时，该参数可以是“AP66_1”、“AP66_2”、“AP66_3”、“AP66_4”。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| AGID | 接入网元分组标识 | 可选必选说明：必选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该值需要执行[**LST CDRPROC**](../话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询“接入网元分组标识”。如果没有符合要求的“接入网元分组标识”，还需执行[**ADD CDRPROC**](../话单处理/增加话单处理（ADD CDRPROC）_51174272.md)命令增加。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| RUROLE | RU角色 | 可选必选说明：可选参数<br>参数含义：用于指定当前RU角色。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CONVERGE：汇聚RU。<br>- SERVICE：业务RU。<br>默认值：无。<br>说明：如果BI收敛开关未开启，该参数默认值为空；如果BI收敛开关开启，该参数默认值动态判断：如果该MODULE所在RU配置了BI口IP或者RESERVEDIP，则默认值为汇聚RU，如果没有配置BI口IP或者RESERVEDIP，则默认值为业务RU。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MODULE]] · 业务模块（MODULE）

## 使用实例

增加一个“接入网元分组标识”为“PS_GROUP_1”的业务模块，示例如下：

```
ADD MODULE: MNAME="AP66_1", AGID="PS_GROUP_1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MODULE.md`
