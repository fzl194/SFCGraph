---
id: UNC@20.15.2@MMLCommand@SET NRFDISCREGNRULE
type: MMLCommand
name: SET NRFDISCREGNRULE（设置服务发现区域识别规则）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFDISCREGNRULE
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF服务发现区域识别规则配置管理
status: active
---

# SET NRFDISCREGNRULE（设置服务发现区域识别规则）

## 功能

**适用NF：NRF**

该命令用于设置NRF服务发现区域识别规则，通过该规则可以提取NF的区域信息，以便进行区域相关的服务发现逻辑决策。

## 注意事项

- 该命令执行后立即生效。

- 参数REGIONSTART的与参数REGIONLENGTH的值之和需要小于等于36。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFTYPE | REGNEXTMACSW | REGIONSTART | REGIONLENGTH |
| --- | --- | --- | --- |
| CUSTOM_OCS | FUNC_OFF | 0 | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示目标NF类型。<br>数据来源：全网规划<br>取值范围：<br>- CUSTOM_OCS（CUSTOM_OCS）<br>默认值：无。<br>配置原则：无 |
| REGNEXTMACSW | 区域关系精确匹配开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在CHF发现OCS流程中是否根据CHF与OCS的区域关系来控制发现结果的精确匹配度。开关打开时，当CHF与OCS处于同区域，则NRF服务发现结果携带OCS的全量信元信息；当CHF与OCS处于不同区域，则NRF服务发现结果针对SUPI号段、GPSI号段、DNN列表、TAI列表等数据量较大的信元，只携带匹配上的信元信息。开关关闭时，发现过程中不进行区域关系的判断。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |
| REGIONSTART | 区域信息起始位置 | 可选必选说明：该参数在"REGNEXTMACSW"配置为"FUNC_ON"时为条件必选参数。<br>参数含义：该参数表示NF实例标识中大区或省份信息的起始位置。假设其取值为N，N表示NF Instance ID中的第N+1个字符。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~35。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFDISCREGNRULE查询当前参数配置值。<br>配置原则：无 |
| REGIONLENGTH | 区域信息长度 | 可选必选说明：该参数在"REGNEXTMACSW"配置为"FUNC_ON"时为条件必选参数。<br>参数含义：该参数表示NF实例标识中大区或省份信息的长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~36。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFDISCREGNRULE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDISCREGNRULE]] · 服务发现区域识别规则（NRFDISCREGNRULE）

## 使用实例

设置服务发现区域识别规则，打开区域关系精确匹配开关，设置区域信息起始位置和区域信息长度。

```
SET NRFDISCREGNRULE: NFTYPE=CUSTOM_OCS, REGNEXTMACSW=FUNC_ON, REGIONSTART=3, REGIONLENGTH=8;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NRFDISCREGNRULE.md`
