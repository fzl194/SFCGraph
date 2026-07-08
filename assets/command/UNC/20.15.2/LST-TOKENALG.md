---
id: UNC@20.15.2@MMLCommand@LST TOKENALG
type: MMLCommand
name: LST TOKENALG（查询Token签名算法）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TOKENALG
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- Token管理
- Token算法管理
status: active
---

# LST TOKENALG（查询Token签名算法）

## 功能

**适用NF：NRF**

NF服务消费者获取到Token后，携带Token访问NF服务提供方的服务。NF服务提供方会对NF服务消费者进行认证，校验Token是否正确，校验过程中NF会使用到公钥和NRF侧配置的Token签名算法。

该命令用于查询Token的签名算法。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/TOKENALG]] · Token签名算法（TOKENALG）

## 使用实例

查询Token的签名算法：

```
LST TOKENALG:
%%LST TOKENALG:;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
 算法名称  =  RS384
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TOKENALG.md`
