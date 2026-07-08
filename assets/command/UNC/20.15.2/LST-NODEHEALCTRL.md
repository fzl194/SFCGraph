---
id: UNC@20.15.2@MMLCommand@LST NODEHEALCTRL
type: MMLCommand
name: LST NODEHEALCTRL（查询Node自愈策略控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NODEHEALCTRL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST NODEHEALCTRL（查询Node自愈策略控制参数）

## 功能

该命令用于查询Node自愈策略控制参数。

## 注意事项

该命令中部分功能在第三方CaaS场景下不可使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [Node自愈策略控制参数（NODEHEALCTRL）](configobject/UNC/20.15.2/NODEHEALCTRL.md)

## 使用实例

查询Node自愈策略控制参数。

```
%%LST NODEHEALCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
        Bonding自愈控制  =  使能
       存储故障倒换开关  =  使能
部分Pod故障升级自愈控制  =  去使能
全部Pod故障升级自愈控制  =  使能
    Pod拓扑核查自愈控制  =  使能
   Fabric平面断隔离控制  =  去使能
     NP链路故障隔离控制  =  去使能
         VF故障隔离控制  =  使能
       存储过载自愈控制  =  去使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Node自愈策略控制参数（LST-NODEHEALCTRL）_48332254.md`
