---
id: UNC@20.15.2@MMLCommand@LST DNAIUPSELPLY
type: MMLCommand
name: LST DNAIUPSELPLY（查询DNAI粒度的UPF选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNAIUPSELPLY
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- DNAI粒度的UPF选择策略
status: active
---

# LST DNAIUPSELPLY（查询DNAI粒度的UPF选择策略）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询DNAI粒度的UPF选择策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNAIUPSELPLY]] · DNAI粒度的UPF选择策略（DNAIUPSELPLY）

## 使用实例

查询DNAI为huawei.com的UPF选择策略： 2.查询所有DNAI粒度的UPF选择策略：

```
%%LST DNAIUPSELPLY: DNAI="huawei.com";%%
RETCODE = 0  Operation succeeded

The result is as follows
--------
                                  Data Network Access Identifier  =  huawei.com
Shared UPF Preferential Selection Switch in Traffic Distribution  =  INHERIT
                             Priority-based UPF Selection Switch  =  INHERIT
                                 Load-based UPF Selection Switch  =  INHERIT
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNAIUPSELPLY.md`
