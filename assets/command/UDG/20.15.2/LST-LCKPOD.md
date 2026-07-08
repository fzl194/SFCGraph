---
id: UDG@20.15.2@MMLCommand@LST LCKPOD
type: MMLCommand
name: LST LCKPOD（查询锁定的POD）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LCKPOD
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- POD锁定开关
status: active
---

# LST LCKPOD（查询锁定的POD）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

显示已经锁定的POD。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [锁定的POD（LCKPOD）](configobject/UDG/20.15.2/LCKPOD.md)

## 使用实例

显示已经锁定的POD：

```
LST LCKPOD:;
```

```

RETCODE = 0  操作成功

锁定POD信息
-------------
        POD名称  =  ssgpod-0
    锁定POD开关  =  使能
  多PDN接入开关  =  不使能
FullMesh 5G LAN组会话接入开关 = 不使能
(结果个数 = 1)

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询锁定的POD（LST-LCKPOD）_64015272.md`
