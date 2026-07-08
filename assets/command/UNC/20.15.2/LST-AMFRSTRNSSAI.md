---
id: UNC@20.15.2@MMLCommand@LST AMFRSTRNSSAI
type: MMLCommand
name: LST AMFRSTRNSSAI（查询TA级限制切片）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFRSTRNSSAI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片选择管理
- TA级限制切片管理
status: active
---

# LST AMFRSTRNSSAI（查询TA级限制切片）

## 功能

**适用NF：AMF**

该命令用于查询TA级限制切片信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSTRAREARANGE | 限制区域范围 | 可选必选说明：可选参数<br>参数含义：该参数用于配置TA级限制切片所属区域的范围：所有区域或者指定区域编码。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_AREA（所有区域）”：所有区域<br>- “AREA_CODE（指定区域编码）”：指定区域编码<br>默认值：无<br>配置原则：<br>对于限制区域范围，TA级限制切片的匹配优先级从高到低依次为：“AREA_CODE(指定区域编码)”，“ALL_AREA(所有区域)”。 |
| RSTRAREACODE | 限制区域编码 | 可选必选说明：该参数在"RSTRAREARANGE"配置为"AREA_CODE"时为条件可选参数。<br>参数含义：该参数用于配置TA级限制切片所属的具体区域信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。该限制区域编码必须通过ADD RSTRNSAREACODE命令成功添加，可执行LST RSTRNSAREACODE进行查看。区域编码内的成员由ADD RSTRNSAREAMEM添加。<br>默认值：无<br>配置原则：无 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TA级限制切片应用的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），TA级限制切片的匹配优先级从高到低依次为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用TA级限制切片的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFRSTRNSSAI]] · TA级限制切片（AMFRSTRNSSAI）

## 使用实例

查询系统中当前配置的TA级限制信息，执行如下命令：

```
%%LST AMFRSTRNSSAI:;%%
RETCODE = 0  操作成功

结果如下
--------
限制区域范围  =  指定区域编码
限制区域编码  =  SH_5G_TRIAL_NETWORK
    用户范围  =  外网用户
    IMSI前缀  =  NULL
切片业务类型  =  1
切片细分标识  =  FFFFFF
    描述信息  =  NULL
(结果个数  = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFRSTRNSSAI.md`
