---
id: UDG@20.15.2@MMLCommand@RMV POOLGRPMAP
type: MMLCommand
name: RMV POOLGRPMAP（移除地址池组映射关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: POOLGRPMAP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池组映射关系
status: active
---

# RMV POOLGRPMAP（移除地址池组映射关系）

## 功能

**适用NF：PGW-U、UPF**

![](移除地址池组映射关系（RMV POOLGRPMAP）_82837149.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果删除映射，将导致原有规则下的地址资源减少，可能导致激活失败， 删除时确认剩余的地址资源是否可以满足业务诉求。

该命令用于删除指定TAC-Group/LAC-Group、APN、SMF到地址池组的映射规则。

## 注意事项

- 该命令执行后只对新激活用户生效。
- PoolGrpMap对象本身为SMF/APN/位置区组与地址池组之间的绑定关系，不支持修改。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAPPINGNAME | 映射规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定映射规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@POOLGRPMAP]] · 地址池组映射关系（POOLGRPMAP）

## 使用实例

删除名为mapping1的映射规则：

```
RMV POOLGRPMAP: MAPPINGNAME="mapping1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-POOLGRPMAP.md`
