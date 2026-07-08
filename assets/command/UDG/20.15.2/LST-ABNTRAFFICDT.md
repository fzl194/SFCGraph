---
id: UDG@20.15.2@MMLCommand@LST ABNTRAFFICDT
type: MMLCommand
name: LST ABNTRAFFICDT（查询异常流量功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ABNTRAFFICDT
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- APN下终端异常下行流量检测开关
status: active
---

# LST ABNTRAFFICDT（查询异常流量功能开关）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询APN下终端异常下行流量检测开关信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该APN必须是系统已经配置的APN，此功能不支持别名APN的配置使能。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ABNTRAFFICDT]] · 异常流量检测开关（ABNTRAFFICDT）

## 使用实例

查询名称为“apn1.com”的APN的终端异常下行流量检测功能的开关信息：

```
LST ABNTRAFFICDT: APN="apn1.com";
```

```

RETCODE = 0  Operation succeeded

Abnormal Traffic Detect Switch
------------------------------
                          APN  =  apn1.com
                       Switch  =  ENABLE
Traffic Behavior Based Switch  =  ENABLE
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ABNTRAFFICDT.md`
