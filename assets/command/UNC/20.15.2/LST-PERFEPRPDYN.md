---
id: UNC@20.15.2@MMLCommand@LST PERFEPRPDYN
type: MMLCommand
name: LST PERFEPRPDYN（查询EpRpDyn性能统计对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFEPRPDYN
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST PERFEPRPDYN（查询EpRpDyn性能统计对象）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于查询EpRpDyn性能统计对象。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定EpRpDyn性能统计的接口类型。<br>数据来源：本端规划<br>取值范围：<br>- S5S8PGW（PGW-C S5/S8接口）<br>- S11SGW（SGW-C S11接口）<br>- S5S8SGW（SGW-C S5/S8接口）<br>- SXASGW（SGW-C Sxa接口）<br>- SXBPGW（PGW-C Sxb接口）<br>- SXGGSN（GGSN-C Sx接口）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFEPRPDYN]] · EpRpDyn性能统计对象（PERFEPRPDYN）

## 使用实例

查询接口类型为S5S8PGW的EpRpDyn对象，执行如下命令：

```
%%LST PERFEPRPDYN: INTERFACETYPE=S5S8PGW;%%
RETCODE = 0  操作成功

结果如下
--------
接口类型  =  PGW-C S5/S8接口
对象名称  =  pgw1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFEPRPDYN.md`
