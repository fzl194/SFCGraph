---
id: UDG@20.15.2@MMLCommand@LST APNSAPARA
type: MMLCommand
name: LST APNSAPARA（查询基于APN的业务感知参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNSAPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- SA公共参数
status: active
---

# LST APNSAPARA（查询基于APN的业务感知参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示基于APN的业务感知参数配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：可选参数<br>参数含义：用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：APN实例名称是通过ADD APN命令配置的。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNSAPARA]] · 基于APN的业务感知参数（APNSAPARA）

## 使用实例

显示基于APN的业务感知参数：

```
LST APNSAPARA: APNNAME="apn1";
```

```

RETCODE = 0  操作成功

基于APN的业务感知参数
---------------------
                      APN名称  =  apn1
 业务流策略确认的最大解析次数  =  4
HTTPS业务流进行解析的最大包数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询基于APN的业务感知参数（LST-APNSAPARA）_49128369.md`
