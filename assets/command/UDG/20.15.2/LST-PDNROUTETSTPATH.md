---
id: UDG@20.15.2@MMLCommand@LST PDNROUTETSTPATH
type: MMLCommand
name: LST PDNROUTETSTPATH（查询UPF向PDN服务器发送探测消息的探测路径配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PDNROUTETSTPATH
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- PDN侧路由探测
status: active
---

# LST PDNROUTETSTPATH（查询UPF向PDN服务器发送探测消息的探测路径配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询UPF向PDN服务器自动发送探测消息的路径配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHNAME | 路径名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用于连通性探测的路径名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的路径名称应满足路径名称的取值范围。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PDNROUTETSTPATH]] · UPF向PDN服务器发送探测消息的探测路径配置（PDNROUTETSTPATH）

## 使用实例

查询配置路径名称为test1的探测路径配置：

```
LST PDNROUTETSTPATH: PATHNAME="test1";
```

```

RETCODE = 0  Operation succeeded

UPF向PDN服务器发送探测消息的探测路径配置
------------------------
                      Path Name  =  test1
                      Path Type  =  DNS
                      Pool Name  =  pool-test
                IP Address Type  =  IPV4
       Destination IPv4 Address  =  10.1.1.1
Destination IPv6 Prefix Address  =  ::
                     DSCP Value  =  0
              Route Test Method  =  PING
          Packet Payload Length  =  100
            Traffic-Class Value  =  0
                         domain  =  NULL
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询UPF向PDN服务器发送探测消息的探测路径配置（LST-PDNROUTETSTPATH）_63911221.md`
