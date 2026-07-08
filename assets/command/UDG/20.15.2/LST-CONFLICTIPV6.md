---
id: UDG@20.15.2@MMLCommand@LST CONFLICTIPV6
type: MMLCommand
name: LST CONFLICTIPV6（查询本地地址池中冲突IPv6地址）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CONFLICTIPV6
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 冲突地址管理
- IPv6冲突地址管理
status: active
---

# LST CONFLICTIPV6（查询本地地址池中冲突IPv6地址）

## 功能

**适用NF：UPF**

该命令用来查询指定地址池里的冲突IPv6地址。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [本地地址池中冲突IPv6地址（CONFLICTIPV6）](configobject/UDG/20.15.2/CONFLICTIPV6.md)

## 使用实例

查询本地地址池lap中配置的冲突IPv6地址，POOLNAME为“lap”：

```
LST CONFLICTIPV6: POOLNAME="lap";
```

```

RETCODE = 0 操作成功

冲突IPv6信息
-------------------------
池名称= lap
冲突IPV6地址= fc01:0000:0000:0000:0000:0000:0000:0001
IPv6前缀长度= 63
（结果个数= 1）

---结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询本地地址池中冲突IPv6地址（LST-CONFLICTIPV6）_94212259.md`
