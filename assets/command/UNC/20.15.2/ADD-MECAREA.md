---
id: UNC@20.15.2@MMLCommand@ADD MECAREA
type: MMLCommand
name: ADD MECAREA（增加5G MEC区域信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MECAREA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- 本地特色业务区域管理
- 本地特色业务区域标识管理
status: active
---

# ADD MECAREA（增加5G MEC区域信息）

## 功能

**适用NF：AMF**

该命令用于增加5G MEC区域信息，位于特定区域的用户可以访问本地特色业务。

## 注意事项

- 下一次移动性流程生效。

- 区域类型为“HIGH_RAIL_AREA”的MEC区域仅支持增加跟踪区成员。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域标识 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一标识AMF服务的某个区域（例如：商场）。其服务范围可以通过ADD MECAREATAI或ADD MECAREAGNB进行配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：<br>当通过RMV MECAREA命令删除“AREAID”区域成员时，请执行LST MECAREATAI和LST MECAREAGNB命令，确保中“AREAID”未被索引。 |
| SERVINGSCOPE | 服务范围 | 可选必选说明：必选参数<br>参数含义：该参数用于描述目标PCF的服务范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。如果输入多个服务范围，那么使用“:”作为分隔符，比如“pudong:puxi”。<br>默认值：无<br>配置原则：<br>NRF针对“服务范围”是按照“包含”的逻辑进行处理的，即目标PCF能为发现请求中携带的所有服务范围提供服务，NRF才会认为其满足条件；故本参数在输入时应避免输入无效的服务范围。 |
| AREATYPE | 区域类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识当前区域的区域类型。<br>数据来源：全网规划<br>取值范围：<br>- PUBLIC_AREA（公网区域）<br>- HIGH_RAIL_AREA（高铁区域）<br>默认值：PUBLIC_AREA<br>配置原则：<br>若本参数发生变更，可能会使已建立AM策略的用户无法应用变更后的AM策略。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于描述区域信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MECAREA]] · 5G MEC区域信息（MECAREA）

## 使用实例

针对标识为“1”的区域（例如：西湖景区）的用户，可以访问本地特性业务，执行如下命令：

```
ADD MECAREA: AREAID=1, SERVINGSCOPE="West Lake", DESC="West Lake";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MECAREA.md`
