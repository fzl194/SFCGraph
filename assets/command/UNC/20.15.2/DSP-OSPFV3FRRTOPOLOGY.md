---
id: UNC@20.15.2@MMLCommand@DSP OSPFV3FRRTOPOLOGY
type: MMLCommand
name: DSP OSPFV3FRRTOPOLOGY（查询OSPFv3的FRR拓扑信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFV3FRRTOPOLOGY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 查询OSPFv3的FRR拓扑信息
status: active
---

# DSP OSPFV3FRRTOPOLOGY（查询OSPFv3的FRR拓扑信息）

## 功能

该命令用于查询OSPFv3的FRR拓扑信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFV3FRRTOPOLOGY]] · OSPFv3的FRR拓扑信息（OSPFV3FRRTOPOLOGY）

## 使用实例

查询OSPFV3进程1的FRR拓扑信息：

```
DSP OSPFV3FRRTOPOLOGY:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
OSPFv3进程号  =  1
OSPFv3区域号  =  0.0.0.0
  路由器标识  =  10.10.10.1
     SPF类型  =  Router
 SPF节点标识  =  10.10.10.1
    节点类型  =  -|-|-|-
      开销值  =  1
      下一跳  =  2001:db8::1
      出接口  =  Eth66/0/3
  备份下一跳  =  ::
  备份出接口  =  NULL
   LFA开销值  =  0
    备份类型  =  None
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSPFV3FRRTOPOLOGY.md`
