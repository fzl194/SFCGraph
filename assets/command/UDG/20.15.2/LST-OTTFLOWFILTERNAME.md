---
id: UDG@20.15.2@MMLCommand@LST OTTFLOWFILTERNAME
type: MMLCommand
name: LST OTTFLOWFILTERNAME（查询外置规则库OTT flow filter信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OTTFLOWFILTERNAME
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 百万级业务规则库
- ESA业务信息
status: active
---

# LST OTTFLOWFILTERNAME（查询外置规则库OTT flow filter信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示通过命令行LOD EXTERNALDB加载的外置OTT数据库中定义的Flow Filter的名称。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [外置规则库OTT flow filter信息（OTTFLOWFILTERNAME）](configobject/UDG/20.15.2/OTTFLOWFILTERNAME.md)

## 使用实例

运营商查询本地配置的外置流过滤器实例信息：

```
LST OTTFLOWFILTERNAME:;
```

```

RETCODE = 0 操作成功.

外置OTT flow-filter信息：
------------------------
OTTFlowFilterName
f_im
f_voip

(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询外置规则库OTT-flow-filter信息（LST-OTTFLOWFILTERNAME）_93531883.md`
