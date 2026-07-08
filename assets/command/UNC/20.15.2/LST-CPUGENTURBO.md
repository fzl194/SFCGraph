---
id: UNC@20.15.2@MMLCommand@LST CPUGENTURBO
type: MMLCommand
name: LST CPUGENTURBO（查询CPU代际睿频开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPUGENTURBO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- CPU代际睿频
status: active
---

# LST CPUGENTURBO（查询CPU代际睿频开关）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询不同CPU代际睿频的开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUGENERATION | CPU代际类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU代际类型。<br>数据来源：本端规划<br>取值范围：<br>- Icelake（Icelake代际）<br>- Skylake（kylake代际）<br>- Broadwell（Broadwell代际）<br>- Haswell（Haswell代际）<br>- CascadeLake（CascadeLake代际）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [CPU代际睿频开关（CPUGENTURBO）](configobject/UNC/20.15.2/CPUGENTURBO.md)

## 使用实例

查询CPU代际类型为Icelake的代际开关：

```
LST CPUGENTURBO:CPUGENERATION=Icelake;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CPU代际睿频开关（LST-CPUGENTURBO）_51175625.md`
