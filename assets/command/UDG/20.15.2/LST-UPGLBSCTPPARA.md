---
id: UDG@20.15.2@MMLCommand@LST UPGLBSCTPPARA
type: MMLCommand
name: LST UPGLBSCTPPARA（查询SCTP全局参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPGLBSCTPPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- SCTP管理
- SCTP基础参数
status: active
---

# LST UPGLBSCTPPARA（查询SCTP全局参数）

## 功能

**适用NF：UPF**

此命令用于查询SCTP全局参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPGLBSCTPPARA]] · SCTP全局参数（UPGLBSCTPPARA）

## 使用实例

查询SCTP全局参数：

```
LST UPGLBSCTPPARA:;
```

```

RETCODE = 0  操作成功
SCTP全局参数
------------
           SCTP路径选择模式  =  仅平行路径为可用路径
RTO重发超时的最小值（毫秒）  =  500
RTO重发超时的最大值（毫秒）  =  1500
RTO重发超时的初始值（毫秒）  =  500
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPGLBSCTPPARA.md`
