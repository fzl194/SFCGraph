---
id: UNC@20.15.2@MMLCommand@DSP SERVICERUSTATE
type: MMLCommand
name: DSP SERVICERUSTATE（查询业务RU的状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SERVICERUSTATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- 业务RU状态
status: active
---

# DSP SERVICERUSTATE（查询业务RU的状态）

## 功能

该命令用于查询当前所有RU的信息。

## 注意事项

- 该命令如果输入RUID，则查询指定RUID的RU信息。
- 如果命令输入的RUID在记录中不存在，则返回无效结果。
- 该命令不输入RUID，则查询所有RU的信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：可选参数。<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294<br>默认值：无。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。数据来源：本端规划<br>取值范围：字符串类型，通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**[LST VNFC](../../../../单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)**<br>命令查询到的管理代理标识，不支持对"VNFC类型名称"为VNFP、VNRS_VNFC、ACS、IPSEC_VNFC的RU状态查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVICERUSTATE]] · RU的信息（SERVICERUSTATE）

## 使用实例

显示当前所有RU的状态。

```
DSP SERVICERUSTATE:
SERVICEINSTANCE="CSLB_VNFC_999"
;
```

```
RETCODE = 0  操作成功。

结果如下
--------
RU的ID  RU的名字         ScaleGroup的名字   RU的状态 
64      CSLB_IP_RU_0064   SG0_CSLB_IPFWD      RU正常   
65      CSLB_IP_RU_0065   SG0_CSLB_IPFWD      RU正常 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询业务RU的状态(DSP-SERVICERUSTATE)_29626970.md`
