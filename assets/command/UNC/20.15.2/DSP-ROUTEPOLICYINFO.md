---
id: UNC@20.15.2@MMLCommand@DSP ROUTEPOLICYINFO
type: MMLCommand
name: DSP ROUTEPOLICYINFO（显示路由策略信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ROUTEPOLICYINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- 查询路由策略信息
status: active
---

# DSP ROUTEPOLICYINFO（显示路由策略信息）

## 功能

该命令用于显示路由策略的基本信息。包括匹配计数信息的显示。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROUTEPOLICYINFO]] · 路由策略信息（ROUTEPOLICYINFO）

## 使用实例

显示路由策略基本信息：

```
DSP ROUTEPOLICYINFO:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
路由策略节点号          匹配模式       路由策略名字         路由策略节点描述              匹配路由数       路由策略类型      引用计数
0                       允许           kkk                  NULL                          0                匹配路由开销      1
1                       允许           kkk                  NULL                          0                匹配路由标签      1
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ROUTEPOLICYINFO.md`
