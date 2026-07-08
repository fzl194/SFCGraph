---
id: UNC@20.15.2@MMLCommand@LST QOSMONT
type: MMLCommand
name: LST QOSMONT（查询QoS监测配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSMONT
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- QoS监测管理
- QoS监测控制
status: active
---

# LST QOSMONT（查询QoS监测配置）

## 功能

**适用NF：SMF**

该命令用于查询QoS监测配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSMONT]] · QoS监测配置（QOSMONT）

## 使用实例

查询QoS监测配置，执行如下命令：

```
%%LST QOSMONT:;%%
RETCODE = 0  操作成功

结果如下
--------
           QoS监测开关 = 使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSMONT.md`
