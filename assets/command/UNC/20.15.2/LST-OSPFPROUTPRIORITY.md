---
id: UNC@20.15.2@MMLCommand@LST OSPFPROUTPRIORITY
type: MMLCommand
name: LST OSPFPROUTPRIORITY（查询OSPF路由的收敛优先级配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFPROUTPRIORITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF路由的收敛优先级配置
status: active
---

# LST OSPFPROUTPRIORITY（查询OSPF路由的收敛优先级配置）

## 功能

该命令用于查询OSPF路由的收敛优先级配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| PRIORITY | 收敛优先级 | 可选必选说明：可选参数<br>参数含义：收敛优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- critical：配置OSPF路由的收敛优先级为关键。<br>- high：配置OSPF路由的收敛优先级为高。<br>- medium：配置OSPF路由的收敛优先级为中。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFPROUTPRIORITY]] · OSPF路由的收敛优先级配置（OSPFPROUTPRIORITY）

## 使用实例

查询OSPF路由的收敛优先级配置：

```
LST OSPFPROUTPRIORITY:;
```

```

RETCODE = 0  操作成功。

结果如下
------------
    进程号  =  1
  拓扑标识  =  0
收敛优先级  =  Critical
    前缀名  =  IpPrefix
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OSPFPROUTPRIORITY.md`
