---
id: UNC@20.15.2@MMLCommand@LST APNNONIPFUNC
type: MMLCommand
name: LST APNNONIPFUNC（查询APN Non-IP功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNNONIPFUNC
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- APN的Non-IP配置
status: active
---

# LST APNNONIPFUNC（查询APN Non-IP功能配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于查询指定APN的网关Non-IP功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNONIPFUNC]] · APN Non-IP功能配置（APNNONIPFUNC）

## 使用实例

显示指定APN的网关Non-IP功能状态： 查询整机APN的网关Non-IP功能状态：

```
%%LST APNNONIPFUNC: APN="apn1";%%
RETCODE = 0  操作成功

结果如下
--------
               APN  =  apn1
APN Non-IP功能开关  =  继承全局
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNNONIPFUNC.md`
