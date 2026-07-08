---
id: UDG@20.15.2@MMLCommand@RMV POOL
type: MMLCommand
name: RMV POOL（删除地址池）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: POOL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池配置
status: active
---

# RMV POOL（删除地址池）

## 功能

**适用NF：PGW-U、UPF**

![](删除地址池（RMV POOL）_82837134.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除地址池，使地址池内地址不可用，可能会导致用户激活失败。

该命令在某一地址池不再使用时，可以用来删掉该地址池。

## 注意事项

- 该命令执行后立即生效。
- 如果一个地址池中仍有地址处于使用状态，则不允许删除该地址池。
- 如果地址池和地址池组绑定，需要先解除地址池和地址池组的绑定关系，然后才可以删除地址池。
- 成功删除地址池时其下的section也会同步删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@POOL]] · 地址池（POOL）

## 使用实例

假设运营商不再使用pool1地址池，则需删除地址池pool1：

```
RMV POOL: POOLNAME="pool1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-POOL.md`
