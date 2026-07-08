---
id: UNC@20.15.2@MMLCommand@LST CPUABILITYCFG
type: MMLCommand
name: LST CPUABILITYCFG（查询不同CPU类型的能力系数和基础消耗。）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPUABILITYCFG
command_category: 查询类
applicable_nf:
- GGSN
- SGW-C
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 权重分配管理
- CPU能力系数策略
status: active
---

# LST CPUABILITYCFG（查询不同CPU类型的能力系数和基础消耗。）

## 功能

**适用NF：GGSN、SGW-C、SMF、PGW-C**

该命令用于查询不同CPU类型的能力系数和基础消耗。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPUTYPE | CPU类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CPU类型。<br>数据来源：本端规划<br>取值范围：<br>- X86_64（X86机器CPU类型）<br>- Aarch（ARM机器CPU类型）<br>默认值：无<br>配置原则：无 |
| CPUGENERATE | CPU代际 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CPU代际。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。当cpu类型是ARM时，固定字符“arch64”，其他字符不生效。<br>默认值：无<br>配置原则：无 |
| CPUFREQUENCY | CPU主频 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CPU主频。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~32767。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CPUABILITYCFG]] · 不同CPU类型的能力系数和基础消耗。（CPUABILITYCFG）

## 使用实例

查询一个服务类型为x86_64、代际为1、主频为0的CPU的能力系数为500、基础消耗为1，执行如下命令：

```
LST CPUABILITYCFG: CPUTYPE=X86_64, CPUGENERATE="1", CPUFREQUENCY=0;%%
RETCODE = 0  操作成功

结果如下
--------
 CPU类型  =  X86机器CPU类型
 CPU代际  =  1
 CPU主频  =  0
能力系数  =  500
基础消耗  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CPUABILITYCFG.md`
