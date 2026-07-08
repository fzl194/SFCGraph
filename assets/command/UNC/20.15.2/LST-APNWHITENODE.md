---
id: UNC@20.15.2@MMLCommand@LST APNWHITENODE
type: MMLCommand
name: LST APNWHITENODE（查询APN设备白名单列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNWHITENODE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- APN设备白名单
status: active
---

# LST APNWHITENODE（查询APN设备白名单列表）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询APN设备白名单。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令<br>[**ADD APN**](../../APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>配置。 |
| NODETYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元类型。<br>数据来源：本端规划<br>取值范围：<br>- SGW（SGW）<br>- SMF（SMF）<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：该参数在"NODETYPE"配置为"SGW"时为条件可选参数。<br>参数含义：该参数用于指定SGW设备的地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNWHITENODE]] · APN设备白名单（APNWHITENODE）

## 使用实例

当需要查询APN设备白名单时，可以执行如下命令

```
%%LST APNWHITENODE:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------                  	
         APN名称  =  huawei.com1
        网元类型  =  SGW
      IP地址类型  =  IPV4
IPv4地址段的地址  =  10.10.10.2
    IPv4掩码长度  =  32
IPv6地址段的地址  =  ::
    IPv6掩码长度  =  128
      NF实例标识  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN设备白名单列表（LST-APNWHITENODE）_58382748.md`
