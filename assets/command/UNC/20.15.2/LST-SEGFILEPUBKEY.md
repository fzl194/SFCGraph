---
id: UNC@20.15.2@MMLCommand@LST SEGFILEPUBKEY
type: MMLCommand
name: LST SEGFILEPUBKEY（查询号段配置文件的签名验证公钥）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SEGFILEPUBKEY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入文件公钥管理
status: active
---

# LST SEGFILEPUBKEY（查询号段配置文件的签名验证公钥）

## 功能

**适用NF：NRF**

该命令用于查询号段配置文件的签名验证公钥。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SEGFILEPUBKEY]] · 号段配置文件的签名验证公钥（SEGFILEPUBKEY）

## 使用实例

查询号段配置文件签名验证公钥信息：

```
LST SEGFILEPUBKEY:;
%%LST SEGFILEPUBKEY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
公钥名称  =  keyname001
公钥信息  =  -----BEGIN PUBLIC KEY-----#MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsog/61GMt1h6iePkMilD#L7PUuZ41aI8swe/aJAUMlDORsGkoOvkUxRZitBccUr/5yThXb1el5TSUpibGCbEj#YWJmpPSbTQzOQUKTYHwB3Ex23Qo5C3ByeN9HgzUKZMghNeHw5IUIKU/9PKp34bVX#/If2u4q+bPrGqFZ7Uqf/HM2eD8LR2POVSgyngNDCKt5MI5DVx4Kj5JmdaZHmJppD#/72qzxLXdJGH79z3M/Z2MtJ7jp4ZEi+MtOnyqx7Tvrm3A/9bWRghDCLUjxKzHvbi#NTVrf8QDpO2J1FkMmsTBsLJAHyA+rCB11J9OFCObF5HaS6ZqKrOz/FD/mAsLZZi7#gwIDAQAB#-----END PUBLIC KEY-----#
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询号段配置文件的签名验证公钥（LST-SEGFILEPUBKEY）_09653001.md`
