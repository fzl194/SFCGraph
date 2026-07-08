---
id: UDG@20.15.2@MMLCommand@DSP OSPFTOPOLOGY
type: MMLCommand
name: DSP OSPFTOPOLOGY（查询OSPF拓扑信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFTOPOLOGY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF拓扑信息
status: active
---

# DSP OSPFTOPOLOGY（查询OSPF拓扑信息）

## 功能

该命令用于查询OSPF拓扑信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：可选参数<br>参数含义：OSPF区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFTOPOLOGY]] · OSPF拓扑信息（OSPFTOPOLOGY）

## 使用实例

查询OSPF进程1的拓扑信息：

```
DSP OSPFTOPOLOGY:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
 OSPF进程号  =  1
     区域号  =  0.0.0.0
 路由器标识  =  10.10.10.1
    SPF类型  =  Router
SPF节点标识  =  10.10.10.1
   节点类型  =  -|-|-|-
     开销值  =  0
     下一跳  =  0.0.0.0
     出接口  =  NULL
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF拓扑信息（DSP-OSPFTOPOLOGY）_50280618.md`
