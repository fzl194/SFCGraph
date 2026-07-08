---
id: UNC@20.15.2@MMLCommand@ADD HTRIMSICFG
type: MMLCommand
name: ADD HTRIMSICFG（增加HTR号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HTRIMSICFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 5000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- HTR流控局向管理
- Gr HTR流控局向管理
- 配置局向关联号段
status: active
---

# ADD HTRIMSICFG（增加HTR号段）

## 功能

**适用网元：SGSN**

该命令用于添加一个HTR局向的具体IMSI号段。只有当HTROFC配置表中 “HTR局向索引” 对应的 “局向流控开关” 为 “YES” 时，本命令所配置的各个IMSI号段才进行流控，可执行 [**LST HTROFC**](../配置局向/查询HTR局向(LST HTROFC)_26305964.md) 进行查看。

## 注意事项

- 该命令执行后立即生效。
- 该表的最大记录数为5000。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>数据来源：整网规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| HTROFCINDEX | HTR局向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTR局向索引。<br>前提条件：该参数必须在HTROFC表中事先配置。可使用<br>[**LST HTROFC**](../配置局向/查询HTR局向(LST HTROFC)_26305964.md)<br>命令查询。<br>数据来源：整网规划<br>取值范围：0~9<br>默认值：无 |

## 操作的配置对象

- [HTR号段（HTRIMSICFG）](configobject/UNC/20.15.2/HTRIMSICFG.md)

## 使用实例

增加记录，添加IMSI前缀为“123030001”，HTR局向索引为5：

ADD HTRIMSICFG: IMSIPRE="123030001", HTROFCINDEX=5;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加HTR号段(ADD-HTRIMSICFG)_26305960.md`
