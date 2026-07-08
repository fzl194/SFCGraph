---
id: UNC@20.15.2@MMLCommand@LST NRFNOTIFYPLY
type: MMLCommand
name: LST NRFNOTIFYPLY（查询NRF通知策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNOTIFYPLY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF通知管理
status: active
---

# LST NRFNOTIFYPLY（查询NRF通知策略）

## 功能

**适用NF：NRF**

该命令用于查询NRF上的通知策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNOTIFYPLY]] · NRF通知策略（NRFNOTIFYPLY）

## 使用实例

运营商希望查询当前NRF上通知策略，执行如下命令。

```
LST NRFNOTIFYPLY:;
%%LST NRFNOTIFYPLY;%%
RETCODE = 0  操作成功

结果如下
---------
 NRF通知策略  =  NFINSTANCEIDNOT 
内部通知策略  =  DEFAULT
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF通知策略（LST-NRFNOTIFYPLY）_60209801.md`
