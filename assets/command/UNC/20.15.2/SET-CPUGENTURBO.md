---
id: UNC@20.15.2@MMLCommand@SET CPUGENTURBO
type: MMLCommand
name: SET CPUGENTURBO（设置CPU睿频开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CPUGENTURBO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- CPU代际睿频
status: active
---

# SET CPUGENTURBO（设置CPU睿频开关）

## 功能

![](设置CPU睿频开关（SET CPUGENTURBO）_51335405.assets/notice_3.0-zh-cn_2.png)

如果配置不合理会导致权重计算产生偏差。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置不同CPU代际的睿频开关。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CPUGENERATION | TURBOSWITCH |
| --- | --- |
| Icelake | - |
| Skylake | - |
| Broadwell | - |
| Haswell | - |
| CascadeLake | - |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUGENERATION | CPU代际类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CPU代际类型。<br>数据来源：本端规划<br>取值范围：<br>- Icelake（Icelake代际）<br>- Skylake（kylake代际）<br>- Broadwell（Broadwell代际）<br>- Haswell（Haswell代际）<br>- CascadeLake（CascadeLake代际）<br>默认值：无。<br>配置原则：无 |
| TURBOSWITCH | 睿频开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置睿频的开关。<br>数据来源：本端规划<br>取值范围：<br>- OFF（OFF）<br>- ON（ON）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPUGENTURBO]] · CPU代际睿频开关（CPUGENTURBO）

## 使用实例

查询CPU代际类型为Icelake的代际开关：

```
SET CPUGENTURBO:CPUGENERATION=Icelake,TURBOSWITCH=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-CPUGENTURBO.md`
