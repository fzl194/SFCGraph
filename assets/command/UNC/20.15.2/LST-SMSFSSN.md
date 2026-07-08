---
id: UNC@20.15.2@MMLCommand@LST SMSFSSN
type: MMLCommand
name: LST SMSFSSN（查询SMSF本局SSN号）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFSSN
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SMSFOPC本局SSN号
status: active
---

# LST SMSFSSN（查询SMSF本局SSN号）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF对接SMSC网元时，SCCP层主叫地址中携带的SSN号。

## 注意事项

- 该命令执行后立即生效。

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFSSN]] · SMSF本局SSN号（SMSFSSN）

## 使用实例

查询SMSF的主叫地址的子系统号：

```
LST SMSFSSN:;
```

```
%%LST SMSFSSN:;%%
RETCODE = 0  操作成功

输出结果如下
------------
子系统号  =  VLR(7)
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMSF本局SSN号（LST-SMSFSSN）_67848008.md`
