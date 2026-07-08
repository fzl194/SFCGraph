---
id: UDG@20.15.2@MMLCommand@LST IOTCAPABILITY
type: MMLCommand
name: LST IOTCAPABILITY（查询物联网能力上报）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IOTCAPABILITY
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- NB-IOT管理
- 物联网能力
status: active
---

# LST IOTCAPABILITY（查询物联网能力上报）

## 功能

**适用NF：UPF**

该命令用来查看UPF的物联网接入能力上报功能选择指示。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/IOTCAPABILITY]] · 物联网能力上报（IOTCAPABILITY）

## 使用实例

查询UPF的物联网接入能力上报功能开关配置：

```
LST IOTCAPABILITY:;
```

```

RETCODE = 0 操作成功。

物联网能力
------------------------------------
NB-IoT接入能力上报 = ENABLE
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询物联网能力上报（LST-IOTCAPABILITY）_70824409.md`
