---
id: UNC@20.15.2@MMLCommand@LST APNGA5GREUSEAVP
type: MMLCommand
name: LST APNGA5GREUSEAVP（查询基于apn的Ga接口重用字段的填写方式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNGA5GREUSEAVP
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 话单字段控制
- 5G用户话单重用字段控制
status: active
---

# LST APNGA5GREUSEAVP（查询基于apn的Ga接口重用字段的填写方式）

## 功能

**适用NF：PGW-C**

该命令用于查询指定APN 5G用户接入时，Ga接口重用字段的填写方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”；该参数取值应与ADD APN命令中参数“APN”保持一致，使用该前需通过ADD APN添加一组记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNGA5GREUSEAVP]] · 基于apn的Ga接口重用字段的填写方式（APNGA5GREUSEAVP）

## 使用实例

对指定APN的5G用户，当需要查询其Ga接口重用字段的填写方式时，使用该命令。

```
%%LST APNGA5GREUSEAVP:;%%
RETCODE = 0  操作成功
结果如下
------------------------
APN名称  无线接入技术      用户位置信息  服务节点类型  

APN.APN   Disable  Enable                           Enable             
APN1      Disable  Enable                           Enable             
(结果个数 = 2)

---    END

2. 2. %%LST APNGA5GREUSEAVP:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                       APN名称  =  APNGA
                        无线接入技术  =  Enable
                       用户位置信息  =  Enable
              服务节点类型  =  Enable
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNGA5GREUSEAVP.md`
