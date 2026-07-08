---
id: UNC@20.15.2@MMLCommand@LST LDPIF
type: MMLCommand
name: LST LDPIF（查询LDP接口配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LDPIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP接口管理
status: active
---

# LST LDPIF（查询LDP接口配置）

## 功能

该命令用于查询LDP接口配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [LDP接口（LDPIF）](configobject/UNC/20.15.2/LDPIF.md)

## 使用实例

查询LDP接口配置：

```
LST LDPIF:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                     VPN实例名称  =  _public_
                          接口名  =  Ethernet64/0/5
    Hello定时器发送时间间隔（s）  =  NULL
          Hello保持定时器值（s）  =  15
      Keepalive发送时间间隔（s）  =  NULL
      Keepalive保持定时器值（s）  =  45
                  传输地址接口名  =  NULL
 接口配置的IgpSynDelayTimer（s）  =  10
              本地LSR ID绑定接口  =  NULL
                    标签发布模式  =  DU
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LDP接口配置（LST-LDPIF）_00441113.md`
