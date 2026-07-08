---
id: UNC@20.15.2@MMLCommand@LST NRFSMSFCUTPLY
type: MMLCommand
name: LST NRFSMSFCUTPLY（查询SMSF割接场景NRF处理策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSMSFCUTPLY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- SMSF割接场景NRF处理策略
status: active
---

# LST NRFSMSFCUTPLY（查询SMSF割接场景NRF处理策略）

## 功能

**适用NF：NRF**

该命令用于查询SMSF割接场景下，NRF的处理策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSMSFCUTPLY]] · SMSF割接场景NRF处理策略（NRFSMSFCUTPLY）

## 使用实例

运营商希望查询控制SMSF割接时NRF服务发现的匹配策略，执行如下命令：

```
LST NRFSMSFCUTPLY:;
%%LST NRFSMSFCUTPLY:;%%
RETCODE = 0  操作成功

结果如下
---------
SMSF割接场景NRF发现匹配开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFSMSFCUTPLY.md`
