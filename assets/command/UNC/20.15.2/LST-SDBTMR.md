---
id: UNC@20.15.2@MMLCommand@LST SDBTMR
type: MMLCommand
name: LST SDBTMR（查询核查定时器配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SDBTMR
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 用户数据资源核查
status: active
---

# LST SDBTMR（查询核查定时器配置）

## 功能

**适用网元：SGSN、MME**

此命令用于查询SDB（Subscriber DataBase）系统维护相关的定时器配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SDBTMR]] · 核查定时器配置（SDBTMR）

## 使用实例

查询SDB定时器配置：

LST SDBTMR:;

```
%%LST SDBTMR:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------
用户分离后签约数据保留时间(h)  =  24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询核查定时器配置（LST-SDBTMR）_26305396.md`
