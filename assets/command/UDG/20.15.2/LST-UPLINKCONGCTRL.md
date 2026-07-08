---
id: UDG@20.15.2@MMLCommand@LST UPLINKCONGCTRL
type: MMLCommand
name: LST UPLINKCONGCTRL（查询Diameter链路拥塞控制）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPLINKCONGCTRL
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- Diameter链路拥塞控制
status: active
---

# LST UPLINKCONGCTRL（查询Diameter链路拥塞控制）

## 功能

**适用NF：UPF**

此命令用来查询链路拥塞触发告警和链路拥塞触发重建链相关参数。

## 注意事项

该命令相关的功能当前版本暂不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPLINKCONGCTRL]] · Diameter链路拥塞控制（UPLINKCONGCTRL）

## 使用实例

查询LinkCongCtrl命令配置：

```
LST UPLINKCONGCTRL:;
```

```

RETCODE = 0  操作成功
Diameter链路拥塞控制
--------------------
                告警开关  =  允许
        告警上报检测周期  =  12
      链路重建的检测周期  =  255
触发链路重建的链路拥塞率  =  80
        告警恢复检测周期  =  12
            链路重建开关  =  禁止
触发告警上报的链路拥塞率  =  20
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Diameter链路拥塞控制（LST-UPLINKCONGCTRL）_45195182.md`
