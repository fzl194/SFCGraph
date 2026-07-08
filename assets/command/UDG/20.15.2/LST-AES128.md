---
id: UDG@20.15.2@MMLCommand@LST AES128
type: MMLCommand
name: LST AES128（查询aes128加密算法的IV值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AES128
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- AES128加密算法的IV值
status: active
---

# LST AES128（查询aes128加密算法的IV值）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询aes128加密算法的IV值。当重定向或者头增强配置需要对imsi、msisdn、imei、msip进行aes128加密处理时，使用该数值作为加密算法的IV值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/AES128]] · aes128加密算法的IV值（AES128）

## 使用实例

查询aes128加密算法的IV值，查询命令如下：

```
LST AES128:;
```

```

RETCODE = 0  操作成功。

aes128加密算法的IV值信息
---------------------------------
    重定向随机IV值开关  = 不使能
重定向动作AES128的IV值  =  *****
    头增强随机IV值开关  = 不使能
头增强动作AES128的IV值  =  *****
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AES128.md`
