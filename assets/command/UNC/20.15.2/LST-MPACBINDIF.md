---
id: UNC@20.15.2@MMLCommand@LST MPACBINDIF
type: MMLCommand
name: LST MPACBINDIF（查询MPAC接口策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MPACBINDIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 接口策略配置
status: active
---

# LST MPACBINDIF（查询MPAC接口策略）

## 功能

该命令用于查询接口MPAC策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定绑定策略生效的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：无 |

## 操作的配置对象

- [MPAC接口策略（MPACBINDIF）](configobject/UNC/20.15.2/MPACBINDIF.md)

## 使用实例

查询MPAC接口策略：

```
LST MPACBINDIF:IFNAME="Ethernet64/0/3",IPVERSION=IPv4;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
            接口名称  =  Ethernet64/0/3
              IP版本  =  IPv4
        IPv4策略名称  =  policyV4
        IPv6策略名称  =  NULL
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MPAC接口策略（LST-MPACBINDIF）_00865717.md`
