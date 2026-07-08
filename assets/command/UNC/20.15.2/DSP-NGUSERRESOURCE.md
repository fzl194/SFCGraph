---
id: UNC@20.15.2@MMLCommand@DSP NGUSERRESOURCE
type: MMLCommand
name: DSP NGUSERRESOURCE（显示5G用户资源）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGUSERRESOURCE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP NGUSERRESOURCE（显示5G用户资源）

## 功能

**适用NF：AMF**

该命令用于按条件查询AMF系统内各种用户状态的统计结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYSCOPE | 查询范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询5G用户资源的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY（汇总信息）”：查询5G用户资源的汇总信息。<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- “BASICUSERNUM（基础用户数）”：查询基础的静态、动态用户数。<br>- “SRVPLMN（Serving PLMN）”：查询指定Serving PLMN注册的用户数信息。<br>- “HOMEPLMN（Home PLMN）”：查询指定Home PLMN注册的用户数信息。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：该参数在"QUERYTYPE"配置为"SRVPLMN"、"HOMEPLMN"时为条件必选参数。<br>参数含义：该参数用于指定移动国家号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"QUERYTYPE"配置为"SRVPLMN"、"HOMEPLMN"时为条件必选参数。<br>参数含义：该参数用于指定移动网络号码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G用户资源（NGUSERRESOURCE）](configobject/UNC/20.15.2/NGUSERRESOURCE.md)

## 使用实例

按Srving PLMN查看AMF上的用户数据统计结果，执行如下命令：

```
%%DSP NGUSERRESOURCE:QUERYSCOPE=SUMMARY,QUERYTYPE=SRVPLMN,MCC="123",MNC="68";%%
RETCODE = 0  操作成功

结果如下
------------------------
      移动国家码  =  123
        移动网号  =  68
      动态用户数  =  1000
  动态漫游用户数  =  500
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示5G用户资源（DSP-NGUSERRESOURCE）_07201321.md`
