---
id: UNC@20.15.2@MMLCommand@LST NRFSMSFSEGSW
type: MMLCommand
name: LST NRFSMSFSEGSW（查询SMSF号段白名单功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSMSFSEGSW
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

# LST NRFSMSFSEGSW（查询SMSF号段白名单功能开关）

## 功能

**适用NF：NRF**

该命令用于查询SMSF号段白名单开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFSMSFSEGSW]] · SMSF号段白名单功能开关（NRFSMSFSEGSW）

## 使用实例

查询SMSF号段白名单功能开关。

```
LST NRFSMSFSEGSW:;
%%LST NRFSMSFSEGSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
SMSF号段白名单开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFSMSFSEGSW.md`
