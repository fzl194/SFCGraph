---
id: UNC@20.15.2@MMLCommand@LST NFREGIONINFO
type: MMLCommand
name: LST NFREGIONINFO（查询本端NF大区和省份数据管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFREGIONINFO
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF概述信息管理
status: active
---

# LST NFREGIONINFO（查询本端NF大区和省份数据管理参数）

## 功能

**适用NF：AMF、SMF、NCG**

该命令用于查询运营商规划的网元所在的区域信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFREGIONINFO]] · 本端NF大区和省份数据管理参数（NFREGIONINFO）

## 使用实例

查询运营商规划的网元所在的区域信息：

```
%%LST NFREGIONINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
网元ID中区域起始位  =  9
网元ID中区域结束位  =  16
网元ID中省份起始位  =  17
网元ID中省份结束位  =  24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本端NF大区和省份数据管理参数（LST-NFREGIONINFO）_24956634.md`
