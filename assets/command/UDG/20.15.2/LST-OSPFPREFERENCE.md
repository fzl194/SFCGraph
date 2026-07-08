---
id: UDG@20.15.2@MMLCommand@LST OSPFPREFERENCE
type: MMLCommand
name: LST OSPFPREFERENCE（查询OSPF协议路由的优先级配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFPREFERENCE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF协议路由的优先级配置
status: active
---

# LST OSPFPREFERENCE（查询OSPF协议路由的优先级配置）

## 功能

该命令用于查询OSPF协议路由的优先级配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| ROUTETYPE | 路由类型 | 可选必选说明：可选参数<br>参数含义：路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- default：区域内和区域间路由。<br>- ase：AS-External路由。<br>- intra：区域内路由。<br>- inter：区域间路由。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFPREFERENCE]] · OSPF协议路由的优先级配置（OSPFPREFERENCE）

## 使用实例

查询OSPF进程1下ASE路由的优先级配置：

```
LST OSPFPREFERENCE:PROCID=1,ROUTETYPE=ase;
```

```

RETCODE = 0  操作成功。

结果如下
----------
      进程号  =  1
    拓扑标识  =  0
    路由类型  =  AS-External路由
  路由优先级  =  150
路由策略名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OSPFPREFERENCE.md`
