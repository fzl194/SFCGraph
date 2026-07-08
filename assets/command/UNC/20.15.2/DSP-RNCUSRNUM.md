---
id: UNC@20.15.2@MMLCommand@DSP RNCUSRNUM
type: MMLCommand
name: DSP RNCUSRNUM（显示RNC下用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RNCUSRNUM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# DSP RNCUSRNUM（显示RNC下用户数）

## 功能

**适用网元：SGSN**

该命令用于查询RNC下的用户数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：整网规划<br>取值范围：<br>- “SYSTEM(整系统)”<br>- “BYRNC(基于RNC查询)”<br>默认值：<br>“SYSTEM(整系统)” |
| RNCMCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动国家号码。<br>前提条件：此参数在<br>“查询类型”<br>设置为<br>“BYRNC(基于RNC查询)”<br>后生效。<br>取值范围：3位数字<br>默认值：无 |
| RNCMNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定移动国家号码。<br>前提条件：此参数在<br>“查询类型”<br>设置为<br>“BYRNC(基于RNC查询)”<br>后生效。<br>取值范围：2～3位数字<br>默认值：无 |
| RNCID | RNC标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定RNC标识。<br>前提条件：此参数在<br>“查询类型”<br>设置为<br>“BYRNC(基于RNC查询)”<br>后生效。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RNCUSRNUM]] · RNC下用户数（RNCUSRNUM）

## 使用实例

查询RNC下所有用户数：

```
%%DSP RNCUSRNUM:TYPE=SYSTEM;%%
RETCODE = 0  操作成功。

RNC用户数信息
-------------
附着用户数  =  80000
（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RNCUSRNUM.md`
