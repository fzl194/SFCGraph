---
id: UNC@20.15.2@MMLCommand@LST APNIPALLOCRULE
type: MMLCommand
name: LST APNIPALLOCRULE（查询基于APN的地址分配规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNIPALLOCRULE
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配规则配置
status: active
---

# LST APNIPALLOCRULE（查询基于APN的地址分配规则）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询指定APN或全部的基于APN地址分配规则。

## 注意事项

该命令指定APN实例名时，表示查询指定APN实例的基于APN的地址分配规则。不指定APN实例名时，表示查询所有基于APN的地址分配规则。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，其中字母不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [基于APN的地址分配规则（APNIPALLOCRULE）](configobject/UNC/20.15.2/APNIPALLOCRULE.md)

## 使用实例

显示名为apn1.com的APN实例的基于APN地址分配规则：

```
%%LST APNIPALLOCRULE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
APN名称  IPv4地址分配属性  IPv4第一级规则开关 IPv4第一级规则  IPv4第二级规则开关  IPv4第二级规则  IPv4第三级规则开关  IPv4第三级规则  IPv6地址分配属性  IPv6第一级规则开关 IPv6第一级规则  IPv6第二级规则开关  IPv6第二级规则  IPv6第三级规则开关  IPv6第三级规则
01        继承全局配置      去使能              NULL             去使能              NULL             去使能               NULL             继承全局配置      去使能             NULL             去使能               NULL             去使能               NULL             
02        继承全局配置      去使能              NULL             去使能              NULL             去使能               NULL             继承全局配置      去使能             NULL             去使能               NULL             去使能               NULL             
03        继承全局配置      去使能              NULL             去使能              NULL             去使能               NULL             继承全局配置      去使能             NULL             去使能               NULL             去使能               NULL             
huawei    继承全局配置      去使能              NULL             去使能              NULL             去使能               NULL             继承全局配置      去使能             NULL             去使能               NULL             去使能               NULL             
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于APN的地址分配规则（LST-APNIPALLOCRULE）_49644918.md`
