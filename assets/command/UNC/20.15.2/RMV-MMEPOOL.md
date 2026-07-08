---
id: UNC@20.15.2@MMLCommand@RMV MMEPOOL
type: MMLCommand
name: RMV MMEPOOL（删除MME POOL）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMEPOOL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- MME Pool
status: active
---

# RMV MMEPOOL（删除MME POOL）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于删除MME POOL。假设运营商不再使用MME POOL时，使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEPOOLNAME | MME POOL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEPOOL]] · MME POOL（MMEPOOL）

## 使用实例

假设要删除一个名为“mmepool1”的MME POOL：

```
RMV MMEPOOL:MMEPOOLNAME="mmepool1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MME-POOL（RMV-MMEPOOL）_31453522.md`
