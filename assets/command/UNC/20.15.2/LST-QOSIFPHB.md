---
id: UNC@20.15.2@MMLCommand@LST QOSIFPHB
type: MMLCommand
name: LST QOSIFPHB（查询禁止QoS优先级映射的类型）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSIFPHB
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- QoS IF PHB
status: active
---

# LST QOSIFPHB（查询禁止QoS优先级映射的类型）

## 功能

该命令用于列举接口下的禁止PHB映射的实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| PHBTYPE | 出接口报文的优先级字段映射类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置出接口报文的优先级字段映射类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- dscp：IP报文的DSCP。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSIFPHB]] · 禁止QoS优先级映射的类型（QOSIFPHB）

## 使用实例

查询在接口Ethernet66/0/3下禁止PHB映射的实例：

```
LST QOSIFPHB:IFNAME="Ethernet66/0/3";
```

```

RETCODE = 0 操作成功

结果如下
--------
                      接口名称  =  Ethernet66/0/3
出接口报文的优先级字段映射类型  =  IP报文的DSCP
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSIFPHB.md`
