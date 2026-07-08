---
id: UNC@20.15.2@MMLCommand@LST VNFMINFO
type: MMLCommand
name: LST VNFMINFO（查询VNFM对接信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VNFMINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- VNFM管理
status: active
---

# LST VNFMINFO（查询VNFM对接信息）

## 功能

该命令用于查询网元与VNFM的对接信息。

> **说明**
> 该命令仅在非TCA场景下支持。

## 注意事项

VNFM组网信息为IPV6+IPV4双栈场景时，该命令中的主节点IP、备节点IP为IPV6的地址信息。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/VNFMINFO]] · VNFM对接信息（VNFMINFO）

## 使用实例

查询网元与VNFM对接信息。

```
%%LST VNFMINFO:;%%
RETCODE = 0  操作成功
操作结果如下
    VNFM地址  =  https://10.10.10.10:30000
  VNFM用户名  =  restuser_xxx
VNFM主站点IP  =  10.10.10.10
VNFM备站点IP  =  10.10.10.11
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VNFM对接信息（LST-VNFMINFO）_69516020.md`
