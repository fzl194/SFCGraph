---
id: UDG@20.15.2@MMLCommand@DSP SDRTOKEN
type: MMLCommand
name: DSP SDRTOKEN（查询SDRC中的TOKEN信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRTOKEN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRTOKEN（查询SDRC中的TOKEN信息）

## 功能

该命令用于查询SDRC中指定AppType的TOKEN策略信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | App类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示该Token所归属业务的类型，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=Token;命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRTOKEN]] · SDRC中的TOKEN信息（SDRTOKEN）

## 使用实例

使用如下命令查询SDRC中缓存的token策略信息：

```
%%DSP SDRTOKEN: APPTYPE=1035;%%
RETCODE = 0  操作成功

结果如下
--------
根令牌ID  主实例ID              新主实例ID            令牌组  下一跳组ID  App类型  多进程模式  内部进程号  外部进程号

0         13568649970415061474  13568649970415061474     0      0          1035       0            0           0
1         13568649970415061474  13568649970415061474     0      0          1035       0            0           0
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SDRC中的TOKEN信息（DSP-SDRTOKEN）_94730435.md`
