---
id: UDG@20.15.2@MMLCommand@LST OSPFV3PRIFIXPRIORITY
type: MMLCommand
name: LST OSPFV3PRIFIXPRIORITY（查询OSPFv3路由收敛优先级配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFV3PRIFIXPRIORITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3路由收敛优先级配置
status: active
---

# LST OSPFV3PRIFIXPRIORITY（查询OSPFv3路由收敛优先级配置）

## 功能

该命令用于查询OSPFv3路由收敛优先级配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| PRIORITY | 路由优先级 | 可选必选说明：可选参数<br>参数含义：路由优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- critical：配置OSPFv3路由的收敛优先级为关键。<br>- high：配置OSPFv3路由的收敛优先级为高。<br>- medium：配置OSPFv3路由的收敛优先级为中。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3路由收敛优先级配置（OSPFV3PRIFIXPRIORITY）](configobject/UDG/20.15.2/OSPFV3PRIFIXPRIORITY.md)

## 使用实例

查询OSPFv3路由收敛优先级配置：

```
LST OSPFV3PRIFIXPRIORITY:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
    OSPFv3进程号  =  1
        拓扑标识  =  0
      路由优先级  =  High
IPv6前缀列表名称  =  IpPrefix
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPFv3路由收敛优先级配置（LST-OSPFV3PRIFIXPRIORITY）_00601161.md`
