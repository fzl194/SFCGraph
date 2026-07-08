---
id: UNC@20.15.2@MMLCommand@LST ASRCHN
type: MMLCommand
name: LST ASRCHN（查询容灾业务通道配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ASRCHN
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 主备容灾管理
- 容灾业务通道
status: active
---

# LST ASRCHN（查询容灾业务通道配置）

## 功能

**适用网元：SGSN、MME**

该命令已废弃。

此命令用于查询主备网元之间的容灾业务通道配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ASRCHN]] · 容灾业务通道配置（ASRCHN）

## 使用实例

查询系统已有容灾业务通道。

LST ASRCHN:;

```
%%LST ASRCHN:;%%
RETCODE = 0  Operation Success.

操作结果如下
------------------------
                                容灾业务通道ID     =  0
                              容灾业务通道本端IP1  =  192.168.1.1
                              容灾业务通道本端IP1  =  192.168.1.2
                             容灾业务通道本端端口  =  18100
                              容灾业务通道对端IP1  =  192.168.1.3
                              容灾业务通道对端IP2  =  192.168.1.4
                             容灾业务通道对端端口  =  18100
                                          VPN名称  =  NULL
                        探测报文发送周期 （毫秒）  =  1000
                                 探测报文重传次数  =  15
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容灾业务通道配置(LST-ASRCHN)_72225807.md`
