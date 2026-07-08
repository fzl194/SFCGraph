---
id: UNC@20.15.2@MMLCommand@LST MAPCMPTBYIMSI
type: MMLCommand
name: LST MAPCMPTBYIMSI（查询MAP协议接口兼容性IMSI号段配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MAPCMPTBYIMSI
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- MAP应用协议
- MAP功能配置
status: active
---

# LST MAPCMPTBYIMSI（查询MAP协议接口兼容性IMSI号段配置）

## 功能

**适用网元：SGSN**

该命令用于查询MAP协议接口兼容性IMSI号段配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MAP兼容性参数策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MAPCMPTBYIMSI]] · MAP协议接口兼容性IMSI号段配置（MAPCMPTBYIMSI）

## 使用实例

配置方式：查询所有MAP协议接口兼容性IMSI号段配置记录

LST MAPCMPTBYIMSI:;

```
%%LST MAPCMPTBYIMSI:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
                    用户范围  =  所有用户
                  运营商标识  =  0
                    IMSI前缀  =  NULL
                    特性列表  =  支持双连接
未签约DCNR是否支持高速用户面  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MAPCMPTBYIMSI.md`
